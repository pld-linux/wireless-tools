Summary:	Wireless ethernet configuration tools
Summary(pl):	Narzêdzia konfiguracji sieci bezprzedowowej
Name:		wireless-tools
Version:	22
Release:	1.pre1
License:	GPL
Group:		Networking/Admin
Group(de):	Netzwerkwesen/Administration
Group(pl):	Sieciowe/Administracyjne
Source0:	http://www.hpl.hp.com/personal/Jean_Tourrilhes/Linux/wireless_tools.%{version}.pre1.tar.gz
Source1:	wireless.init
Patch0:		%{name}-opt.patch
URL:		http://www.hpl.hp.com/personal/Jean_Tourrilhes/Linux/Tools.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contain the Wireless tools, used to manipulate
the Wireless Extensions. The Wireless Extension is an interface
allowing you to set Wireless LAN specific parameters and get the
specific stats for wireless networking equipment.

%description -l pl
Narzêdzie u¿ywane do manipulacji Rozszerzeniami Bezprzewodowymi.
Rozszerzenia Bezprzewodowe to interfejs pozwalaj±cy na ustawianie
parametrów i uzyskiwanie statystyk na temat bezprzewodowych
urz±dzeñ.

%prep
%setup  -q -n wireless_tools.%{version}
%patch0 -p1

%build
%{__make} OPT="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8} \
	$RPM_BUILD_ROOT%{_sysconfdir}/rc.d/init.d

install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/rc.d/init.d/wavelan

%{__make} install \
	INSTALL_DIR=$RPM_BUILD_ROOT%{_sbindir}
	
install *.8 $RPM_BUILD_ROOT%{_mandir}/man8

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
