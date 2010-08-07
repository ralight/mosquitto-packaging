##release is the version number of the spec file
%define release 1
%define def_version 0.8

Name:		mosquitto
Release:	%{release}%{?dist}
Summary:	MQTT version 3 compatible message broker

Group:		Development/Tools
License:	BSD
URL:		http://mosquitto.org

%if %{defined version}
Version:	%{version}
Source:		mosquitto-%{version}.tar.gz	
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}
%else
Version:	%{def_version}
Source:		mosquitto-%{def_version}.tar.gz	
BuildRoot:	%{_tmppath}/%{name}-%{def_version}-%{release}
%endif

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
A message broker that supports version 3 of the MQ Telemetry Transport
protocol. MQTT provides a lightweight method of carrying out messaging using a
publish/subscribe model.
This package also contains mosquitto_pub and mosquitto_sub, which are simple
command line clients that can be used with mosquitto or other MQTT brokers

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
install -d $RPM_BUILD_ROOT/etc/event.d
cp service/upstart/mosquitto.conf $RPM_BUILD_ROOT/etc/event.d/mosquitto
#chcon -t textrel_shlib_t '/usr/lib/sqlite3/pcre.so'
#semanage fcontext -a -t textrel_shlib_t '/usr/lib/sqlite3/pcre.so'


%clean
rm -rf $RPM_BUILD_ROOT

%post
id mosquitto 2>&1 >/dev/null || useradd -k /dev/null -r -m -d /var/lib/mosquitto/ -s /sbin/nologin  mosquitto

%postun
if [ $1 -eq 0 ]
then
	userdel -r mosquitto
fi

%files
%defattr(-,root,root,-)
/usr/sbin/mosquitto
%config /etc/mosquitto.conf
/usr/bin/mosquitto_pub
/usr/bin/mosquitto_sub
${_libdir}/libmosquitto.so.0
${_libdir}/libmosquitto.so
${_libdir}/libmosquittopp.so.0
${_libdir}/libmosquittopp.so
/usr/include/mosquitto.h
/usr/include/mosquittopp.h
/etc/event.d/mosquitto
%doc /usr/share/man/man1/mosquitto_pub.1.gz
%doc /usr/share/man/man1/mosquitto_sub.1.gz
%doc /usr/share/man/man3/libmosquitto.3.gz
%doc /usr/share/man/man5/mosquitto.conf.5.gz
%doc /usr/share/man/man7/mqtt.7.gz
%doc /usr/share/man/man8/mosquitto.8.gz

%changelog

