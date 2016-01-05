#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libksba
Version  : 1.3.3
Release  : 5
URL      : ftp://ftp.gnupg.org/gcrypt/libksba/libksba-1.3.3.tar.bz2
Source0  : ftp://ftp.gnupg.org/gcrypt/libksba/libksba-1.3.3.tar.bz2
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0 LGPL-3.0
Requires: libksba-bin
Requires: libksba-lib
Requires: libksba-doc
BuildRequires : bison
BuildRequires : libgpg-error-dev
BuildRequires : valgrind

%description
LIBKSBA
---------
2012, 2013, 2014, 2015  g10 Code GmbH
This file is free software; as a special exception the author gives
unlimited permission to copy and/or distribute it, with or without
modifications, as long as this notice is preserved.

%package bin
Summary: bin components for the libksba package.
Group: Binaries

%description bin
bin components for the libksba package.


%package dev
Summary: dev components for the libksba package.
Group: Development
Requires: libksba-lib
Requires: libksba-bin
Provides: libksba-devel

%description dev
dev components for the libksba package.


%package doc
Summary: doc components for the libksba package.
Group: Documentation

%description doc
doc components for the libksba package.


%package lib
Summary: lib components for the libksba package.
Group: Libraries

%description lib
lib components for the libksba package.


%prep
%setup -q -n libksba-1.3.3

%build
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/ksba-config

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/lib64/*.so
/usr/share/aclocal/*.m4

%files doc
%defattr(-,root,root,-)
%doc /usr/share/info/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*
