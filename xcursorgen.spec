Name: xcursorgen
Version: 1.0.2
Release: %mkrel 2
Summary: Create an X cursor file from a collection of PNG images
Group: Development/X11
Source: http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License: MIT
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: x11-util-macros	>= 1.1.5
BuildRequires: libx11-devel	>= 1.1.3
BuildRequires: libxcursor-devel	>= 1.1.9
BuildRequires: libpng-devel	>= 1.2.22

%description
Xcursorgen creates an X cursor file from a collection of PNG images.

%prep
%setup -q -n %{name}-%{version}

%build
%configure	--x-includes=%{_includedir}\
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
