#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
# autospec version: v4
# autospec commit: da8b975
#
# Source0 file verified with key 0x528897B826403ADA
#
Name     : libksba
Version  : 1.6.6
Release  : 25
URL      : https://gnupg.org/ftp/gcrypt/libksba/libksba-1.6.6.tar.bz2
Source0  : https://gnupg.org/ftp/gcrypt/libksba/libksba-1.6.6.tar.bz2
Source1  : https://gnupg.org/ftp/gcrypt/libksba/libksba-1.6.6.tar.bz2.sig
Summary  : X.509 and CMS support library
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0 LGPL-3.0
Requires: libksba-bin = %{version}-%{release}
Requires: libksba-info = %{version}-%{release}
Requires: libksba-lib = %{version}-%{release}
Requires: libksba-license = %{version}-%{release}
BuildRequires : bison
BuildRequires : buildreq-configure
BuildRequires : libgpg-error-dev
BuildRequires : libgpg-error-extras
BuildRequires : valgrind
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
LIBKSBA
---------
This file is free software; as a special exception the author gives
unlimited permission to copy and/or distribute it, with or without
modifications, as long as this notice is preserved.

%package bin
Summary: bin components for the libksba package.
Group: Binaries
Requires: libksba-license = %{version}-%{release}

%description bin
bin components for the libksba package.


%package dev
Summary: dev components for the libksba package.
Group: Development
Requires: libksba-lib = %{version}-%{release}
Requires: libksba-bin = %{version}-%{release}
Provides: libksba-devel = %{version}-%{release}
Requires: libksba = %{version}-%{release}

%description dev
dev components for the libksba package.


%package info
Summary: info components for the libksba package.
Group: Default

%description info
info components for the libksba package.


%package lib
Summary: lib components for the libksba package.
Group: Libraries
Requires: libksba-license = %{version}-%{release}

%description lib
lib components for the libksba package.


%package license
Summary: license components for the libksba package.
Group: Default

%description license
license components for the libksba package.


%prep
%setup -q -n libksba-1.6.6
cd %{_builddir}/libksba-1.6.6
pushd ..
cp -a libksba-1.6.6 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1708702185
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%configure --disable-static
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
%configure --disable-static
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check
cd ../buildavx2;
make %{?_smp_mflags} check || :

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1708702185
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libksba
cp %{_builddir}/libksba-%{version}/COPYING.GPLv2 %{buildroot}/usr/share/package-licenses/libksba/4cc77b90af91e615a64ae04893fdffa7939db84c || :
cp %{_builddir}/libksba-%{version}/COPYING.GPLv3 %{buildroot}/usr/share/package-licenses/libksba/e31db874e5b375f0592b02e3e450c9e94086e661 || :
cp %{_builddir}/libksba-%{version}/COPYING.LGPLv3 %{buildroot}/usr/share/package-licenses/libksba/f45ee1c765646813b442ca58de72e20a64a7ddba || :
export GOAMD64=v2
GOAMD64=v3
pushd ../buildavx2/
%make_install_v3
popd
GOAMD64=v2
%make_install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/ksba-config

%files dev
%defattr(-,root,root,-)
/usr/include/ksba.h
/usr/lib64/libksba.so
/usr/lib64/pkgconfig/ksba.pc
/usr/share/aclocal/*.m4

%files info
%defattr(0644,root,root,0755)
/usr/share/info/ksba.info

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libksba.so.8.14.6
/usr/lib64/libksba.so.8
/usr/lib64/libksba.so.8.14.6

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libksba/4cc77b90af91e615a64ae04893fdffa7939db84c
/usr/share/package-licenses/libksba/e31db874e5b375f0592b02e3e450c9e94086e661
/usr/share/package-licenses/libksba/f45ee1c765646813b442ca58de72e20a64a7ddba
