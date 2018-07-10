Name:		xcursorgen
Version:	1.0.6
Release:	8
Summary:	Create an X cursor file from a collection of PNG images
Group:		Development/X11
Source:		http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License:	MIT

BuildRequires:	pkgconfig(libpng) >= 1.2.8
BuildRequires:	pkgconfig(x11) >= 1.0.0
BuildRequires:	pkgconfig(xcursor) >= 1.1.5.2
BuildRequires:	x11-util-macros >= 1.0.1

%description
Xcursorgen creates an X cursor file from a collection of PNG images.

%prep
%setup -q -n %{name}-%{version}

%build
%configure \
	--x-includes=%{_includedir} \
    --x-libraries=%{_libdir}

%make

%install
%makeinstall_std

%files
%defattr(-,root,root)
%{_bindir}/xcursorgen
%{_mandir}/man1/xcursorgen.*
