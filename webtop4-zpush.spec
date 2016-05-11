%define zpush_major_version 2.2.8
%define zpush_minor_version 0017

Summary: WebTop z-push
Name: webtop4-zpush
Version: 1.1.3
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
#%dir /var/lib/nethserver/z-push/state/
/usr/share/webtop/z-push/*

%changelog
