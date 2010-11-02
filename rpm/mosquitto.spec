##release is the version number of the spec file
%define release 1
%define def_version 0.9

Name:		mosquitto
Release:	%{release}%{?dist}
Summary:	MQTT version 3 compatible message broker

Group:		Productivity/Networking/Other
License:	BSD
URL:		http://mosquitto.org

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

%if %{defined suse_version}
Requires:  sqlite3, tcpd
BuildRequires:  sqlite3-devel, tcpd-devel, gcc-c++, python
%endif

%if %{defined rhel_version}
BuildRequires:  tcp_wrappers, sqlite >= 3, gcc-c++, python
%endif

%if %{defined centos_version}
BuildRequires:  tcp_wrappers, sqlite >= 3, gcc-c++, python
%endif

%if %{defined fedora_version}
Requires:   sqlite >= 3, tcp_wrappers
BuildRequires:  tcp_wrappers-devel, sqlite-devel, gcc-c++, python, python-devel
%endif

%if %{defined mdkversion}
Requires:  libsqlite3, libwrap0
BuildRequires:  libsqlite3-devel, libwrap-devel, gcc-c++, python, python-devel
%endif

%description
A message broker that supports version 3 of the MQ Telemetry Transport
protocol. MQTT provides a lightweight method of carrying out messaging using a
publish/subscribe model.

%package clients
Summary: Mosquitto command line pub/sub clients
Group: Productivity/Networking/Other
Requires: libmosquitto0

%description clients
Group: Productivity/Networking/Other
This is two MQTT version 3 clients. The first can publish messages to a broker,
the second can subscribe to multiple topics on a broker.

%package -n libmosquitto0
Summary: MQTT C client library
Group: Development/Libraries/C and C++

%description -n libmosquitto0
This is a library that provides a means of implementing MQTT version 3
clients. MQTT provides a lightweight method of carrying out messaging using a
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
This is a library that provides a means of implementing MQTT version 3
clients. MQTT provides a lightweight method of carrying out messaging using a
publish/subscribe model.

%package -n libmosquittopp0-devel
Summary: MQTT C++ client library development files
Group: Development/Libraries/C and C++

%description -n libmosquittopp0-devel
This is a library that provides a means of implementing MQTT version 3
clients. MQTT provides a lightweight method of carrying out messaging using a
publish/subscribe model.

%package -n python-mosquitto
Summary: MQTT Python client library
Group: Development/Libraries/Python
Requires: python

%description -n python-mosquitto
This is a library that provides a means of implementing MQTT version 3
clients. MQTT provides a lightweight method of carrying out messaging using a
publish/subscribe model.

%prep
%setup -q


%build
awk '$1~/^\#persistence$/{print "persistence 1";next}
	$1~/^\#persistence_location$/{print "persistence_location /var/lib/mosquitto/";;next}
	{print $0}' mosquitto.conf > mosquitto.conf.tmp
mv mosquitto.conf.tmp mosquitto.conf
%if 0%{?suse_version}<1130 && %{undefined fedora_version}
sed -i 's/DIRS=lib client src man/DIRS=lib client man/' Makefile
sed -i '/mosquitto.conf/d' Makefile
sed -i '/man8/d' man/Makefile
sed -i '/man7/d' man/Makefile
sed -i '/man5/d' man/Makefile
%endif
make


%install
rm -rf $RPM_BUILD_ROOT
mkdir $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT prefix=/usr LIB_SUFFIX=%{LIB_SUFFIX}
install -d $RPM_BUILD_ROOT/etc/event.d
%if %{defined fedora_version}
cp service/upstart/mosquitto.conf $RPM_BUILD_ROOT/etc/event.d/mosquitto
%endif
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
%config /etc/mosquitto.conf
%if %{defined fedora_version}
/etc/event.d/mosquitto
%endif
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
%if %{undefined rhel_version} && %{undefined centos_version}
/usr/lib*/python*/site-packages/mosquitto-0.8*.egg-info
%endif
/usr/lib*/python*/site-packages/mosquitto.py*

%changelog
