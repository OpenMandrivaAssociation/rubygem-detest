%define oname detest

Name:       rubygem-%{oname}
Version:    3.1.2
Release:    %mkrel 1
Summary:    Assertion testing library for Ruby
Group:      Development/Ruby
License:    ISC License
URL:        https://snk.tuxfamily.org/lib/detest/
Source0:    %{oname}-%{version}.gem
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root
Requires:   rubygems
Suggests:   rubygem(inochi) >= 5.0.1
BuildRequires: rubygems
BuildArch:  noarch
Provides:   rubygem(%{oname}) = %{version}

%description
Detest is an assertion testing library for the Ruby programming language. It
features a simple assertion vocabulary, instant debuggability of failures,
and flexibility in composing tests.


%prep

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{ruby_gemdir}
gem install --local --install-dir %{buildroot}%{ruby_gemdir} \
            --force --rdoc %{SOURCE0}
mkdir -p %{buildroot}/%{_bindir}
mv %{buildroot}%{ruby_gemdir}/bin/* %{buildroot}/%{_bindir}
rmdir %{buildroot}%{ruby_gemdir}/bin
find %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/bin -type f | xargs chmod a+x

# Move manpages to mandir
mkdir -p %{buildroot}/%{_mandir}
mv %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/man/* %{buildroot}/%{_mandir}
rmdir %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/man

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%{_bindir}/detest
%dir %{ruby_gemdir}/gems/%{oname}-%{version}/
%{ruby_gemdir}/gems/%{oname}-%{version}/bin/
%{ruby_gemdir}/gems/%{oname}-%{version}/lib/
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/CREDITS
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/LICENSE
%doc %{ruby_gemdir}/doc/%{oname}-%{version}
%{ruby_gemdir}/cache/%{oname}-%{version}.gem
%{ruby_gemdir}/specifications/%{oname}-%{version}.gemspec
%{_mandir}/man1/%{oname}.1.*
