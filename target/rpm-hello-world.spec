Name:		rpm-hello-world
Version:	0.0.1-SNAPSHOT
Release:	1%{?dist}
Summary:	Spring Boot Starter Parent

Group:		Applications/System			
License:	MIT	
URL:		https://github.com/Chomeh/java-rpm-example.git		
Source0:	%{name}-%{version}-rpm.tar.gz	
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:	noarch
#Requires:	java-1.7.0-openjdk
Requires(post): chkconfig
Requires(preun): chkconfig
# This is for /sbin/service
Requires(preun): initscripts
# This is for /sbin/service
Requires(postun): initscripts

%description
Spring Boot Starter Parent

%define __jar_repack %{nil}

%prep
%setup -q

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_sysconfdir}/%{name}
mkdir -p %{buildroot}/%{_initddir}
mkdir -p %{buildroot}/%{_datadir}/%{name}
mkdir -p %{buildroot}/%{_localstatedir}/log/%{name}
cp config/* %{buildroot}/%{_sysconfdir}/%{name} 
cp initd/* %{buildroot}/%{_initddir}/ 
cp *.jar %{buildroot}/%{_datadir}/%{name}/%{name}.jar

%clean
rm -rf %{buildroot}

%files
%defattr(-,%{name},%{name},-)
%{_datadir}/%{name}/*
%attr(755,root,root) %{_initddir}/*
%{_localstatedir}/log/*
%config(noreplace) %attr(600,%{name},%{name}) %{_sysconfdir}/%{name}/*

%pre
getent group %{name} > /dev/null || groupadd -r %{name}
getent passwd %{name} > /dev/null || useradd -r -g %{name} %{name} -s /sbin/nologin

%post
# This adds the proper /etc/rc*.d links for the script
/sbin/chkconfig --add %{name}

%preun
if [ $1 -eq 0 ] ; then
    /sbin/service %{name} stop >/dev/null 2>&1
    /sbin/chkconfig --del %{name}
fi

%postun
if [ "$1" -ge "1" ] ; then
    /sbin/service %{name} condrestart >/dev/null 2>&1 || :
fi


%changelog

