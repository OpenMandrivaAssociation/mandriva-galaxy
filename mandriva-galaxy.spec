%define __libtoolize    /bin/true

Summary:	Mandriva-galaxy
Name:		mandriva-galaxy	
Version:	2007.1
Release:	%mkrel 12
Epoch:		2
License:	GPL
URL:		http://www.mandriva.com/
Group:		System/Configuration/Other

# get the source from our cvs repository (see
# http://www.mandrakelinux.com/en/cvs.php3)
# no extra source or patch are allowed here.
Source:			%name-%version.tar.bz2

BuildRoot:		%_tmppath/%name-%release-root
BuildRequires:	XFree86-devel
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
make -f admin/Makefile.common


	%configure --enable-final \
		--disable-debug \
%if "%{_lib}" != "lib"
   --enable-libsuffix="%(A=%{_lib}; echo ${A/lib/})" \
%endif
		--with-xinerama \
		--disable-rpath

%make

%install
rm -rf %buildroot

%makeinstall_std
# Bad hack - Tired
chmod 0755 %buildroot/%_bindir/*

install -d -m 0755 %buildroot/%_datadir/gnome/autostart
cp -f %buildroot/%_datadir/autostart/*.desktop %buildroot/%_datadir/gnome/autostart


install -d -m 0755 %buildroot/%_iconsdir/
install -m 0644 $RPM_BUILD_DIR/%name-%version/mdkhtmlbrowser/mandrivagalaxy.png %buildroot/%_iconsdir/

install -d -m 0755 %buildroot/%_datadir/nautilus/default-desktop/
install -m 0644 $RPM_BUILD_DIR/%name-%version/mdkhtmlbrowser/Welcome.desktop %buildroot/%_datadir/nautilus/default-desktop/

install -d -m 0755 %buildroot/%_datadir/apps/kdesktop/DesktopLinks/
install -m 0644 $RPM_BUILD_DIR/%name-%version/mdkhtmlbrowser/Welcome.desktop %buildroot/%_datadir/apps/kdesktop/DesktopLinks/

install -d -m 0755 %buildroot/%_datadir/mdk/mandrivagalaxy/
install -m 0644 $RPM_BUILD_DIR/%name-%version/mdkhtmlbrowser/*.png %buildroot/%_datadir/mdk/mandrivagalaxy/


(
	cd %buildroot/%_bindir/
	ln -s mandrivagalaxy.real mandrakegalaxy.real
)

(
	cd %buildroot/%_iconsdir/
	ln -s mandrivagalaxy.png mandrakegalaxy.png
)

rm -f %buildroot/%_datadir/applnk/Applications/*.desktop

%find_lang mandrivagalaxy

%clean
rm -fr %buildroot

%files -f mandrivagalaxy.lang
%defattr(-,root,root)
#
%_bindir/*

%_datadir/autostart/*.desktop
%_datadir/gnome/autostart/*.desktop
#
#%_datadir/applnk/Applications/*.desktop
%dir %_datadir/mdk/
%dir %_datadir/mdk/mandrivagalaxy/
%_datadir/mdk/mandrivagalaxy/*.html
%_datadir/mdk/mandrivagalaxy/*.png
%attr(755,root,root) %config(noreplace) %{_sysconfdir}/X11/xinit.d/mandriva-galaxy
#
%_iconsdir/*.png
#%_iconsdir/large/*.png

%_datadir/nautilus/default-desktop/*.desktop
%_datadir/apps/kdesktop/DesktopLinks/*.desktop

%dir %_datadir/mdk/mandrivagalaxy/images/
%_datadir/mdk/mandrivagalaxy/style/images/*.png
%_datadir/mdk/mandrivagalaxy/style/images/*.jpeg
%_datadir/mdk/mandrivagalaxy/style/*.css
#%_datadir/mdk/mandrivagalaxy/*.js



