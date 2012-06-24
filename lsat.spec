# TODO
# - add weekly cron-job
Summary:	LSAT - Linux Security Auditing Tool
Summary(pl):	LSAT - Linuksowe narz�dzie do audytu bezpiecze�stwa
Name:		lsat
Version:	0.7.3
Release:	1
Group:		Applications/System
License:	GPL v2
Source0:	http://usat.sourceforge.net/code/%{name}-%{version}.tgz
# Source0-md5:	637a461b2035dcb7a9b9f78e2823558f
URL:		http://usat.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Linux Security Auditing Tool (LSAT) is a post install security
auditing tool. It is modular in design, so new features can be added
quickly. It checks inetd entries and scans for unneeded RPM packages.

%description -l pl
Linux Security Auditing Tool (LSAT) jest narz�dziem do poinstalacyjnego
audytu bezpiecze�stwa. Jest zrobiony jako modularne narz�dzie, wi�c
nowe ficzery mog� by� szybko dodawane. Sprawdza wpisy w inetd oraz 
skanuje niepotrzebne pakiety RPM. 

%prep
%setup -q

%build
%configure2_13

%{__make}
%{__make} manpage

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install installman

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README* *.txt *.html changelog/*.html
%attr(755,root,root) %{_bindir}/*
%attr(644,root,root) %{_mandir}/man*/*
