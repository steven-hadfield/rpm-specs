#
# Conditional build:
%bcond_without	static_libs	# don't build static libraries
%bcond_without	tests		# don't run tests

Summary:	Library for working with MaxMind DB files
Name:		libmaxminddb
Version:	1.1.1
Release:	1%{?dist}
License:	ASL 2.0
Group:		System Environment/Libraries
Source0:	https://github.com/maxmind/libmaxminddb/releases/download/%{version}/%{name}-%{version}.tar.gz
URL:		http://maxmind.github.io/libmaxminddb/
BuildRequires:	libtool
%if %{with tests}
BuildRequires:	perl(Test::More) >= 0.88
BuildRequires:	perl-IPC-Run3
BuildRequires:	perl-Test-Output
%endif

%description
The libmaxminddb library provides a C library for reading MaxMind DB
files, including the GeoIP2 databases from MaxMind. This is a custom
binary format designed to facilitate fast lookups of IP addresses
while allowing for great flexibility in the type of data associated
with an address.

%package devel
Summary:	Header files for %{name} library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{name} library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki %{name}.

%package static
Summary:	Static %{name} library
Summary(pl.UTF-8):	Statyczna biblioteka %{name}
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static %{name} library.

%description static -l pl.UTF-8
Statyczna biblioteka %{name}.

%prep
%setup -q

%build
%configure \
	%{!?with_static_libs:--disable-static}
# Avoid using local libtool which forces rpath
sed -i 's|^LIBTOOL=.*|LIBTOOL="/usr/bin/libtool"|g' configure
%{__make}

%if %{with tests}
%check
%{__make} check
%endif

%install
%make_install

rm %{buildroot}/%{_libdir}/libmaxminddb.la

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mmdblookup
%attr(755,root,root) %{_libdir}/libmaxminddb.so.*.*.*
%{_libdir}/libmaxminddb.so.0
%{_mandir}/man1/mmdblookup.1*

%files devel
%defattr(644,root,root,755)
%doc doc/libmaxminddb.md
%{_libdir}/%{name}.so
%{_includedir}/maxminddb.h
%{_includedir}/maxminddb_config.h
%{_mandir}/man3/MMDB_*.3*
%{_mandir}/man3/libmaxminddb.3*

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libmaxminddb.a
%endif

%changelog
* Thu Sep 10 2015 Steven Hadfield <steven.hadfield@business.com> - 1.1.1-1
- Update to upstream 1.1.1

* Thu Jan 23 2014 Steven Hadfield <steven.hadfield@business.com>
- Adapted for Fedora

* Tue Dec 24 2013 PLD Linux Team <feedback@pld-linux.org>
- For complete changelog see: http://git.pld-linux.org/?p=packages/libmaxminddb.git;a=log;h=master

* Tue Dec 24 2013 Elan Ruusamäe <glen@delfi.ee> e1b1f24
- up to 0.5.3

* Sun Dec 22 2013 Elan Ruusamäe <glen@delfi.ee> 5cd9f67
- update test deps; enchance description

* Sun Dec 22 2013 Elan Ruusamäe <glen@delfi.ee> 0615b33
- run tests

* Sun Dec 22 2013 Elan Ruusamäe <glen@delfi.ee> 3a54679
- new, version 0.5.2

