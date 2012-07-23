<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
    "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
    <meta http-equiv="Content-Script-Type" content="text/javascript"/>
    <meta http-equiv="Content-Style-Type" content="text/css"/>

    <link href="/favicon.ico" rel="shortcut icon" />

    <title>File mosquitto.init.d of Package mosquitto - openSUSE Build Service</title>

    <link href="https://static.opensuse.org/themes/bento/css/style.css?1310589270" media="screen" rel="stylesheet" title="Normal" type="text/css" />
    <link href="https://static.opensuse.org/hosts/build2.o.o/stylesheets/style.css?1331733753" media="screen" rel="stylesheet" type="text/css" />

      <link href="https://static.opensuse.org/hosts/build2.o.o/stylesheets/package.css?1274082977" media="all" rel="stylesheet" type="text/css" />
  <link href="https://static.opensuse.org/hosts/build2.o.o/stylesheets/cm2/suse.css?1342168774" media="screen" rel="stylesheet" type="text/css" />
  <style type="text/css">
    .CodeMirror-scroll {
      height: 600px;
      width: auto;
    }
  </style>


    <script src="https://static.opensuse.org/hosts/build2.o.o/javascripts/layout-squashed.js?1331733753" type="text/javascript"></script>

<script type="text/javascript">
//<![CDATA[
      
      var _paq = _paq || [];
      $(function() {
        var u = (("https:" == document.location.protocol) ? "https://beans.opensuse.org/piwik/" : "http://beans.opensuse.org/piwik/");
        _paq.push(['setSiteId', 8]);
        _paq.push(['setTrackerUrl', u + 'piwik.php']);
        _paq.push(['trackPageView']);
        _paq.push(['setDomains', ["*.opensuse.org"]]);
        var d = document,
        g = d.createElement('script'),
        s = d.getElementsByTagName('script')[0];
        g.type = 'text/javascript';
        g.defer = true;
        g.async = true;
        g.src = u + 'piwik.js';
        s.parentNode.insertBefore(g, s);
        
  $("#advanced_tabs_trigger").click(function() {
    $("#advanced_tabs").show();
    $("#advanced_tabs_trigger").remove();
  });

      });
        var CSRF_PROTECT_AUTH_TOKEN = "OuWnByLv8h0Ps1QwED3VE0ZPD2a6kJ1gWSUwl0lbXxA=";

//]]>
</script>  </head>

  <body>

        <script src="https://static.opensuse.org/themes/bento/js/l10n/global-navigation-data-en_US.js?1339683239" type="text/javascript"></script>
<script src="https://static.opensuse.org/themes/bento/js/global-navigation.js?1310589270" type="text/javascript"></script>

    <!-- Start: Header -->
    <div id="header">

      <div id="header-content" class="container_12">

        <a href="/" id="header-logo"><img alt="Header-logo" height="26" src="https://static.opensuse.org/themes/bento/images/header-logo.png?1310589270" width="46" /></a>
      <ul id="global-navigation">
        <!-- change link to en.o.o after transition -->
        <li id="item-downloads"><a href="http://wiki.opensuse.org//openSUSE:Browse#Downloads">Downloads</a></li>
        <li id="item-support"><a href="http://wiki.opensuse.org//openSUSE:Browse#Support">Support</a></li>
        <li id="item-community"><a href="http://wiki.opensuse.org//openSUSE:Browse#Community">Community</a></li>
        <li id="item-development"><a href="http://wiki.opensuse.org//openSUSE:Browse#Development">Development</a></li>
        </ul>

        

<form action="/search/search" class="label-overlay" id="global-search-form" method="post"><div style="margin:0;padding:0;display:inline"><input name="authenticity_token" type="hidden" value="OuWnByLv8h0Ps1QwED3VE0ZPD2a6kJ1gWSUwl0lbXxA=" /></div>  <div style="display: inline">
    <label for="search">Search</label>
    <input id="search" name="search_text" type="text" value="" />    <input type="submit" value="Search" class="hidden" />
  </div>
</form>


      </div>
    </div>
    <!-- End: Header -->



    <div id="subheader" class="container_16">
      <div id="breadcrump" class="grid_10 alpha">
        <img alt="Home_grey" src="https://static.opensuse.org/themes/bento/images/home_grey.png?1274082993" /><a href="/">openSUSE Build Service</a>
            &gt;
                          <a href="/project/list_public">Projects</a>
            &gt;
             <!-- multiple items in crump list but they belong together as sub group, eg sub projects -->
              <a href="/project/show?project=home%3Aoojah">home:oojah</a>:<a href="/project/show?project=home%3Aoojah%3Amqtt">mqtt</a>
            &gt;
                          <a href="/project/packages?project=home%3Aoojah%3Amqtt">Packages</a>
            &gt;
                          <a href="/package/show?package=mosquitto&amp;project=home%3Aoojah%3Amqtt">mosquitto</a>
            &gt;
                          <a href="/package/files?package=mosquitto&amp;project=home%3Aoojah%3Amqtt&amp;rev=10a685a61417414407ba601fb1730dae">Files</a>
            &gt;
                          mosquitto.init.d
      </div>

      <div class="grid_6 omega" style="text-align: right;">
        <a href="https://secure-www.novell.com/selfreg/jsp/createOpenSuseAccount.jsp?%22https://build.opensuse.org/package/view_file?file=mosquitto.init.d&amp;package=mosquitto&amp;project=home%3Aoojah%3Amqtt&amp;rev=10a685a61417414407ba601fb1730dae%22">Register</a> |
      <a href="/user/login" id="login-trigger">Login</a>
      <div id="login-form">
