Name: xcursorgen
Version: 1.0.1
Release: %mkrel 2
Summary: create an X cursor file from a collection of PNG images
Group: Development/X11
Source: http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License: MIT
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: libpng-devel >= 1.2.8
BuildRequires: libx11-devel >= 1.0.0
BuildRequires: libxcursor-devel >= 1.1.5.2
BuildRequires: x11-util-macros >= 1.0.1

%description
CHECK

%prep
%setup -q -n %{name}-%{version}

%build
%configure2_5x	--x-includes=%{_includedir}\
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
%{_mandir}/man1/xcursorgen.1x.bz2


