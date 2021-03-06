%define webtop_version 0459

Summary: Webtop4 core
Name: webtop4-core
Version: 1.2.4
Release: 1%{?dist}
License: GPL
URL: %{url_prefix}/%{name} 
Source0: %{name}-%{version}.tar.gz
Source1: https://www.sonicle.com/nethesis/nethtop/webtop%23%23%{webtop_version}.war
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
* Wed Mar 06 2019 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.2.4-1
- Fix SQL injection on wtusername login variable

* Mon Jan 30 2017 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.2.3-1
- Update webtop-core to version 0458. NethServer/dev#5180

* Wed Jan 25 2017 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.2.2-1
- Update webtop-core to version 0457. NethServer/dev#5180

* Thu Jan 19 2017 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.2.1-1
- Update webtop-core to version 0456. Refs #3436

* Fri May 20 2016 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.2.0-1
- First release. Refs #3372

