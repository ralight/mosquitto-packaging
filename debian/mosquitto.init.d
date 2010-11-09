#! /bin/sh

### BEGIN INIT INFO
# Provides:		mosquitto
# Required-Start:	$remote_fs $syslog
# Required-Stop:	$remote_fs $syslog
# Default-Start:	2 3 4 5
# Default-Stop:		
# Short-Description:	mosquitto MQTT v3 message broker
### END INIT INFO

set -e

# /etc/init.d/mosquitto: start and stop the mosquitto MQTT message broker

test -x /usr/sbin/mosquitto || exit 0

umask 022

. /lib/lsb/init-functions

# Are we running from init?
run_by_init() {
    ([ "$previous" ] && [ "$runlevel" ]) || [ "$runlevel" = S ]
}

export PATH="${PATH:+$PATH:}/usr/sbin:/sbin"

case "$1" in
  start)
	log_daemon_msg "Starting Mosquitto message broker" "mosquitto"
	if start-stop-daemon --start --quiet --oknodo --pidfile /var/run/mosquitto.pid --exec /usr/sbin/mosquitto -- -d -c /etc/mosquitto/mosquitto.conf ; then
	    log_end_msg 0
	else
	    log_end_msg 1
	fi
	;;
  stop)
	log_daemon_msg "Stopping Mosquitto message broker" "mosquitto"
	if start-stop-daemon --stop --quiet --oknodo --pidfile /var/run/mosquitto.pid; then
	    log_end_msg 0
	else
	    log_end_msg 1
	fi
	;;

  restart)
	log_daemon_msg "Restarting Mosquitto message broker" "mosquitto"
	start-stop-daemon --stop --quiet --oknodo --retry 30 --pidfile /var/run/mosquitto.pid
	check_for_no_start log_end_msg
	check_dev_null log_end_msg
	if start-stop-daemon --start --quiet --oknodo --pidfile /var/run/mosquitto.pid --exec /usr/sbin/mosquitto -- -d -c /etc/mosquitto/mosquitto.conf ; then
	    log_end_msg 0
	else
	    log_end_msg 1
	fi
	;;

  try-restart)
	log_daemon_msg "Restarting Mosquitto message broker" "mosquitto"
	set +e
	start-stop-daemon --stop --quiet --retry 30 --pidfile /var/run/mosquitto.pid
	RET="$?"
	set -e
	case $RET in
	    0)
		# old daemon stopped
		check_for_no_start log_end_msg
		check_dev_null log_end_msg
		if start-stop-daemon --start --quiet --oknodo --pidfile /var/run/mosquitto.pid --exec /usr/sbin/mosquitto -- -d -c /etc/mosquitto/mosquitto.conf ; then
		    log_end_msg 0
		else
		    log_end_msg 1
		fi
		;;
	    1)
		# daemon not running
		log_progress_msg "(not running)"
		log_end_msg 0
		;;
	    *)
		# failed to stop
		log_progress_msg "(failed to stop)"
		log_end_msg 1
		;;
	esac
	;;

  status)
	status_of_proc -p /var/run/mosquitto.pid /usr/sbin/mosquitto mosquitto && exit 0 || exit $?
	;;

  *)
	log_action_msg "Usage: /etc/init.d/mosquitto {start|stop|restart|try-restart|status}"
	exit 1
esac

exit 0
