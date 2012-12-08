Name: mandriva-galaxy
Summary: Mandriva-galaxy
Version: 2011.0
Release: %mkrel 4
Epoch: 2
License: GPL
URL: http://svn.mandriva.com/cgi-bin/viewvc.cgi/soft/mandriva-galaxy-kde4
Group: System/Configuration/Other
Source: %{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: kde4-macros
BuildRequires: kdelibs4-devel
BuildRequires: qt4-devel
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
%{_sysconfdir}/xdg/autostart/mandriva-galaxy.desktop
%{_iconsdir}/mandriva-galaxy.png
%{_datadir}/locale/*/LC_MESSAGES/mandriva-galaxy.mo


%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 2:2011.0-2mdv2011.0
+ Revision: 666382
- mass rebuild

* Tue Feb 15 2011 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 2:2011.0-1
+ Revision: 637882
- New version: 2011.0

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 2:2009.1-14mdv2010.1
+ Revision: 523266
- rebuilt for 2010.1

* Tue Sep 01 2009 Christophe Fergeau <cfergeau@mandriva.com> 2:2009.1-13mdv2010.0
+ Revision: 423705
- rebuild

  + Arthur Renato Mello <arthur@mandriva.com>
    -Update es and fi translation files
    - Update translation files
      Change release from 2009.0 to 2009.1

* Thu Apr 16 2009 Arthur Renato Mello <arthur@mandriva.com> 2:2009.0-10mdv2009.1
+ Revision: 367703
- Update tarball with the correct translation files
- Update package to add new translations files
- Use .po for translation instead of qt translation

  + Antoine Ginies <aginies@mandriva.com>
    - rebuild

* Fri Oct 03 2008 Arthur Renato Mello <arthur@mandriva.com> 2:2009.0-7mdv2009.0
+ Revision: 291019
- Fixing Bug 39252: Mandriva galaxy should not start at drak3d session

* Wed Oct 01 2008 Arthur Renato Mello <arthur@mandriva.com> 2:2009.0-6mdv2009.0
+ Revision: 290476
- Changing from QApplication to KApplication to use right colour scheme

* Sun Sep 28 2008 Funda Wang <fwang@mandriva.org> 2:2009.0-5mdv2009.0
+ Revision: 289043
- Renew tarball with translations
- use plain qt4 cmake

* Tue Sep 16 2008 Arthur Renato Mello <arthur@mandriva.com> 2:2009.0-4mdv2009.0
+ Revision: 285258
- Added a mandrivagalaxy.real symlink to not bread the .desktop created on 2008.1

* Mon Aug 18 2008 Arthur Renato Mello <arthur@mandriva.com> 2:2009.0-3mdv2009.0
+ Revision: 273222
- Fix bug 42908. xinit script was testing if parameter was KDE but for KDE 4 that is KDE4. This made mandriva-galaxy starts duplicate

* Fri Aug 15 2008 Arthur Renato Mello <arthur@mandriva.com> 2:2009.0-2mdv2009.0
+ Revision: 272443
- Add fr translation

* Fri Aug 15 2008 Arthur Renato Mello <arthur@mandriva.com> 2:2009.0-1mdv2009.0
+ Revision: 272395
- Add missing BuildRequire for qt4-linguist
- New version based on Qt4

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Wed Apr 02 2008 Anne Nicolas <ennael@mandriva.org> 2:2008.1-3mdv2008.1
+ Revision: 191985
- new release
- new tarball (Fix #39702)

* Mon Mar 31 2008 Anne Nicolas <ennael@mandriva.org> 2:2008.1-2mdv2008.1
+ Revision: 191293
- update spec file
- update tarball for Spring release

* Thu Feb 28 2008 Anne Nicolas <ennael@mandriva.org> 2:2008.1-1mdv2008.1
+ Revision: 176050
- fix makefile and css
- new tarball for Spring
- new images for Spring release

* Thu Jan 03 2008 Oden Eriksson <oeriksson@mandriva.com> 2:2008.0-3mdv2008.1
+ Revision: 141783
- rebuilt against openldap-2.4.7 libs

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - buildrequires X11-devel instead of XFree86-devel

* Wed Oct 03 2007 Anne Nicolas <ennael@mandriva.org> 2:2008.0-2mdv2008.0
+ Revision: 95226
- reimport tarball
- delete corrupted tarball
- new tarball for 2008
- fix files section
- new release
- fix permission

* Mon Oct 01 2007 Gustavo Pichorim Boiko <boiko@mandriva.com> 2:2008.0-1mdv2008.0
+ Revision: 94348
- Move the hand installed files to the package so that they are handle by
  automake
- Rebuild for 2008.0


* Wed Apr 04 2007 Laurent Montel <lmontel@mandriva.com> 2007.1-12mdv2007.1
+ Revision: 150530
- Update page

* Fri Mar 23 2007 Laurent Montel <lmontel@mandriva.com> 2:2007.1-11mdv2007.1
+ Revision: 148338
- Update indexhtml-*.html

* Tue Mar 20 2007 Laurent Montel <lmontel@mandriva.com> 2:2007.1-10mdv2007.1
+ Revision: 147023
- Fix windows size

* Mon Mar 19 2007 Laurent Montel <lmontel@mandriva.com> 2:2007.1-8mdv2007.1
+ Revision: 146520
- Add index-*.html

* Thu Mar 15 2007 Laurent Montel <lmontel@mandriva.com> 2:2007.1-7mdv2007.1
+ Revision: 144172
- Fix font

* Thu Mar 15 2007 Frederic Crozat <fcrozat@mandriva.com> 2:2007.1-6mdv2007.1
+ Revision: 144072
- Add autostart .desktop for GNOME too

* Wed Mar 14 2007 Laurent Montel <lmontel@mandriva.com> 2:2007.1-5mdv2007.1
+ Revision: 143360
- Fix compile under x86_64
- Fix build
- Fix size
- Update index.html
- Import mandriva-galaxy

* Thu Sep 21 2006 Laurent MONTEL <lmontel@mandriva.com> 2007-3
- Remove menu entry

* Tue Sep 19 2006 Pablo Saratxaga <pablo@mandriva.com> 2007-2
- updated translations
- new html file

* Tue May 30 2006 Laurent MONTEL <lmontel@mandriva.com> 2007-1
- Use %%mkrel
- Hide desktop file into new xdg menu

* Tue Feb 28 2006 Laurent MONTEL <lmontel@mandriva.com> 2006-15mdk
- Fix provides/requires

* Sat Oct 01 2005 Laurent MONTEL <lmontel@mandriva.com> 2006-14mdk
- Fix javascript script

* Sat Oct 01 2005 Laurent MONTEL <lmontel@mandriva.com> 2006-13mdk
- Fix accessibility page

* Wed Sep 21 2005 Laurent MONTEL <lmontel@mandriva.com> 2006-12mdk
- Fix icons link

* Thu Sep 15 2005 Frederic Lepied <flepied@mandriva.com> 2006-11mdk
- updated translations

* Tue Sep 13 2005 Frederic Lepied <flepied@mandriva.com> 2006-10mdk
- fixed the inverted test

* Tue Sep 13 2005 Laurent MONTEL <lmontel@mandriva.com> 2006-9mdk
- Oops cvs up => update css

* Tue Sep 13 2005 Laurent MONTEL <lmontel@mandriva.com> 2006-8mdk
- Fix upgrade

* Tue Sep 13 2005 Laurent MONTEL <lmontel@mandriva.com> 2006-7mdk
- Fix size

* Sat Sep 10 2005 Laurent MONTEL <lmontel@mandriva.com> 2006-6mdk
- Update po

* Wed Sep 07 2005 Frederic Lepied <flepied@mandriva.com> 2006-5mdk
- fix startup
- mandriva

* Tue Sep 06 2005 Laurent MONTEL <lmontel@mandriva.com> 2006-4mdk
- Change binary name

* Tue Sep 06 2005 Frederic Lepied <flepied@mandriva.com> 2006-3mdk
- rebuild

* Wed Aug 24 2005 Laurent MONTEL <lmontel@mandriva.com> 2006-2mdk
- Enable javascript

* Thu Aug 04 2005 Laurent MONTEL <lmontel@mandriva.com> 2006-1mdk
- Rename

* Mon Mar 14 2005 Laurent MONTEL <lmontel@mandriva.com> 10.1-8mdk
- Update po file

* Fri Sep 10 2004 David Baudens <baudens@mandriva.com> 10.1-7mdk
- Add missing images (please think to also modify spec when you modify
  something in cvs)

* Fri Aug 27 2004 David Baudens <baudens@mandriva.com> 10.1-6mdk
- Update po files

* Wed Aug 18 2004 Laurent MONTEL <lmontel@mandriva.com> 10.1-5mdk
- Update po file

* Thu Aug 12 2004 Laurent MONTEL <lmontel@mandriva.com> 10.1-4mdk
- Update po file

* Sat Jul 31 2004 Laurent MONTEL <lmontel@mandriva.com> 10.1-3mdk
- Remove requires on xinitrc

* Wed Jul 28 2004 Laurent MONTEL <lmontel@mandriva.com> 10.1-2mdk
- Fix  permission of "mandrivagalaxy" now it launch into each WM

* Tue Jul 27 2004 Laurent MONTEL <lmontel@mandriva.com> 10.1-1mdk
- Update po file

* Tue Jun 29 2004 Laurent MONTEL <lmontel@mandriva.com> 10.0-20mdk
- Fix requires

* Tue Jun 15 2004 Laurent MONTEL <lmontel@mandriva.com> 10.0-19mdk
- Fix use automake/autoconf

* Sat Jun 05 2004 <lmontel@n2.mandriva.com> 10.0-18mdk
- Rebuild

* Sat May 22 2004 Laurent MONTEL <lmontel@mandriva.com> 10.0-17mdk
- Add missing buildrequires

* Tue Apr 20 2004 Laurent MONTEL <lmontel@mandriva.com> 10.0-16mdk
- Fix mandrakeexpert url in mdkgalaxy-fr

