%define module HaXml

Name: haskell-%{module}
Version: 1.13.2
Release: %mkrel 2
Summary: A library to parse/write XML files
Url: http://www.cs.york.ac.uk/fp/HaXml
Group: Development/Other
License: LGPL
Source: http://www.haskell.org/HaXml/%{module}-%{version}.tar.bz2
BuildRequires: ghc
BuildRequires: haddock
BuildRoot: %_tmppath/%name-%version-%release-root
Requires(post): ghc
Requires(preun): ghc

%description
Haskell utilities for parsing, filtering, transforming and
generating XML documents.

%prep
%setup -q -n %{module}-%{version}

%build
runhaskell Setup.hs configure --prefix=%{_prefix}
runhaskell Setup.hs build
runhaskell Setup.hs haddock

runhaskell Setup.hs   register --gen-script
runhaskell Setup.hs unregister --gen-script

%install
runhaskell Setup.hs copy --destdir=%{buildroot}

rm -fr %{buildroot}%{_datadir}/%{module}-%{version}/doc

%check
runhaskell Setup.hs test

%post -f register.sh

%preun -f unregister.sh

%files
%defattr(-,root,root)
%doc dist/doc/html
%doc README
%_libdir/%{module}-%{version}
%_bindir/*

%clean
rm -fr %buildroot



