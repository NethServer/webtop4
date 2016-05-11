%define webtop_version 0405

Summary: Webtop4 core
Name: webtop4-core
Version: 1.1.3
Release: 1%{?dist}
License: GPL
URL: %{url_prefix}/%{name} 
Source0: %{name}-%{version}.tar.gz
Source1: http://git.nethesis.it/install/webtop/webtop%23%23%{webtop_version}.war
BuildArch: noarch
Requires: webtop4-libs

BuildRequires: unzip

%description
NethServer WebTop 4 core libraries

%prep
%setup

%build
mkdir -p root/var/lib/tomcat/webapps/webtop
unzip %{SOURCE1} \
  WEB-INF/lib/sonicle-commons-web.jar \
  WEB-INF/lib/sonicle-commons.jar \
  WEB-INF/lib/sonicle-mail.jar \
  WEB-INF/lib/sonicle-security.jar \
  WEB-INF/lib/sonicle-webtop-ext.jar \
  WEB-INF/lib/sonicle-webtop-groupware.jar \
  WEB-INF/lib/sonicle-webtop-services.jar \
  WEB-INF/lib/sonicle-webtop-themes.jar \
  WEB-INF/lib/sonicle-webtop-webtopadmin.jar \
  META-INF/MANIFEST.MF \
  META-INF/context.xml \
  WEB-INF/classes/logback.xml \
  WEB-INF/shiro.ini \
  WEB-INF/web.xml \
  -d root/var/lib/tomcat/webapps/webtop
mkdir -p root/usr/share/webtop/doc/
echo %{webtop_version} > root/usr/share/webtop/doc/VERSION

%install
rm -rf %{buildroot}
(cd root; find . -depth -print | cpio -dump %{buildroot})

%post

%preun

%files
%defattr(-,root,root)
/var/lib/tomcat/webapps/webtop/*
%doc /usr/share/webtop/doc/VERSION
%doc COPYING

%changelog
