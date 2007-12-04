%define __libtoolize    /bin/true

Summary:	Mandriva-galaxy
Name:		mandriva-galaxy	
Version:	2008.0
Release:	%mkrel 2
Epoch:		2
License:	GPL
URL:		http://www.mandriva.com/
Group:		System/Configuration/Other

# get the source from our cvs repository (see
# http://www.mandrakelinux.com/en/cvs.php3)
# no extra source or patch are allowed here.
Source:			%name-%version.tar.bz2

BuildRoot:		%_tmppath/%name-%release-root
BuildRequires:	X11-devel
BuildRequires:	arts-devel
BuildRequires:	fam-devel
BuildRequires:	kdelibs-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	qt3-devel
BuildRequires:	zlib-devel
BuildRequires:	intltool

BuildRequires:  autoconf2.5, automake >= 1.7

Group:		Graphical desktop/KDE
Requires:	kdelibs
Obsoletes:	mandrake-galaxy
Provides:	mandrake-galaxy
Obsoletes:  mandrivagalaxy
Provides:   mandrivagalaxy
Obsoletes:  mandrakegalaxy
Provides:  	mandrakegalaxy

%description
This package displays an html file allowing users to launch browsers to
other html pages (Mandriva Web sites or local html documentation) or to
launch Mandriva applications such as the Mandriva Control Center.

%prep

%setup -q

%build
%configure2_5x --enable-final \
		--disable-debug \
		--with-xinerama \
		--disable-rpath

%make

%install
rm -rf %buildroot

%makeinstall_std
# legacy links
(
	cd %buildroot/%_bindir/
	ln -s mandrivagalaxy.real mandrakegalaxy.real
)

(
	cd %buildroot/%_iconsdir/
	ln -s mandrivagalaxy.png mandrakegalaxy.png
)

%find_lang mandrivagalaxy

%clean
rm -fr %buildroot

%files -f mandrivagalaxy.lang
%defattr(-,root,root)
#
%attr(755,root,root) %_bindir/*

%_datadir/autostart/*.desktop
%_datadir/gnome/autostart/*.desktop
%dir %_datadir/mdk/
%dir %_datadir/mdk/mandrivagalaxy/
%_datadir/mdk/mandrivagalaxy/*.html
%_datadir/mdk/mandrivagalaxy/*.png
%attr(755,root,root) %config(noreplace) %{_sysconfdir}/X11/xinit.d/mandriva-galaxy
%_iconsdir/*.png

%_datadir/nautilus/default-desktop/*.desktop
%_datadir/apps/kdesktop/DesktopLinks/*.desktop

%dir %_datadir/mdk/mandrivagalaxy/style/images/
%_datadir/mdk/mandrivagalaxy/style/images/*.png
%_datadir/mdk/mandrivagalaxy/style/*.css
#%_datadir/mdk/mandrivagalaxy/*.js



