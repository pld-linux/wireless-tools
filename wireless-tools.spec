%define	pre	pre9
Summary:	Wireless ethernet configuration tools
Summary(pl.UTF-8):	Narzędzia do konfiguracji sieci bezprzewodowej
Summary(pt_BR.UTF-8):	Ferramentas para redes sem fio
Name:		wireless-tools
Version:	30
Release:	0.%{pre}.1
Epoch:		1
License:	GPL v2
Group:		Networking/Admin
Source0:	https://hewlettpackard.github.io/wireless-tools/wireless_tools.%{version}.%{pre}.tar.gz
# Source0-md5:	ca91ba7c7eff9bfff6926b1a34a4697d
Patch0:		%{name}-optflags.patch
Patch1:		%{name}-debian.patch
URL:		https://hewlettpackard.github.io/wireless-tools/Tools.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir	/sbin

%define		specflags	-fno-strict-aliasing

%description
This package contains the Wireless tools, used to manipulate the
Wireless Extensions. The Wireless Extension is an interface allowing
you to set Wireless LAN specific parameters and get the specific stats
for wireless networking equipment.

%description -l pl.UTF-8
Narzędzie używane do manipulacji Rozszerzeniami Bezprzewodowymi.
Rozszerzenia Bezprzewodowe to interfejs pozwalający na ustawianie
parametrów i uzyskiwanie statystyk na temat bezprzewodowych urządzeń.

%description -l pt_BR.UTF-8
Este pacote contém ferramentas para redes sem fio, utilizadas para
manipular as wireless extensions. Wireless extensions é uma interface
que permite que você modifique parâmetros específicos para redes sem
fio e verificar estatísticas sobre estas.

%package -n libiw
Summary:	Wireless Extension library
Summary(pl.UTF-8):	Biblioteka rozszerzeń bezprzewodowych
Group:		Libraries

%description -n libiw
Wireless Extension library.

%description -n libiw -l pl.UTF-8
Biblioteka rozszerzeń bezprzewodowych.

%package -n libiw-devel
Summary:	Wireless Extension library (development files)
Summary(pl.UTF-8):	Biblioteka rozszerzeń bezprzewodowych (pliki developerskie)
Group:		Development/Libraries
Requires:	libiw = %{epoch}:%{version}-%{release}

%description -n libiw-devel
Wireless Extension library (development files).

%description -n libiw-devel -l pl.UTF-8
Biblioteka rozszerzeń bezprzewodowych (pliki developerskie).

%package -n libiw-static
Summary:	Wireless Extension library (static library)
Summary(pl.UTF-8):	Biblioteka rozszerzeń bezprzewodowych (biblioteka statyczna)
Group:		Development/Libraries
Requires:	libiw-devel = %{epoch}:%{version}-%{release}

%description -n libiw-static
Wireless Extension library (static library).

%description -n libiw-static -l pl.UTF-8
Biblioteka rozszerzeń bezprzewodowych (biblioteka statyczna).

%prep
%setup -q -n wireless_tools.%{version}
%patch -P0 -p1
%patch -P1 -p1

%build
%{__make} \
	CC="%{__cc}" \
	OPTFLAGS="%{rpmcflags} %{rpmcppflags}"

%{__make} libiw.a \
	CC="%{__cc}" \
	OPTFLAGS="%{rpmcflags} %{rpmcppflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},/%{_lib},%{_libdir},%{_includedir},%{_mandir}/man8}

%{__make} install install-dynamic install-static \
	INSTALL_DIR=$RPM_BUILD_ROOT%{_sbindir} \
	INSTALL_LIB=$RPM_BUILD_ROOT%{_libdir} \
	INSTALL_INC=$RPM_BUILD_ROOT%{_includedir} \
	INSTALL_MAN=$RPM_BUILD_ROOT%{_mandir}

%{__mv} $RPM_BUILD_ROOT%{_libdir}/libiw.so.* $RPM_BUILD_ROOT/%{_lib}
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libiw.so
ln -sf /%{_lib}/$(cd $RPM_BUILD_ROOT/%{_lib}; echo libiw.so.*) \
	$RPM_BUILD_ROOT%{_libdir}/libiw.so

%{__rm} -r $RPM_BUILD_ROOT%{_mandir}/fr.ISO*
%{__mv} $RPM_BUILD_ROOT%{_mandir}/fr{.UTF-8,}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-n libiw -p /sbin/ldconfig
%postun	-n libiw -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGELOG.h ESSID-BUG.txt HOTPLUG-UDEV.txt IFRENAME-VS-XXX.txt PCMCIA.txt README
%lang(fr) %doc README.fr
%attr(755,root,root) %{_sbindir}/ifrename
%attr(755,root,root) %{_sbindir}/iwconfig
%attr(755,root,root) %{_sbindir}/iwevent
%attr(755,root,root) %{_sbindir}/iwgetid
%attr(755,root,root) %{_sbindir}/iwlist
%attr(755,root,root) %{_sbindir}/iwpriv
%attr(755,root,root) %{_sbindir}/iwspy
%{_mandir}/man5/iftab.5*
%{_mandir}/man7/wireless.7*
%{_mandir}/man8/ifrename.8*
%{_mandir}/man8/iwconfig.8*
%{_mandir}/man8/iwevent.8*
%{_mandir}/man8/iwgetid.8*
%{_mandir}/man8/iwlist.8*
%{_mandir}/man8/iwpriv.8*
%{_mandir}/man8/iwspy.8*
%lang(cs) %{_mandir}/cs/man[578]/*
%lang(fr) %{_mandir}/fr/man[578]/*

%files -n libiw
%defattr(644,root,root,755)
%attr(755,root,root) /%{_lib}/libiw.so.*

%files -n libiw-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libiw.so
%{_includedir}/iwlib.h
%{_includedir}/wireless.h

%files -n libiw-static
%defattr(644,root,root,755)
%{_libdir}/libiw.a
