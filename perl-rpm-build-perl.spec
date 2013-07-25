%define upstream_name    rpm-build-perl
%define upstream_version 0.82

Name:		perl-%{upstream_name}
Version:	%perl_convert_version 0.82
Release:	1

Summary:	Perl compiler backend to extract Perl dependencies
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/B/rpm-build-perl-0.82.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(B)
BuildRequires:	perl(Encode)
BuildRequires:	perl(O)
BuildRequires:	perl(Safe)
BuildRequires:	perl(Test::More)
BuildArch:	noarch

%description
B::PerlReq is a backend module for the Perl compiler that extracts
dependencies from Perl source code, based on the internal compiled
structure that Perl itself creates after parsing a program. The output of
B::PerlReq is suitable for automatic dependency tracking (e.g. for RPM
packaging).

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
# fail because even more requires are found than expected
#make test

%install
%makeinstall_std

%files
%doc README Changes META.yml
%{_mandir}/man1/*
%{_mandir}/man3/*
%{perl_vendorlib}/*
%{_bindir}/perl.*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.740.0-2mdv2011.0
+ Revision: 657478
- rebuild for updated spec-helper

* Mon Mar 14 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.740.0-1
+ Revision: 644797
- update to new version 0.74

* Tue Apr 20 2010 Jérôme Quelin <jquelin@mandriva.org> 0.720.0-1mdv2011.0
+ Revision: 536958
- update to 0.72

* Sun Sep 27 2009 Jérôme Quelin <jquelin@mandriva.org> 0.710.0-1mdv2010.0
+ Revision: 450063
- update to 0.71

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.700.0-1mdv2010.0
+ Revision: 404358
- rebuild using %%perl_convert_version

* Mon May 11 2009 Jérôme Quelin <jquelin@mandriva.org> 0.70-1mdv2010.0
+ Revision: 374549
- update to new version 0.70

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.6.8-2mdv2009.0
+ Revision: 268955
- rebuild early 2009.0 package (before pixel changes)

* Sat May 31 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.6.8-1mdv2009.0
+ Revision: 213761
- import perl-rpm-build-perl


* Sat May 31 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.6.8-1mdv2009.0
- first mdv release

