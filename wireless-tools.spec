Summary:	Wireless ethernet configuration tools
Summary(pl):	Narz�dzia do konfiguracji sieci bezprzewodowej
Summary(pt_BR):	Ferramentas para redes sem fio
Name:		wireless-tools
Version:	28
%define	pre	pre6
Release:	0.%{pre}.1
Epoch:		1
License:	GPL v2
Group:		Networking/Admin
Source0:	http://www.hpl.hp.com/personal/Jean_Tourrilhes/Linux/wireless_tools.%{version}.%{pre}.tar.gz
# Source0-md5:	3ad1da3b17dff963eba32f0b79401253
URL:		http://www.hpl.hp.com/personal/Jean_Tourrilhes/Linux/Tools.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir	/sbin

%description
This package contains the Wireless tools, used to manipulate the
Wireless Extensions. The Wireless Extension is an interface allowing
you to set Wireless LAN specific parameters and get the specific stats
for wireless networking equipment.

%description -l pl
Narz�dzie u�ywane do manipulacji Rozszerzeniami Bezprzewodowymi.
Rozszerzenia Bezprzewodowe to interfejs pozwalaj�cy na ustawianie
parametr�w i uzyskiwanie statystyk na temat bezprzewodowych urz�dze�.

%description -l pt_BR
Este pacote cont�m ferramentas para redes sem fio, utilizadas para
manipular as wireless extensions. Wireless extensions � uma interface
que permite que voc� modifique par�metros espec�ficos para redes sem
fio e verificar estat�sticas sobre estas.

%package -n libiw
Summary:	Wireless Extension library
Summary(pl):	Biblioteka rozszerze� bezprzewodowych
Group:		Libraries

%description -n libiw
Wireless Extension library.

%description -n libiw -l pl
Biblioteka rozszerze� bezprzewodowych.

%package -n libiw-devel
Summary:	Wireless Extension library (development files)
Summary(pl):	Biblioteka rozszerze� bezprzewodowych (pliki developerskie)
Group:		Development/Libraries
Requires:	libiw = %{epoch}:%{version}-%{release}

%description -n libiw-devel
Wireless Extension library (development files).

%description -n libiw-devel -l pl
Biblioteka rozszerze� bezprzewodowych (pliki developerskie).

%package -n libiw-static
Summary:	Wireless Extension library (static library)
Summary(pl):	Biblioteka rozszerze� bezprzewodowych (biblioteka statyczna)
Group:		Development/Libraries
Requires:	libiw-devel = %{epoch}:%{version}-%{release}

%description -n libiw-static
Wireless Extension library (static library).

%description -n libiw-static -l pl
iblioteka rozszerze� bezprzewodowych (biblioteka statyczna).

%prep
%setup -q -n wireless_tools.%{version}

%build
%{__make} \
	CC="%{__cc}" OPT="%{rpmcflags}" \
	KERNEL_SRC=%{_kernelsrcdir}

sed -i -e 's#.*BUILD_STATIC = y#BUILD_STATIC = y#g' Makefile
%{__make} libiw.a \
	CC="%{__cc}" OPT="%{rpmcflags}" \
	KERNEL_SRC=%{_kernelsrcdir}


%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_libdir},%{_includedir},%{_mandir}/man8}

%{__make} install install-dynamic install-static \
	INSTALL_DIR=$RPM_BUILD_ROOT%{_sbindir} \
	INSTALL_LIB=$RPM_BUILD_ROOT%{_libdir} \
	INSTALL_INC=$RPM_BUILD_ROOT%{_includedir} \
	INSTALL_MAN=$RPM_BUILD_ROOT%{_mandir}

%clean
rm -rf $RPM_BUILD_ROOT

%post -n libiw -p /sbin/ldconfig
%postun -n libiw -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc READ* INSTA* PCM*
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man?/*

%files -n libiw
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*

%files -n libiw-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/*.h

%files -n libiw-static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