<form action="https://build.opensuse.org/ICSLogin/auth-up" enctype="application/x-www-form-urlencoded" id="login_form" method="post"><div style="margin:0;padding:0;display:inline"><input name="authenticity_token" type="hidden" value="OuWnByLv8h0Ps1QwED3VE0ZPD2a6kJ1gWSUwl0lbXxA=" /></div>          <p>
            <input id="url" name="url" type="hidden" value="https://build.opensuse.org/package/view_file?file=mosquitto.init.d&amp;package=mosquitto&amp;project=home%3Aoojah%3Amqtt&amp;rev=10a685a61417414407ba601fb1730dae" />
            <input id="context" name="context" type="hidden" value="default" />
            <input id="proxypath" name="proxypath" type="hidden" value="reserve" />
            <input id="message" name="message" type="hidden" value="Please log in" />
            <input id="return_to_path" name="return_to_path" type="hidden" value="/package/view_file?file=mosquitto.init.d&amp;package=mosquitto&amp;project=home%3Aoojah%3Amqtt&amp;rev=10a685a61417414407ba601fb1730dae" />
            <label for="username">Username</label>
            <input id="username" name="username" type="text" value="" />
          </p>
          <p>
            <label for="password">Password</label>
            <input id="password" name="password" type="password" value="" />
          </p>
          <p><input name="commit" onclick="fillEmptyFields();" type="submit" value="Login" /></p>
          <p class="slim-footer"><a href="#" id="close-login">Cancel</a></p>
</form>      </div>
</div>

    </div>

    

    <!-- this is needed for the delete confirm dialogues -->
    <div id="dialog_wrapper" style="display: none"></div>

    <!-- Start: Main Content Area -->
    <div id="content" class="container_16 content-wrapper">
        <div class="grid_16 box box-shadow alpha omega">
          



<div class="box-header header-tabs">
  <ul id="package_tabs">
    <li><a href="/package/show?package=mosquitto&amp;project=home%3Aoojah%3Amqtt">Overview</a></li>
    <li><a href="/package/files?package=mosquitto&amp;project=home%3Aoojah%3Amqtt">Sources</a></li>
      <li><a href="/package/repositories?package=mosquitto&amp;project=home%3Aoojah%3Amqtt">Repositories</a></li>
      <li><a href="/package/revisions?package=mosquitto&amp;project=home%3Aoojah%3Amqtt">Revisions</a></li>
      <li><a href="/package/requests?package=mosquitto&amp;project=home%3Aoojah%3Amqtt">Requests</a></li>
      <li><a href="/package/users?package=mosquitto&amp;project=home%3Aoojah%3Amqtt">Users</a></li>
      <li><a href="#" id="advanced_tabs_trigger">Advanced</a></li>
  </ul>
    <div id="advanced_tabs" class="hidden">
      <ul>
        <li><a href="/package/attributes?package=mosquitto&amp;project=home%3Aoojah%3Amqtt">Attributes</a></li>
        <li><a href="/package/meta?package=mosquitto&amp;project=home%3Aoojah%3Amqtt">Meta</a></li>
      </ul>
    </div>
</div>


<h3>File mosquitto.init.d of Package mosquitto</h3>
  <p>Currently displaying revision <i>10a685a61417414407ba601fb1730dae</i>, <a href="/package/view_file?file=mosquitto.init.d&amp;package=mosquitto&amp;project=home%3Aoojah%3Amqtt">show latest</a></p>

<p>
    

<script src="https://static.opensuse.org/hosts/build2.o.o/javascripts/cm2/codemirror.js?1332325040" type="text/javascript"></script>
<script src="https://static.opensuse.org/hosts/build2.o.o/javascripts/cm2/codemirror-ui.js?1320674799" type="text/javascript"></script>
<script src="https://static.opensuse.org/hosts/build2.o.o/javascripts/cm2/mode/d.js" type="text/javascript"></script>

<textarea id="editor_327426020545352" name="editor_327426020545352" style="display: none;" rows="0" cols="0">#! /bin/sh
# Based on /etc/init.d/sshd as it came on CentOS 5.6:
#
# Copyright (c) 1995-2000 SuSE GmbH Nuernberg, Germany.
#
# Author: Jiri Smid &lt;feedback@suse.de&gt;

# /etc/init.d/mosquitto
#

