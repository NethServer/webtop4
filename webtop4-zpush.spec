%define zpush_major_version 2.2.10
%define zpush_minor_version 0018

Summary: WebTop z-push
Name: webtop4-zpush
Version: 1.2.1
Release: 1%{?dist}
License: GPL
URL: %{url_prefix}/%{name} 
Source0: http://git.nethesis.it/install/webtop/z-push-%{zpush_major_version}%23%23%{zpush_minor_version}.tar.gz
BuildArch: noarch

Requires: webtop4-core

BuildRequires: unzip

%description
NethServer z-push

%prep
#%setup

%build
mkdir -p root/var/log/z-push
mkdir -p root/var/lib/nethserver/z-push/state
mkdir -p root/usr/share/webtop/z-push/
tar xvzf %{SOURCE0} -C root/usr/share/webtop/z-push

%install
rm -rf %{buildroot}
(cd root; find . -depth -print | cpio -dump %{buildroot})

%post

%preun

%files
%defattr(-,root,root)
%attr(755, apache, apache) /var/log/z-push
%attr(755, apache, apache) /var/lib/nethserver/z-push
%attr(755, root, root) /usr/share/webtop/z-push/z-push-admin.php
/usr/share/webtop/z-push/*

%changelog
* Thu Jan 19 2017 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.2.1-1
- Update z-push 2.2.10-0018. Refs #3436

* Fri May 20 2016 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.2.0-1
- First release. Refs #3372

