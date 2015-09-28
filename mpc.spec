#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mpc
Version  : 1.0.3
Release  : 13
URL      : ftp://ftp.gnu.org/gnu/mpc/mpc-1.0.3.tar.gz
Source0  : ftp://ftp.gnu.org/gnu/mpc/mpc-1.0.3.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-3.0+ LGPL-3.0 GPL-3.0 GFDL-1.3
Requires: mpc-lib
Requires: mpc-doc
BuildRequires : gmp-dev
BuildRequires : mpfr-dev
BuildRequires : sed

%description
without any warranty.
GNU MPC is a complex floating-point library with exact rounding.
It is based on the GNU MPFR floating-point library (http://www.mpfr.org/),
which is itself based on the GNU MP library (http://gmplib.org/).

%package dev
Summary: dev components for the mpc package.
Group: Development
Requires: mpc-lib

%description dev
dev components for the mpc package.


%package doc
Summary: doc components for the mpc package.
Group: Documentation

%description doc
doc components for the mpc package.


%package lib
Summary: lib components for the mpc package.
Group: Libraries

%description lib
lib components for the mpc package.


%prep
%setup -q -n mpc-1.0.3

%build
%configure --disable-static
make V=1 %{?_smp_mflags}

%check
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/lib64/*.so

%files doc
%defattr(-,root,root,-)
%doc /usr/share/info/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*
