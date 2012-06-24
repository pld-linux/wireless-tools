Summary:	Wireless ethernet configuration tools
Summary(pl):	Narz�dzia do konfiguracji sieci bezprzewodowej
Summary(pt_BR):	Ferramentas para redes sem fio
Name:		wireless-tools
Version:	24
Release:	1
License:	GPL v2
Group:		Networking/Admin
Source0:	http://pcmcia-cs.sourceforge.net/ftp/contrib/wireless_tools.%{version}.tar.gz
Source1:	wireless.init
#Patch0:	%{name}-opt.patch
URL:		http://www.hpl.hp.com/personal/Jean_Tourrilhes/Linux/Tools.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contain the Wireless tools, used to manipulate the
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

%prep
%setup  -q -n wireless_tools.%{version}
# %patch0 -p1

%build
%{__make} OPT="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_libdir},%{_includedir},%{_mandir}/man8} \
	$RPM_BUILD_ROOT%{_sysconfdir}/rc.d/init.d

install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/rc.d/init.d/wavelan

%{__make} install \
	INSTALL_DIR=$RPM_BUILD_ROOT%{_sbindir} \
	INSTALL_LIB=$RPM_BUILD_ROOT%{_libdir} \
	INSTALL_INC=$RPM_BUILD_ROOT%{_includedir} \
	INSTALL_MAN=$RPM_BUILD_ROOT%{_mandir}

gzip -9nf READ* INSTA* PCM*

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/chkconfig --add wavelan

%preun
if [ "$1" = "0" ]; then
	/sbin/chkconfig --del wavelan
fi

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_sbindir}/*
%attr(754,root,root) %{_sysconfdir}/rc.d/init.d/wavelan
%{_mandir}/man?/*
