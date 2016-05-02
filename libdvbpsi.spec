Name:       libdvbpsi
Version:    1.3.0
Release:    2%{?dist}
Summary:    Library for MPEG TS and DVB PSI tables decoding and generation
License:    LGPLv2+
URL:        http://www.videolan.org/developers/%{name}.html

Source0:    http://download.videolan.org/pub/%{name}/%{version}/%{name}-%{version}.tar.bz2

BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  doxygen
BuildRequires:  graphviz
BuildRequires:  libtool

%description
%{name} is a simple library designed for decoding and generation of MPEG TS and
DVB PSI tables according to standards ISO/IEC 13818 and ITU-T H.222.0.

%package devel
Summary:    Development package for %{name}
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description devel
%{name} is a simple library designed for decoding and generation of MPEG TS and
DVB PSI tables according to standards ISO/IEC 13818 and ITU-T H.222.0.

This package contains development files for %{name}

%prep
%setup -q -n %{name}-%{version}
autoreconf -vif

%build
%configure --disable-dependency-tracking --disable-static
make %{?_smp_mflags}
make doc

%install
make install DESTDIR=%{buildroot} INSTALL="install -p"
rm -f %{buildroot}%{_libdir}/lib*.la

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%{!?_licensedir:%global license %%doc}
%license COPYING
%doc AUTHORS ChangeLog README
%{_libdir}/%{name}.so.*

%files devel
%doc doc/doxygen/html
%{_includedir}/dvbpsi/
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Mon May 02 2016 Simone Caronni <negativo17@gmail.com> - 1.3.0-2
- SPEC file cleanup.

* Sat Oct 24 2015 Nicolas Chauvet <kwizart@gmail.com> - 1.3.0-1
- Update to 1.3.0
