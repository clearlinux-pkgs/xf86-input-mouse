#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x0FDD682D974CA72A (mattst88@gmail.com)
#
Name     : xf86-input-mouse
Version  : 1.9.3
Release  : 30
URL      : http://xorg.freedesktop.org/releases/individual/driver/xf86-input-mouse-1.9.3.tar.gz
Source0  : http://xorg.freedesktop.org/releases/individual/driver/xf86-input-mouse-1.9.3.tar.gz
Source99 : http://xorg.freedesktop.org/releases/individual/driver/xf86-input-mouse-1.9.3.tar.gz.sig
Summary  : X.org mouse input driver
Group    : Development/Tools
License  : HPND
Requires: xf86-input-mouse-lib = %{version}-%{release}
Requires: xf86-input-mouse-license = %{version}-%{release}
Requires: xf86-input-mouse-man = %{version}-%{release}
BuildRequires : pkgconfig(inputproto)
BuildRequires : pkgconfig(xorg-macros)
BuildRequires : pkgconfig(xorg-server)
BuildRequires : pkgconfig(xproto)

%description
Mouse Support in xf86-input-mouse
Original version written by Kazutaka Yokota for XFree86 on 17 December 2002
Updated by Alan Coopersmith for X.Org releases
____________________________________________________________

%package dev
Summary: dev components for the xf86-input-mouse package.
Group: Development
Requires: xf86-input-mouse-lib = %{version}-%{release}
Provides: xf86-input-mouse-devel = %{version}-%{release}
Requires: xf86-input-mouse = %{version}-%{release}

%description dev
dev components for the xf86-input-mouse package.


%package lib
Summary: lib components for the xf86-input-mouse package.
Group: Libraries
Requires: xf86-input-mouse-license = %{version}-%{release}

%description lib
lib components for the xf86-input-mouse package.


%package license
Summary: license components for the xf86-input-mouse package.
Group: Default

%description license
license components for the xf86-input-mouse package.


%package man
Summary: man components for the xf86-input-mouse package.
Group: Default

%description man
man components for the xf86-input-mouse package.


%prep
%setup -q -n xf86-input-mouse-1.9.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1557105087
export CFLAGS="-O3 -g -fopt-info-vec "
unset LDFLAGS
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1557105087
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/xf86-input-mouse
cp COPYING %{buildroot}/usr/share/package-licenses/xf86-input-mouse/COPYING
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/xorg/xf86-mouse-properties.h
/usr/lib64/pkgconfig/xorg-mouse.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/xorg/modules/input/mouse_drv.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/xf86-input-mouse/COPYING

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man4/mousedrv.4
