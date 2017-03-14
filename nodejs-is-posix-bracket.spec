%{?scl:%scl_package nodejs-is-posix-bracket}
%{!?scl:%global pkg_name %{name}}
%{?nodejs_find_provides_and_requires}

%global enable_tests 0
%global npm_name is-posix-bracket

Name:       %{?scl_prefix}nodejs-%{npm_name}
Version:    0.1.1
Release:    1%{?dist}
Summary:    Returns true if the given string is a POSIX bracket expression (POSIX character class)
License:    MIT
URL:        https://github.com/jonschlinkert/is-posix-bracket
Source0:    http://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildRequires: %{?scl_prefix}nodejs-devel
BuildArch:  noarch
ExclusiveArch: %{nodejs_arches} noarch

%description
Returns true if the given string is a POSIX bracket expression (POSIX character class).

%prep
%setup -q -n package

rm -rf node_modules

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr index.js package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}

%nodejs_symlink_deps

%if 0%{?enable_tests}
%check
#not running tests in RHSCL
%endif

%files
%{nodejs_sitelib}/%{npm_name}

%doc LICENSE
%doc README.md

%changelog
* Tue Nov 01 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 0.1.1-1
- Initial build

