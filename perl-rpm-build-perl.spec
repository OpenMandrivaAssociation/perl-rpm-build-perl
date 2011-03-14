%define upstream_name    rpm-build-perl
%define upstream_version 0.74

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Perl compiler backend to extract Perl dependencies
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/B/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(B)
BuildRequires: perl(Encode)
BuildRequires: perl(O)
BuildRequires: perl(Safe)
BuildRequires: perl(Test::More)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
B::PerlReq is a backend module for the Perl compiler that extracts
dependencies from Perl source code, based on the internal compiled
structure that Perl itself creates after parsing a program. The output of
B::PerlReq is suitable for automatic dependency tracking (e.g. for RPM
packaging).

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
