Name:		xcursorgen
Version:	1.0.8
Release:	2
Summary:	Create an X cursor file from a collection of PNG images
Group:		Development/X11
Source:		http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.xz
License:	MIT

BuildRequires:	pkgconfig(libpng) >= 1.2.8
BuildRequires:	pkgconfig(x11) >= 1.0.0
BuildRequires:	pkgconfig(xcursor) >= 1.1.5.2
BuildRequires:	pkgconfig(xorg-macros)

%description
Xcursorgen creates an X cursor file from a collection of PNG images.

%prep
%autosetup -n %{name}-%{version} -p1

%build
%configure \
    --x-includes=%{_includedir} \
    --x-libraries=%{_libdir}

%make_build

%install
%make_install

%files
%{_bindir}/xcursorgen
%doc %{_mandir}/man1/xcursorgen.*
