Summary:	LinuxCNC controls CNC machines.
Name:		linuxcnc
Version:	2.9.3++

Release:	1
License:	GPL
Group:		System/Packages
Source:		https://github.com/LinuxCNC/linuxcnc

Distribution:	openSUSE Tumbleweed 20240924
Vendor:		LinuxCNC.org
Packager:	Carsten Prescher


%define         __spec_build_pre %{nil}
%define		__spec_install_post %{nil}

%description
LinuxCNC controls CNC machines.
It can drive milling machines, lathes, 3d printers, laser cutters, plasma cutters, robot arms, hexapods, and more.

%prep
make -C yapps

%build

export PATH=$PATH:$PWD/yapps/target/bin
export PYTHONPATH=$PWD/yapps/target/lib/python3.11/site-packages

export LDFLAGS="-ltirpc -lstdc++"
export PATH=$PATH:$PWD/opentarget/bin

rm -rf $RPM_BUILD_ROOT

cd %{_sourcedir }

./autogen.sh
./configure --prefix=/opt --enable-non-distributable=yes
make

%install
make install DESTDIR=$RPM_BUILD_ROOT

%files
%defattr(-,root,root)

/etc/X11/app-defaults/TkLinuxCNC
/opt/etc/linuxcnc
/opt/etc/linuxcnc/rtapi.conf
/opt/bin/*
/opt/lib64/*
/opt/lib64/linuxcnc
/opt/lib64/libpyplugin.so.0
/opt/lib64/libposemath.so
/opt/lib64/libtooldata.so.0
/opt/lib64/liblinuxcncini.so.0
/opt/lib64/librs274.so
/opt/lib64/liblinuxcnc.a
/opt/lib64/liblinuxcnchal.so.0
/opt/lib64/libtooldata.so
/opt/lib64/libposemath.so.0
/opt/lib64/liblinuxcnchal.so
/opt/lib64/librs274.so.0
/opt/lib64/liblinuxcncini.so
/opt/lib64/libnml.so
/opt/lib64/libnml.so.0
/opt/include/linuxcnc
/opt/lib/linuxcnc
/opt/lib/tcltk/linuxcnc
/opt/lib/tcltk/linuxcnc/scripts
/opt/lib/tcltk/linuxcnc/scripts/*
/opt/lib/tcltk/linuxcnc/*
/opt/lib/tcltk/linuxcnc/bin
/opt/lib/tcltk/linuxcnc/bin/*
/opt/lib/tcltk/linuxcnc/msgs
/opt/lib/tcltk/linuxcnc/msgs/*
/opt/share/linuxcnc
/opt/share/man/man1/*
/opt/share/man/man3/*
/opt/share/man/man9/*
/opt/share/doc/linuxcnc
/opt/share/qtvcp
/opt/share/glade
/opt/share/axis
/opt/share/gtksourceview-4
/opt/share/gscreen
/opt/share/gmoccapy
/usr/lib/python3.11/site-packages/*
/usr/share/applications/*
/usr/share/locale/*/LC_MESSAGES/*