### BEGIN INIT INFO
# Provides: mosquitto
# Required-Start: $network $remote_fs
# Required-Stop: $network $remote_fs
# Default-Start: 3 5
# Default-Stop: 0 1 2 6
# Short-Description: Mosquitto MQTT broker
# Description: Mosquitto MQTT broker
### END INIT INFO

MOSQUITTO_BIN=/usr/sbin/mosquitto
test -x $MOSQUITTO_BIN || exit 5
prog=&quot;mosquitto&quot;

MOSQUITTO_PIDFILE=/var/run/mosquitto.pid

. /etc/rc.d/init.d/functions

start()
{
	echo -n &quot;Starting Mosquitto MQTT broker&quot;
	## Start daemon with startproc(8). If this fails
	## the echo return value is set appropriate.

	$MOSQUITTO_BIN -d -c /etc/mosquitto/mosquitto.conf &amp;&amp; success || failure
	RETVAL=$?
	[ &quot;$RETVAL&quot; = 0 ] &amp;&amp; touch /var/lock/mosquitto
        echo
}

stop()
{
	echo -n &quot;Shutting down Mosquitto MQTT broker&quot;
        ## Stop daemon with killproc(8) and if this fails
        ## set echo the echo return value.
	if [ -n &quot;`pidfileofproc $MOSQUITTO_BIN`&quot; ] ; then
        	#killproc -p $MOSQUITTO_PIDFILE -TERM $MOSQUITTO_BIN
		killproc $MOSQUITTO_BIN
	else
		failure $&quot;Stopping $prog&quot;
	fi
	RETVAL=$?

	[ &quot;$RETVAL&quot; = 0 ] &amp;&amp; rm -f /var/lock/mosquitto
	echo
}

reload()
{
	echo -n $&quot;Reloading $prog: &quot;
        if [ -n &quot;`pidfileofproc $MOSQUITTO_BIN`&quot; ] ; then
            killproc $MOSQUITTO_BIN -HUP
        else
            failure $&quot;Reloading $prog&quot;
        fi
        RETVAL=$?
        echo
}

case &quot;$1&quot; in
	start)
		start
		;;
	stop)
		stop
		;;
	restart)
		## Stop the service and regardless of whether it was
		## running or not, start it again.
		$0 stop
		$0 start
		;;
	force-reload|reload)
		reload
		;;
	status)
		status -p $MOSQUITTO_PIDFILE mosquitto
		RETVAL=$?
		;;
	*)
	echo &quot;Usage: $0 {start|stop|status|restart|force-reload|reload}&quot;
	exit 1
	;;
esac
exit $RETVAL

</textarea>
<script type="text/javascript">
//<![CDATA[
  var codeMirrorOptions = {
    mode: 'd',
    lineNumbers: true,
    matchBrackets: true,
    onCursorActivity: function(editor) {
      editor.setLineClass(editor.hlLine, null);
      editor.hlLine = editor.setLineClass(editor.getCursor().line, "activeline");
    },
  }
    codeMirrorOptions['readOnly'] = true;
    var editor = CodeMirror.fromTextArea(document.getElementById('editor_327426020545352'), codeMirrorOptions);

//]]>
</script>
</p>

        </div>
    </div>
    <!-- End: Main Content Area -->


    <div style="clear: both;"></div>
    <!-- Start: Footer -->
    <div id="footer" class="container_12">

      <div class="box_content grid_3">
        <strong class="grey-medium spacer1">Locations</strong>
        <ul>
          <li><a href="/project/list_public">Projects</a></li>
          <li><a href="/search">Search</a></li>
            <li><a href="/monitor">Status Monitor</a></li>
        </ul>
      </div>

      <div class="box_content grid_3">
        <strong class="grey-medium spacer1">Help</strong>
        <ul>
              <li><a href="http://wiki.opensuse.org/Portal:Build_Service">Open Build Service Portal</a></li>
              <li><a href="http://wiki.opensuse.org/openSUSE:Build_Service_Tutorial">Building Packages</a></li>
              <li><a href="http://en.opensuse.org/openSUSE:Specfile_guidelines">Writing spec Files</a></li>
              <li><a href="http://en.opensuse.org/openSUSE:Submitting_bug_reports">Reporting a Bug</a></li>
              <li><a href="http://forums.opensuse.org/english/other-forums/development/open-build-service-obs/">Forums</a></li>
        </ul>
      </div>

      
  <strong class="grey-medium spacer1">Sponsor</strong>
  <p>
    <a href="http://en.opensuse.org/Sponsors"><img alt="Sponsor_ip-exchange2" src="https://static.opensuse.org/themes/bento/images/sponsors/sponsor_ip-exchange2.png?1274868374" /></a>
  </p>


      <div id="footer-legal" class="grid_12">
        <p>
          <a href="http://openbuildservice.org">Open Build Service (OBS)</a> is an <a href="http://www.opensuse.org">openSUSE project</a>.
        </p>
      </div>

    </div>
    <!-- End: Footer -->


  </body>
</html>
