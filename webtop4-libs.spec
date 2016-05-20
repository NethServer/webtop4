%define webtop_version 0405

Summary: Webtop4 libs
Name: webtop4-libs
Version: 1.2.0
Release: 1%{?dist}
License: GPL
URL: %{url_prefix}/%{name} 
Source0: %{name}-%{version}.tar.gz
Source1: http://git.nethesis.it/install/webtop/webtop%23%23%{webtop_version}.war
BuildArch: noarch

BuildRequires: unzip

%description
NethServer WebTop 4 libraries

%prep
%setup

%build
mkdir -p root/var/lib/tomcat/webapps/webtop
unzip %{SOURCE1}  \
  *jar -x *sonicle*.jar \
  -d root/var/lib/tomcat/webapps/webtop

%install
rm -rf %{buildroot}
(cd root; find . -depth -print | cpio -dump %{buildroot})

%post

%preun

%files
%defattr(-,root,root)
/var/lib/tomcat/webapps/webtop/*

%changelog
* Fri May 20 2016 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.2.0-1
- First release. Refs #3372

