%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

Summary:		a headless WebKit with JavaScript API
Name:			phantomjs
Version:		2.0.0
Release:		1%{?dist}
License:		BSD
Source0:		https://bitbucket.org/ariya/phantomjs/downloads/%{name}-%{version}-source.zip
URL:			http://phantomjs.org/
BuildRequires:	sqlite-devel
BuildRequires:	gperf
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	libicu-devel
BuildRequires:	gstreamer-devel
BuildRequires:	openssl-devel
BuildRequires:	freetype-devel
BuildRequires:	libX11-devel
BuildRequires:	libXext-devel
BuildRequires:	fontconfig-devel
BuildRequires:	libpng-devel
BuildRequires:	libjpeg-turbo-devel
BuildRequires:	ruby
%if 0%{?el7}%{?fedora}
BuildRequires:	harfbuzz-devel
%endif

%description
PhantomJS is a headless WebKit with JavaScript API. It has fast and native
support for various web standards: DOM handling, CSS selector, JSON,
Canvas, and SVG. PhantomJS is created by Ariya Hidayat.

%prep
%setup -q

%build
# Would prefer to use system QT, but PhantomJS currently requires 5.3.x
./build.sh --confirm --qt-config '-no-rpath'

%check
%{__make} check

%install
install -D bin/phantomjs %{buildroot}%{_bindir}/phantomjs

mkdir -p %{buildroot}%{_pkgdocdir}/examples
cp -p examples/* %{buildroot}%{_pkgdocdir}/examples/
cp README.md ChangeLog CONTRIBUTING.md %{buildroot}%{_pkgdocdir}
%{!?_licensedir: cp LICENSE.BSD third-party.txt %{buildroot}%{_pkgdocdir}}

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/phantomjs
%dir %{_pkgdocdir}
%doc %{_pkgdocdir}/*
%{?_licensedir: %license LICENSE.BSD}
%{?_licensedir: %license third-party.txt}

%changelog
* Sat Sep 12 2015 Steven Hadfield <hadfieldster@gmail.com> - 2.0.0-1
- Update to 2.0.0

* Fri Apr 18 2014 Eric Heydenberk <heydenberk@gmail.com>
- add missing filenames for examples to files section

* Tue Apr 30 2013 Eric Heydenberk <heydenberk@gmail.com>
- add missing filenames for examples to files section

* Wed Apr 24 2013 Robin Helgelin <lobbin@gmail.com>
- updated to version 1.9

* Thu Jan 24 2013 Matthew Barr <mbarr@snap-interactive.com>
- updated to version 1.8

* Thu Nov 15 2012 Jan Schaumann <jschauma@etsy.com>
- first rpm version
