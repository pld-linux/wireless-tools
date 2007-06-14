Summary:	Wireless ethernet configuration tools
Summary(pl.UTF-8):	Narzędzia do konfiguracji sieci bezprzewodowej
Summary(pt_BR.UTF-8):	Ferramentas para redes sem fio
Name:		wireless-tools
Version:	29
#define		_pre	%{nil}
%define		_pre	.pre21
#Release:	1
Release:	0%{_pre}.1
Epoch:		1
License:	GPL v2
Group:		Networking/Admin
Source0:	http://www.hpl.hp.com/personal/Jean_Tourrilhes/Linux/wireless_tools.%{version}%{_pre}.tar.gz
# Source0-md5:	953774d6a34050bae4ef3bfa731f6653
Patch0:		%{name}-llh.patch
Patch1:		%{name}-optflags.patch
URL:		http://www.hpl.hp.com/personal/Jean_Tourrilhes/Linux/Tools.html
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
%patch0 -p1
%patch1 -p1

sed -i -e 's#__user##g' iwlib.h wireless.22.h

%build
%{__make} \
	CC="%{__cc}" \
	OPTFLAGS="%{rpmcflags}"

%{__make} libiw.a \
	CC="%{__cc}" \
	OPTFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_libdir},%{_includedir},%{_mandir}/man8}

%{__make} install install-dynamic install-static \
	INSTALL_DIR=$RPM_BUILD_ROOT%{_sbindir} \
	INSTALL_LIB=$RPM_BUILD_ROOT%{_libdir} \
	INSTALL_INC=$RPM_BUILD_ROOT%{_includedir} \
	INSTALL_MAN=$RPM_BUILD_ROOT%{_mandir}

install -d $RPM_BUILD_ROOT%{_mandir}/{cs,fr}/man{5,7,8}
install cs/*.5 $RPM_BUILD_ROOT%{_mandir}/cs/man5
install cs/*.7 $RPM_BUILD_ROOT%{_mandir}/cs/man7
install cs/*.8 $RPM_BUILD_ROOT%{_mandir}/cs/man8
install fr/*.5 $RPM_BUILD_ROOT%{_mandir}/fr/man5
install fr/*.7 $RPM_BUILD_ROOT%{_mandir}/fr/man7
install fr/*.8 $RPM_BUILD_ROOT%{_mandir}/fr/man8

%clean
rm -rf $RPM_BUILD_ROOT

%post	-n libiw -p /sbin/ldconfig
%postun	-n libiw -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc READ* INSTA* PCM*
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man[578]/*
%lang(cs) %{_mandir}/cs/man[578]/*
%lang(fr) %{_mandir}/fr/man[578]/*

%files -n libiw
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libiw.so.*

%files -n libiw-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libiw.so
%{_includedir}/*.h

%files -n libiw-static
%defattr(644,root,root,755)
%{_libdir}/libiw.a
