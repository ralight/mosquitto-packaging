##release is the version number of the spec file
%define release 1
%define def_version 0.9

Name:		mosquitto
Release:	%{release}%{?dist}
Summary:	MQTT version 3 compatible message broker

Group:		Productivity/Networking/Other
License:	BSD
URL:		http://mosquitto.org/

%if "%_lib" == "lib64"
%define LIB_SUFFIX 64
%else
%define LIB_SUFFIX %nil
%endif

%if %{defined version}
Version:	%{version}
Source:		mosquitto-%{version}.tar.gz	
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}
%else
Version:	%{def_version}
Source:		mosquitto-%{def_version}.tar.gz	
BuildRoot:	%{_tmppath}/%{name}-%{def_version}-%{release}
%endif

Requires:  sqlite3 >= 3.5, tcpd
BuildRequires:  sqlite3-devel >= 3.5, tcpd-devel, gcc-c++, python, pwdutils
Source1: mosquitto.init.d

%description
A message broker that supports version 3 of the MQ Telemetry Transport
protocol. MQTT provides a lightweight method of carrying out messaging using a
publish/subscribe model.

%package clients
Summary: Mosquitto command line publish/subscribe clients
Group: Productivity/Networking/Other
Requires: libmosquitto0

%description clients
Two command line MQTT v3.1 clients that can publish and subscribe to an MQTT
broker.

%package -n libmosquitto0
Summary: MQTT C client library
Group: Development/Libraries/C and C++

%description -n libmosquitto0
A library that provides a means of implementing MQTT version 3.1 clients. MQTT
provides a lightweight method of carrying out messaging using a
publish/subscribe model.

%package -n libmosquitto0-devel
Summary: MQTT C client library development files
Requires: libmosquitto0
Group: Development/Libraries/C and C++

%description -n libmosquitto0-devel
This is a library that provides a means of implementing MQTT version 3
clients. MQTT provides a lightweight method of carrying out messaging using a
publish/subscribe model.

%package -n libmosquittopp0
Summary: MQTT C++ client library
Group: Development/Libraries/C and C++

%description -n libmosquittopp0
This is a library that provides a means of implementing MQTT version 3.1
clients using C++. MQTT provides a lightweight method of carrying out messaging
using a publish/subscribe model.

%package -n libmosquittopp0-devel
Summary: MQTT C++ client library development files
Group: Development/Libraries/C and C++

%description -n libmosquittopp0-devel
This is a library that provides a means of implementing MQTT version 3.1
clients in C++. MQTT provides a lightweight method of carrying out messaging
using a publish/subscribe model.

%package -n python-mosquitto
Summary: MQTT Python client library
Group: Development/Libraries/Python
Requires: python

%description -n python-mosquitto
This is a python module that provides a means of implementing MQTT version 3.1
clients. MQTT provides a lightweight method of carrying out messaging using a
publish/subscribe model.

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
make install DESTDIR=$RPM_BUILD_ROOT prefix=/usr LIB_SUFFIX=%{LIB_SUFFIX}
install -d $RPM_BUILD_ROOT/etc/init.d
install -m 0755 %SOURCE1 $RPM_BUILD_ROOT/etc/init.d/mosquitto
ln -sf /etc/init.d/mosquitto /usr/sbin/rcmosquitto
%if %{defined fedora_version}
cp service/upstart/mosquitto.conf $RPM_BUILD_ROOT/etc/event.d/mosquitto
%endif


%clean
rm -rf $RPM_BUILD_ROOT

%post
id mosquitto 2>&1 >/dev/null || useradd -k /dev/null -r -m -d /var/lib/mosquitto/ -s /sbin/nologin  mosquitto
insserv mosquitto

%preun
%stop_on_removal mosquitto

%postun
%restart_on_update mosquitto
insserv -r mosquitto
if [ $1 -eq 0 ]
then
	userdel -r mosquitto
fi

%post -n libmosquitto0
/sbin/ldconfig

%postun -n libmosquitto0
/sbin/ldconfig

%post -n libmosquittopp0
/sbin/ldconfig

%postun -n libmosquittopp0
/sbin/ldconfig

%files
%defattr(-,root,root,-)
/usr/sbin/mosquitto
/etc/init.d/mosquitto
/usr/sbin/rcmosquitto
%config /etc/mosquitto/mosquitto.conf
%doc /usr/share/man/man5/mosquitto.conf.5.*
%doc /usr/share/man/man7/mqtt.7.*
%doc /usr/share/man/man8/mosquitto.8.*

%files clients
%defattr(-,root,root,-)
/usr/bin/mosquitto_pub
/usr/bin/mosquitto_sub
%doc /usr/share/man/man1/mosquitto_pub.1.*
%doc /usr/share/man/man1/mosquitto_sub.1.*

%files -n libmosquitto0
%defattr(-,root,root,-)
%{_libdir}/libmosquitto.so*
%doc /usr/share/man/man3/libmosquitto.3.*

%files -n libmosquitto0-devel
%defattr(-,root,root,-)
/usr/include/mosquitto.h

%files -n libmosquittopp0
%defattr(-,root,root,-)
%{_libdir}/libmosquittopp.so*

%files -n libmosquittopp0-devel
%defattr(-,root,root,-)
/usr/include/mosquittopp.h

%files -n python-mosquitto
%defattr(-,root,root,-)
/usr/lib*/python*/site-packages/mosquitto-0.9*.egg-info
/usr/lib*/python*/site-packages/mosquitto.py*

%changelog
