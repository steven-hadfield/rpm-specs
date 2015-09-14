%define			pkgname	reader
%define			php_min_version 5.3.1
%define			maxminddb_min_version 0.5.3
Summary:		MaxMind DB Reader PHP Extension
Name:			php-maxmind-db-%{pkgname}-ext
Version:		1.0.3
Release:		1%{?dist}
License:		ASL 2.0
Group:			Development/Libraries
Source0:		https://github.com/maxmind/MaxMind-DB-Reader-php/archive/v%{version}/%{pkgname}-%{version}.tar.gz
URL:			https://github.com/maxmind/MaxMind-DB-Reader-php
BuildRequires:	php-devel
BuildRequires:	libmaxminddb-devel
Requires:		php(zend-abi) = %{php_zend_api}
Requires:		php(api) = %{php_core_api}
Requires:		libmaxminddb >= %{maxminddb_min_version}
Requires:		php(language) >= %{php_min_version}

%global php_apiver  %((echo 0; php -i 2>/dev/null | sed -n 's/^PHP API => //p') | tail -1)
%global php_inidir  %((echo 0; php -i 2>/dev/null | sed -n 's/^Scan this dir for additional .ini files => //p') | tail -1)
%global php_extdir  %(php-config --extension-dir 2>/dev/null || echo "undefined")
%global php_version %(php-config --version 2>/dev/null || echo 0)

%description
PHP Reader for the MaxMind DB Database Format.

This is the C library implementation for reading MaxMind DB files
that promises much better performance than the pure PHP version.
MaxMind DB is a binary file format that stores data indexed by IP
address subnets (IPv4 or IPv6).

%prep
%setup -qn MaxMind-DB-Reader-php-%{version}

%build
# Generate ini file for inclusion
echo '; Include MaxMind DB Reader extension
extension=maxminddb.so' > maxminddb.ini
cd ext
phpize
%configure
%{__make}

%check
NO_INTERACTION=yes %{__make} --directory=ext test

%install
install -d %{buildroot}%{php_inidir}
cp -a maxminddb.ini %{buildroot}%{php_inidir}/40-maxminddb.ini
%{__make} install --directory=ext \
	INSTALL_ROOT=%{buildroot}

%files
%defattr(644,root,root,755)
%doc README.md CHANGELOG.md
%{php_extdir}/maxminddb.so
%config(noreplace) %{php_inidir}/40-maxminddb.ini

%changelog
* Thu Sep 10 2015 Steven Hadfield <steven.hadfield@business.com> - 1.0.3-1
- Update to upstream 1.0.3

* Wed Feb 5 2014 Steven Hadfield <steven.hadfield@business.com>
- Build from master HEAD (7591bc8b4f275f360377763b26921911b8f1c9dd)

* Fri Jan 24 2014 Steven Hadfield <steven.hadfield@business.com>
- New 0.2.0

