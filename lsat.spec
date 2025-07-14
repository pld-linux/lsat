# TODO
# - add weekly cron-job
Summary:	LSAT - Linux Security Auditing Tool
Summary(pl.UTF-8):	LSAT - linuksowe narzędzie do audytu bezpieczeństwa
Name:		lsat
Version:	0.9.7.1
Release:	0.1
Group:		Applications/System
License:	GPL v2
Source0:	http://usat.sourceforge.net/code/%{name}-%{version}.tgz
# Source0-md5:	441defd1f7f82c5eccd3b5a9f46fe5fa
Patch0:		%{name}-ftpusers_path.patch
URL:		http://usat.sourceforge.net/
BuildRequires:	perl-tools-pod
BuildRequires:	popt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Linux Security Auditing Tool (LSAT) is a post install security
auditing tool. It is modular in design, so new features can be added
quickly. It checks inetd entries and scans for unneeded RPM packages.

%description -l pl.UTF-8
Linux Security Auditing Tool (LSAT) jest narzędziem do
poinstalacyjnego audytu bezpieczeństwa. Jest zrobiony jako modularne
narzędzie, więc nowe funkcje mogą być szybko dodawane. Sprawdza wpisy
w inetd oraz skanuje niepotrzebne pakiety RPM.

%prep
%setup -q
%patch -P0 -p1

%build
# It has to be this macro - there is no configure.in included
%configure2_13

%{__make}
%{__make} manpage

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install installman \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README* *.txt *.html changelog/*.html
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man*/*
