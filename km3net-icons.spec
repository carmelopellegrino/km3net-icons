# $Id$
Name:           km3net-icons
Version:        1.0
Release:        1
Summary:        Icons for KM3NeT
Group:          KM3NeT
License:        INFN
URL:            https://github.com/carmelopellegrino/km3net-icons
Source0:        https://github.com/carmelopellegrino/km3net-icons
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
Requires:
%description
Simple icon set for KM3NeT

%define debug_package %{nil}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/share/icons/km3net/
cp index.theme $RPM_BUILD_ROOT/usr/share/icons/km3net/
cp -r 8x8   $RPM_BUILD_ROOT/usr/share/icons/km3net/
cp -r 16x16 $RPM_BUILD_ROOT/usr/share/icons/km3net/
cp -r 22x22 $RPM_BUILD_ROOT/usr/share/icons/km3net/
cp -r 24x24 $RPM_BUILD_ROOT/usr/share/icons/km3net/
cp -r 32x32 $RPM_BUILD_ROOT/usr/share/icons/km3net/
cp -r 48x48 $RPM_BUILD_ROOT/usr/share/icons/km3net/

%post
/usr/bin/update-desktop-database &> /dev/null || :

%postun
/usr/bin/update-desktop-database &> /dev/null || :

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
/usr/share/icons/km3net/*

%changelog
* Thu Nov 19 2015 Carmelo Pellegrino <cpellegrino@km3net.de> 1.0
- First RPM release
