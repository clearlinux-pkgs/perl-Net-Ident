#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Net-Ident
Version  : 1.24
Release  : 5
URL      : https://cpan.metacpan.org/authors/id/T/TO/TODDR/Net-Ident-1.24.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/T/TO/TODDR/Net-Ident-1.24.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libn/libnet-ident-perl/libnet-ident-perl_1.24-1.debian.tar.xz
Summary  : 'Lookup the username on the remote end of a TCP/IP connection'
Group    : Development/Tools
License  : Artistic-1.0 GPL-1.0
Requires: perl-Net-Ident-license = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
NAME
Net::Ident - lookup the username on the remote end of a
TCP/IP connection
SYNOPSIS
use Net::Ident;

%package dev
Summary: dev components for the perl-Net-Ident package.
Group: Development
Provides: perl-Net-Ident-devel = %{version}-%{release}

%description dev
dev components for the perl-Net-Ident package.


%package license
Summary: license components for the perl-Net-Ident package.
Group: Default

%description license
license components for the perl-Net-Ident package.


%prep
%setup -q -n Net-Ident-1.24
cd ..
%setup -q -T -D -n Net-Ident-1.24 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/Net-Ident-1.24/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Net-Ident
cp deblicense/copyright %{buildroot}/usr/share/package-licenses/perl-Net-Ident/deblicense_copyright
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1Net/Ident.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Net::Ident.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Net-Ident/deblicense_copyright
