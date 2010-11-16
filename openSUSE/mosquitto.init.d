#! /bin/sh

# Based on /etc/init.d/ssh :
#
# Copyright (c) 1995-2000 SuSE GmbH Nuernberg, Germany.
#
# Author: Jiri Smid <feedback@suse.de>

# /etc/init.d/mosquitto
#
# and symbolic link
#
# /usr/sbin/rcmosquitto

### BEGIN INIT INFO
# Provides: mosquitto
# Required-Start: $network $remote_fs
# Required-Stop: $network $remote_fs
# Default-Start: 3 5
# Default-Stop: 0 1 2 6
# Description: Start the mosquitto mqtt broker
### END INIT INFO

MOSQUITTO_BIN=/usr/sbin/mosquitto
test -x $MOSQUITTO_BIN || exit 5

MOSQUITTO_PIDFILE=/var/run/mosquitto.pid

. /etc/rc.status

case "$1" in
	start)
	echo -n "Starting Mosquitto MQTT broker"
	## Start daemon with startproc(8). If this fails
	## the echo return value is set appropriate.

	startproc -f $MOSQUITTO_BIN $MOSQUITTO_OPTS -o "PidFile=$MOSQUITTO_PIDFILE"

	# Remember status and be verbose
	rc_status -v
	;;
	stop)
	echo -n "Shutting down Mosquitto MQTT broker"
	## Stop daemon with killproc(8) and if this fails
	## set echo the echo return value.

	killproc -p $MOSQUITTO_PIDFILE -TERM $MOSQUITTO_BIN

	# Remember status and be verbose
	rc_status -v
	;;
	try-restart)
		## Stop the service and if this succeeds (i.e. the
		## service was running before), start it again.
		$0 status >/dev/null &&  $0 restart

		# Remember status and be quiet
		rc_status
		;;
	restart)
		## Stop the service and regardless of whether it was
		## running or not, start it again.
		$0 stop
		$0 start

		# Remember status and be quiet
		rc_status
		;;
	force-reload|reload)
	## Signal the daemon to reload its config. Most daemons
	## do this on signal 1 (SIGHUP).

	echo -n "Reload service mosquitto"

	killproc -p $MOSQUITTO_PIDFILE -HUP $MOSQUITTO_BIN

		rc_status -v

		;;
	status)
	echo -n "Checking for service mosquitto "
		## Check status with checkproc(8), if process is running
		## checkproc will return with exit status 0.

		# Status has a slightly different for the status command:
		# 0 - service running
		# 1 - service dead, but /var/run/  pid  file exists
		# 2 - service dead, but /var/lock/ lock file exists
		# 3 - service not running

	checkproc -p $MOSQUITTO_PIDFILE $MOSQUITTO_BIN

	rc_status -v
	;;
	probe)
	## Optional: Probe for the necessity of a reload,
	## give out the argument which is required for a reload.

		test /etc/mosquitto/mosquitto.conf -nt $MOSQUITTO_PIDFILE && echo reload
	;;
	*)
	echo "Usage: $0 {start|stop|status|try-restart|restart|force-reload|reload|probe}"
	exit 1
	;;
esac
rc_exit

