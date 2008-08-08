%define module   rpm-build-perl
%define version    0.6.8
%define release    %mkrel 2

Name:       perl-%{module}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Perl compiler backend to extract Perl dependencies
Url:        http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/B/%{module}-%{version}.tar.gz
BuildRequires: perl(B)
BuildRequires: perl(Encode)
BuildRequires: perl(O)
BuildRequires: perl(Safe)
BuildRequires: perl(Test::More)
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description

B::PerlReq is a backend module for the Perl compiler that extracts
dependencies from Perl source code, based on the internal compiled
structure that Perl itself creates after parsing a program. The output of
B::PerlReq is suitable for automatic dependency tracking (e.g. for RPM
packaging).

%prep
%setup -q -n %{module}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README Changes META.yml
%{_mandir}/man1/*
%{_mandir}/man3/*
%{perl_vendorlib}/*
%{_bindir}/perl.*

