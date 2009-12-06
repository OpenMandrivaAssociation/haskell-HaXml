%define module HaXml

Name: haskell-%{module}
Version: 1.20
Release: %mkrel 1
Summary: A library to parse/write XML files
Url: http://www.cs.york.ac.uk/fp/HaXml
Group: Development/Other
License: LGPL
Source: http://hackage.haskell.org/packages/archive/%{module}/%{version}/%{module}-%{version}.tar.gz
BuildRequires: ghc
BuildRequires: haddock
BuildRequires: haskell(polyparse) >= 1.2
BuildRequires: haskell-macros
BuildRoot: %_tmppath/%name-%version-%release-root

%description
Haskell utilities for parsing, filtering, transforming and
generating XML documents.

%prep
%setup -q -n %{module}-%{version}

%build
%_cabal_build

%_cabal_genscripts

%check
%_cabal_check

%install
%_cabal_install

rm -fr %{buildroot}/%_datadir/*/doc/

%_cabal_rpm_gen_deps

%_cabal_scriptlets

%files
%defattr(-,root,root)
%_libdir/%{module}-%{version}
%{_docdir}/%{module}-%{version}
%_bindir/*
%_cabal_rpm_files

%clean
rm -fr %buildroot
