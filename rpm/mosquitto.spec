##release is the version number of the spec file
%define release 2
%define version 0.6.1

Name:		mosquitto
Version:	%{version}
Release:	%{release}%{?dist}
Summary:	A message broker implementing the MQTT protocol version 3.

Group:		Development/Tools
License:	BSD
URL:		http://mosquitto.atchoo.org
Source:		mosquitto-%{version}.tar.gz	
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%if %{defined suse_version}
Requires:  sqlite3 >= 3.6.14.1, tcpd, sqlite3-pcre
BuildRequires:  sqlite3-devel, tcpd-devel
%endif

%if %{defined rhel_version}
Requires:   sqlite >= 3.6.14.1, tcp_wrappers, sqlite3-pcre
BuildRequires:  tcp_wrappers, sqlite >= 3.6.14.1
%endif

%if %{defined centos_version}
Requires:   sqlite >= 3.6.14.1, tcp_wrappers, sqlite3-pcre
BuildRequires:  tcp_wrappers, sqlite >= 3.6.14.1
%endif

%if %{defined fedora_version}
Requires:   sqlite >= 3.6.14.1, tcp_wrappers, sqlite3-pcre
BuildRequires:  tcp_wrappers-devel, sqlite-devel
%endif

%if %{defined mdkversion}
Requires:  libsqlite3 >= 3.6.14.1, libwrap0, sqlite3-pcre
BuildRequires:  libsqlite3-devel, libwrap-devel
%endif

%description
Mosquitto is a message broker that implements the MQ Telemetry Transport protocol version 3. MQTT provides a lightweight method of carrying out messaging using a publish/subscribe model. Probably the most famous example of this is all of the work that Andy Stanford-Clark (one of the originators of MQTT) has done in home monitoring and automation with his twittering house and twittering ferry (but it's not all about twitter!). 

%prep
%setup -q


%build
awk '$1~/^\#persistence$/{print "persistence 1";next}
	$1~/^\#persistence_location$/{print "persistence_location /var/lib/mosquitto/";;next}
	{print $0}' mosquitto.conf > mosquitto.conf.tmp
mv mosquitto.conf.tmp mosquitto.conf

make


%install
rm -rf $RPM_BUILD_ROOT
mkdir $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT prefix=/usr
#chcon -t textrel_shlib_t '/usr/lib/sqlite3/pcre.so'
#semanage fcontext -a -t textrel_shlib_t '/usr/lib/sqlite3/pcre.so'


%clean
rm -rf $RPM_BUILD_ROOT

%post
id mosquitto 2>&1 >/dev/null || useradd -k /dev/null -r -m -d /var/lib/mosquitto/  mosquitto

%postun
if [ $1 eq 0 ]
then
	userdel -r mosquitto
fi

%files
%defattr(-,root,root,-)
/usr/sbin/mosquitto
%config /etc/mosquitto.conf
/usr/bin/mosquitto_pub
/usr/bin/mosquitto_sub
%doc /usr/share/man/man1/mosquitto_pub.1.gz
%doc /usr/share/man/man1/mosquitto_sub.1.gz
%doc /usr/share/man/man5/mosquitto.conf.5.gz
%doc /usr/share/man/man7/mqtt.7.gz
%doc /usr/share/man/man8/mosquitto.8.gz

%changelog

