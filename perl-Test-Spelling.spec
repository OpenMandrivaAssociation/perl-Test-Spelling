%define upstream_name    Test-Spelling
%define upstream_version 0.19

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Check for spelling errors in POD
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Test/Test-Spelling-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires: perl(Test::Tester)
BuildRequires: perl(IPC::Run3)
BuildRequires:	perl(Carp)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(Pod::Spell)
BuildRequires:	perl(Test::More)

BuildArch:	noarch
Requires:	aspell-en

%description
Check POD files for spelling mistakes, using the Pod::Spell manpage and
_spell_ to do the heavy lifting.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/Test

%changelog
* Tue May 31 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.140.0-1mdv2011.0
+ Revision: 682198
- update to new version 0.14

* Fri Apr 29 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.130.0-1
+ Revision: 660570
- new version
- drop aspell command patch, fixed upstream

* Sat Mar 27 2010 Jérôme Quelin <jquelin@mandriva.org> 0.110.0-2mdv2011.0
+ Revision: 527995
- using aspell in english by default

* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.110.0-1mdv2010.0
+ Revision: 405595
- rebuild using %%perl_convert_version

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.11-2mdv2009.0
+ Revision: 268739
- rebuild early 2009.0 package (before pixel changes)

* Sat May 31 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.11-1mdv2009.0
+ Revision: 213781
- import perl-Test-Spelling


* Sat May 31 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.11-1mdv2009.0
- first mdv release

