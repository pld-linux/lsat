# TODO
# - add weekly cron-job
Summary:	LSAT - Linux Security Auditing Tool
Summary(pl):	LSAT - linuksowe narzêdzie do audytu bezpieczeñstwa
Name:		lsat
Version:	0.9.1
Release:	0.1
Group:		Applications/System
License:	GPL v2
Source0:	http://usat.sourceforge.net/code/%{name}-%{version}.tgz
# Source0-md5:	ae2b979d00a7f72261827f945980e79b
Patch0:		%{name}-ftpusers_path.patch
URL:		http://usat.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Linux Security Auditing Tool (LSAT) is a post install security
auditing tool. It is modular in design, so new features can be added
quickly. It checks inetd entries and scans for unneeded RPM packages.

%description -l pl
Linux Security Auditing Tool (LSAT) jest narzêdziem do
poinstalacyjnego audytu bezpieczeñstwa. Jest zrobiony jako modularne
narzêdzie, wiêc nowe funkcje mog± byæ szybko dodawane. Sprawdza wpisy
w inetd oraz skanuje niepotrzebne pakiety RPM.

%prep
%setup -q
%patch0 -p1

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
%attr(644,root,root) %{_mandir}/man*/*
