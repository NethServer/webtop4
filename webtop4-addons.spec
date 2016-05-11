%define webtop_version 0405

Summary: Webtop4 addons
Name: webtop4-addons
Version: 1.1.3
Release: 1%{?dist}
License: GPL
URL: %{url_prefix}/%{name} 
Source0: http://git.nethesis.it/install/webtop/webtop%23%23%{webtop_version}.war
BuildArch: noarch

BuildRequires: unzip

%description
NethServer WebTop 4 addons

%prep

%build
mkdir -p root/var/lib/tomcat/webapps/webtop
unzip %{SOURCE0} \
  WEB-INF/lib/sonicle-webtop-addons.jar \
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
