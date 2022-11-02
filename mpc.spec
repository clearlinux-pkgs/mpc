#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xF7D5C9BF765C61E3 (andreas@enge.fr)
#
Name     : mpc
Version  : 1.2.1
Release  : 41
URL      : https://mirrors.kernel.org/gnu/mpc/mpc-1.2.1.tar.gz
Source0  : https://mirrors.kernel.org/gnu/mpc/mpc-1.2.1.tar.gz
Source1  : https://mirrors.kernel.org/gnu/mpc/mpc-1.2.1.tar.gz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-3.0 LGPL-3.0+
Requires: mpc-info = %{version}-%{release}
Requires: mpc-lib = %{version}-%{release}
Requires: mpc-license = %{version}-%{release}
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
Requires: mpc-lib = %{version}-%{release}
Provides: mpc-devel = %{version}-%{release}
Requires: mpc = %{version}-%{release}

%description dev
dev components for the mpc package.


%package info
Summary: info components for the mpc package.
Group: Default

%description info
info components for the mpc package.


%package lib
Summary: lib components for the mpc package.
Group: Libraries
Requires: mpc-license = %{version}-%{release}

%description lib
lib components for the mpc package.


%package license
Summary: license components for the mpc package.
Group: Default

%description license
license components for the mpc package.


%prep
%setup -q -n mpc-1.2.1
cd %{_builddir}/mpc-1.2.1
pushd ..
cp -a mpc-1.2.1 buildavx2
popd
pushd ..
cp -a mpc-1.2.1 buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1667432965
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition "
%configure --disable-static
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3"
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3"
%configure --disable-static
make  %{?_smp_mflags}
popd
unset PKG_CONFIG_PATH
pushd ../buildavx512/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v4 -mprefer-vector-width=512 -Wl,-z,x86-64-v4 -mtune=sapphirerapids "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v4 -mprefer-vector-width=512 -Wl,-z,x86-64-v4 -mtune=sapphirerapids "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v4 -mprefer-vector-width=512"
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v4 -mprefer-vector-width=512"
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v4"
%configure --disable-static
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make bench
pushd ../buildavx2/
make bench
popd
pushd ../buildavx512/
make bench
popd

%install
export SOURCE_DATE_EPOCH=1667432965
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/mpc
cp %{_builddir}/mpc-%{version}/COPYING.LESSER %{buildroot}/usr/share/package-licenses/mpc/f45ee1c765646813b442ca58de72e20a64a7ddba || :
pushd ../buildavx2/
%make_install_v3
popd
pushd ../buildavx512/
%make_install_v4
popd
%make_install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/mpc.h
/usr/lib64/glibc-hwcaps/x86-64-v3/libmpc.so
/usr/lib64/glibc-hwcaps/x86-64-v4/libmpc.so
/usr/lib64/libmpc.so

%files info
%defattr(0644,root,root,0755)
/usr/share/info/mpc.info

%files lib
%defattr(-,root,root,-)
/usr/lib64/glibc-hwcaps/x86-64-v3/libmpc.so.3
/usr/lib64/glibc-hwcaps/x86-64-v3/libmpc.so.3.2.1
/usr/lib64/glibc-hwcaps/x86-64-v4/libmpc.so.3
/usr/lib64/glibc-hwcaps/x86-64-v4/libmpc.so.3.2.1
/usr/lib64/libmpc.so.3
/usr/lib64/libmpc.so.3.2.1

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mpc/f45ee1c765646813b442ca58de72e20a64a7ddba
