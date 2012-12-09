Name: xcursorgen
Version: 1.0.5
Release: %mkrel 1
Summary: Create an X cursor file from a collection of PNG images
Group: Development/X11
Source: http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License: MIT
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: libpng-devel >= 1.2.8
BuildRequires: libx11-devel >= 1.0.0
BuildRequires: libxcursor-devel >= 1.1.5.2
BuildRequires: x11-util-macros >= 1.0.1

%description
Xcursorgen creates an X cursor file from a collection of PNG images.

%prep
%setup -q -n %{name}-%{version}

%build
%configure2_5x --x-includes=%{_includedir}\
--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/xcursorgen
%{_mandir}/man1/xcursorgen.*


%changelog
* Tue Oct 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.4-3mdv2012.0
+ Revision: 702932
- attempt to relink against libpng15.so.15

* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.4-2
+ Revision: 671288
- mass rebuild

* Fri Sep 24 2010 Thierry Vignaud <tv@mandriva.org> 1.0.4-1mdv2011.0
+ Revision: 580825
- new release

* Wed Nov 11 2009 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.0.3-1mdv2010.1
+ Revision: 464699
- New version: 1.0.3

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 1.0.2-5mdv2009.1
+ Revision: 351213
- rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.0.2-4mdv2009.0
+ Revision: 226024
- rebuild

* Tue Feb 12 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.0.2-3mdv2008.1
+ Revision: 166460
- Revert to use upstream tarball, build requires and remove non mandatory local patches.

* Mon Jan 21 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.0.2-2mdv2008.1
+ Revision: 155926
- Updated BuildRequires and resubmit package.

+ Olivier Blin <blino@mandriva.org>
- restore BuildRoot

+ Thierry Vignaud <tv@mandriva.org>
- kill re-definition of %%buildroot on Pixel's request

* Tue Aug 21 2007 Thierry Vignaud <tv@mandriva.org> 1.0.2-1mdv2008.0
+ Revision: 68272
- new release
- do not hardcode man page extension
- fix description & summary


* Wed May 31 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-31 18:32:34 (31796)
- rebuild to fix cooker uploading

* Mon May 29 2006 Andreas Hasenack <andreas@mandriva.com>
+ 2006-05-29 14:36:37 (31646)
- renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

* Thu May 25 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-25 20:17:57 (31598)
- X11R7.1

