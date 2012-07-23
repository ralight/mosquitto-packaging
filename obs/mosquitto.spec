Name:       mosquitto
Version:    0.15
Release:    1

License:    BSD
Group:      Productivity/Networking/Other

BuildRoot:  %{_tmppath}/%{name}-%{version}-build

URL:        http://mosquitto.org
Source:     http://mosquitto.org/files/source/mosquitto-%{version}.tar.gz
%if %{defined suse_version}
Source1:    mosquitto.init.d.suse
%else
Source1:    mosquitto.init.d
%endif
Source2:    mosquitto.fw
Source3:    mosquitto.apparmor
Patch1:     mosquitto.conf.patch
%if 0%{?sles_version} == 10
Patch2:     disable-python.patch
%endif

Summary:    MQTT version 3.1 compatible message broker

%if "%_lib" == "lib64"
%define LIB_SUFFIX 64
%else
%define LIB_SUFFIX %nil
%endif

%if %{defined suse_version}
Requires:  tcpd
BuildRequires:  tcpd-devel, gcc-c++, python, pwdutils

%define _fwdefdir /etc/sysconfig/SuSEfirewall2.d/services
%py_requires
PreReq: %insserv_prereq %fillup_prereq

%endif

%if %{defined rhel_version}
BuildRequires:  tcp_wrappers, gcc-c++, python
%endif

%if %{defined centos_version}
BuildRequires:  tcp_wrappers, gcc-c++, python
%endif

%if %{defined fedora_version}
Requires:   tcp_wrappers
BuildRequires:  tcp_wrappers-devel, gcc-c++, python, python-devel
%endif

%if %{defined mdkversion}
Requires:  libwrap0
BuildRequires:  libwrap-devel, gcc-c++, python, python-devel
%endif

%description
A message broker that supports version 3.1 of the MQ Telemetry Transport  
protocol. MQTT provides a method of carrying out messaging using a   
publish/subscribe model. It is lightweight, both in terms of bandwidth   
usage and ease of implementation. This makes it particularly useful at  
the edge of the network where simple embedded devices are in use, such   
as an arduino implementing a sensor.  

%package pub
Summary: Mosquitto command line subscribe client
Group: Productivity/Networking/Other

%description pub
A command line MQTT v3.1 client that can subscribe to an MQTT broker on multiple topics.

%package sub
Summary: Mosquitto command line publish client
Group: Productivity/Networking/Other

%description sub
A command line MQTT v3.1 client that can publish message to an MQTT broker.

%package -n libmosquitto0
Summary: MQTT C client library
Group: Development/Libraries/C and C++

%description -n libmosquitto0
This is a library that provides a means of implementing MQTT version 3.1
clients. MQTT provides a lightweight method of carrying out messaging using a
publish/subscribe model.

%package -n libmosquitto-devel
Summary: MQTT C client library development files
Requires: libmosquitto0
Group: Development/Libraries/C and C++

%description -n libmosquitto-devel
This is a library that provides a means of implementing MQTT version 3.1
clients. MQTT provides a lightweight method of carrying out messaging using a
publish/subscribe model.

%package -n libmosquittopp0
Summary: MQTT C++ client library
Group: Development/Libraries/C and C++

%description -n libmosquittopp0
This is a library that provides a means of implementing MQTT version 3.1
clients. MQTT provides a lightweight method of carrying out messaging using a
publish/subscribe model.

%package -n libmosquittopp-devel
Summary: MQTT C++ client library development files
Group: Development/Libraries/C and C++

%description -n libmosquittopp-devel
This is a library that provides a means of implementing MQTT version 3.1
clients. MQTT provides a lightweight method of carrying out messaging using a
publish/subscribe model.

%if 0%{?sles_version} != 10

%package -n python-mosquitto
Summary: MQTT Python client library
Group: Development/Libraries/Python
Requires: python libmosquitto0

%description -n python-mosquitto
This is a library that provides a means of implementing MQTT version 3.1
clients. MQTT provides a lightweight method of carrying out messaging using a
publish/subscribe model.

