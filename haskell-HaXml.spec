#% global debug_package %{nil}
#% define _cabal_setup Setup.lhs
#% define _no_haddock 1
%define module HaXml
Name:           haskell-%{module}
Version:        1.23.3
Release:        1
Summary:        Utilities for manipulating XML documents
Group:          Development/Other
License:        LGPL
URL:            http://hackage.haskell.org/package/%{module}
Source0:        http://hackage.haskell.org/packages/archive/%{module}/%{version}/%{module}-%{version}.tar.gz

BuildRequires:  ghc, ghc-devel, haskell-macros, haddock
buildrequires:  haskell(polyparse)
buildrequires:  haskell(random)
Requires(pre):  ghc
requires(pre):  haskell(polyparse)
requires(pre):  haskell(random)

%description
Haskell utilities for parsing, filtering, transforming and generating XML
documents.

%prep
%setup -q -n %{module}-%{version}

%build
%_cabal_build

%install
%_cabal_install
%_cabal_rpm_gen_deps
%_cabal_scriptlets

%check
%_cabal_check

%files
%defattr(-,root,root,-)
%{_docdir}/%{module}-%{version}
%{_libdir}/%{module}-%{version}
%_cabal_rpm_deps_dir
%_cabal_haddoc_files
%{_bindir}/*



