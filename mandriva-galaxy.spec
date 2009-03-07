Name: mandriva-galaxy	
Summary: Mandriva-galaxy
Version: 2009.0
Release: %mkrel 8
Epoch: 2
License: GPL
URL: http://svn.mandriva.com/cgi-bin/viewvc.cgi/soft/mandriva-galaxy-kde4
Group: System/Configuration/Other
Source: %{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: kde4-macros
BuildRequires: kdelibs4-devel
BuildRequires: qt4-devel
BuildRequires: qt4-linguist
BuildRequires: cmake

Requires: mandriva-galaxy-data

%description
This package displays an html file allowing users to launch browsers to
other html pages (Mandriva Web sites or local html documentation) or to
launch Mandriva applications such as the Mandriva Control Center.

%prep 
%setup -q -n mandriva-galaxy

%build 
%cmake_qt4
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std -C build
ln -s %{_bindir}/mandriva-galaxy %{buildroot}/%{_bindir}/mandrivagalaxy.real

%clean 
rm -rf $RPM_BUILD_ROOT 

%files
%defattr(-,root,root)
%attr(755,root,root) %{_bindir}/mandriva-galaxy
%attr(755,root,root) %{_bindir}/mandrivagalaxy.real
%attr(755,root,root) %config(noreplace) %{_sysconfdir}/X11/xinit.d/mandriva-galaxy.xinit
%{_datadir}/autostart/mandriva-galaxy.desktop
%{_datadir}/gnome/autostart/mandriva-galaxy.desktop
%dir %{_datadir}/mandriva-galaxy
%{_datadir}/mandriva-galaxy/*
%{_iconsdir}/mandriva-galaxy.png
