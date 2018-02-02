#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xF7D5C9BF765C61E3 (andreas@enge.fr)
#
Name     : mpc
Version  : 1.1.0
Release  : 21
URL      : https://ftp.gnu.org/gnu/mpc/mpc-1.1.0.tar.gz
Source0  : https://ftp.gnu.org/gnu/mpc/mpc-1.1.0.tar.gz
Source99 : https://ftp.gnu.org/gnu/mpc/mpc-1.1.0.tar.gz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-3.0 LGPL-3.0+
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
Provides: mpc-devel

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
%setup -q -n mpc-1.1.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1515687897
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1515687897
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/lib64/libmpc.so

%files doc
%defattr(-,root,root,-)
%doc /usr/share/info/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libmpc.so.3
/usr/lib64/libmpc.so.3.1.0
