%define upstream_name    Test-Spelling
%define upstream_version 0.11

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    Check for spelling errors in POD
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Test/%{upstream_name}-%{upstream_version}.tar.gz
Patch0:     %{upstream_name}-0.11-use-aspell.patch

BuildRequires: perl(Carp)
BuildRequires: perl(File::Spec)
BuildRequires: perl(File::Temp)
BuildRequires: perl(Pod::Spell)
BuildRequires: perl(Test::More)

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

Requires: aspell-en

%description
Check POD files for spelling mistakes, using the Pod::Spell manpage and
_spell_ to do the heavy lifting.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
%patch0 -p 2 -b .aspell

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/Test