%endif # disable python for SLES 10

%prep
%setup -q
%patch1
%if 0%{?sles_version} == 10
%patch2
%endif

%build
make


%install
make install DESTDIR=$RPM_BUILD_ROOT prefix=/usr LIB_SUFFIX=%{LIB_SUFFIX}
%if %{defined fedora_version}
install -d $RPM_BUILD_ROOT/etc/event.d
cp service/upstart/mosquitto.conf $RPM_BUILD_ROOT/etc/event.d/mosquitto
%endif

install -d $RPM_BUILD_ROOT/etc/init.d
%if %{defined suse_version}
install -d $RPM_BUILD_ROOT/etc/apparmor.d
#install firewall definitions format is described here:
#/usr/share/SuSEfirewall2/services/TEMPLATE
mkdir -p $RPM_BUILD_ROOT/%{_fwdefdir}
install -m 644 %SOURCE2 $RPM_BUILD_ROOT/%{_fwdefdir}/mosquitto
install -m 644 %SOURCE3 $RPM_BUILD_ROOT/etc/apparmor.d/usr.sbin.mosquitto
%endif

install -d $RPM_BUILD_ROOT/var/lib/mosquitto
install -m 0755 %SOURCE1 $RPM_BUILD_ROOT/etc/init.d/mosquitto
ln -sf /etc/init.d/mosquitto $RPM_BUILD_ROOT/usr/sbin/rcmosquitto

%clean
rm -rf $RPM_BUILD_ROOT

%post
getent group mosquitto >/dev/null || /usr/sbin/groupadd -o -r mosquitto  
getent passwd mosquitto >/dev/null || /usr/sbin/useradd -r -g mosquitto -d /var/lib/mosquitto -s /bin/false -c "Mosquitto broker" mosquitto  

%preun
%stop_on_removal mosquitto

%postun
%insserv_cleanup
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
/etc/mosquitto
%config /etc/mosquitto/mosquitto.conf
%config /etc/mosquitto/pwfile.example
%config /etc/mosquitto/aclfile.example
%if %{defined fedora_version}
/etc/event.d/mosquitto
%endif
%if %{defined suse_version}
/etc/apparmor.d  
/etc/apparmor.d/usr.sbin.mosquitto  
%config %{_fwdefdir}/mosquitto  
%endif
%doc /usr/share/man/man5/mosquitto.conf.5.*
%doc /usr/share/man/man7/mqtt.7.*
%doc /usr/share/man/man8/mosquitto.8.*
%attr(755,mosquitto,mosquitto) /var/lib/mosquitto/

%files pub
%defattr(-,root,root,-)
/usr/bin/mosquitto_pub
%doc /usr/share/man/man1/mosquitto_pub.1.*

%files sub
%defattr(-,root,root,-)
/usr/bin/mosquitto_sub
%doc /usr/share/man/man1/mosquitto_sub.1.*

%files -n libmosquitto0
%defattr(-,root,root,-)
%{_libdir}/libmosquitto.so.*
%doc /usr/share/man/man3/libmosquitto.3.*

%files -n libmosquitto-devel
%defattr(-,root,root,-)
/usr/include/mosquitto.h
%{_libdir}/libmosquitto.so

%files -n libmosquittopp0
%defattr(-,root,root,-)
%{_libdir}/libmosquittopp.so.*

%files -n libmosquittopp-devel
%defattr(-,root,root,-)
/usr/include/mosquittopp.h
%{_libdir}/libmosquittopp.so

%if 0%{?sles_version} == 10
%else
%files -n python-mosquitto
%defattr(-,root,root,-)
%if ( %{undefined rhel_version} || 0%{?rhel_version} > 599 ) && ( %{undefined centos_version} || 0%{?centos_version} > 599 )
/usr/lib*/python*/site-packages/mosquitto-%{version}*.egg-info
%endif
/usr/lib*/python*/site-packages/mosquitto.py*
%endif

%changelog
