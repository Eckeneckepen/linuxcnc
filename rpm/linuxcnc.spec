Summary:	LinuxCNC controls CNC machines.
Name:		linuxcnc
Version:	2.9.3++

Release:	1
License:	GPL
Group:		System/Packages
Source:		https://github.com/LinuxCNC/linuxcnc

Distribution:	openSUSE Tumbleweed 20240924
Vendor:		LinuxCNC.org
Packager:	%{packager}

Requires:       python311-qt5


%define         __spec_build_pre %{nil}
%define		__spec_install_post %{nil}

%description
LinuxCNC controls CNC machines.
It can drive milling machines, lathes, 3d printers, laser cutters, plasma cutters, robot arms, hexapods, and more.


%prep
make -C yapps

%build
export PATH=$PATH:%{_topdir}/yapps/target/bin
export PYTHONPATH=%{_topdir}/yapps/target/lib/python3.11/site-packages

export LDFLAGS="-ltirpc -lstdc++"


cd %{_sourcedir}

./autogen.sh
./configure --with-realtime=uspace --prefix=/opt --enable-non-distributable=yes
make -j 2

%install
cd %{_sourcedir}
make install DESTDIR=%{_topdir}/target
echo "#### End of install"

%files
%defattr(-,root,root)

/etc/X11/app-defaults/TkLinuxCNC
/opt/etc/linuxcnc
/opt/bin/*
/opt/lib64/*
/opt/include/linuxcnc
/opt/lib/linuxcnc
/opt/lib/tcltk/linuxcnc
/opt/share/linuxcnc
/usr/lib/python3.11/site-packages/*

%docdir /opt/share/man
/opt/share/man
%docdir /opt/share/doc/linuxcnc
/opt/share/doc/linuxcnc

/opt/share/qtvcp
/opt/share/glade
/opt/share/axis
/opt/share/gtksourceview-4
/opt/share/gscreen
/opt/share/gmoccapy
/usr/share/applications/*
/usr/share/locale/*/LC_MESSAGES/*
