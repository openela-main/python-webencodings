%global srcname webencodings
%global desc This is a Python implementation of the WHATWG Encoding standard.

%if 0%{?rhel} > 7
# Disable python2 build by default
%bcond_with python2
%else
%bcond_without python2
%endif

Name: python-%{srcname}
Version: 0.5.1
Release: 6%{?dist}
BuildArch: noarch

License: BSD
Summary: Character encoding for the web
URL: https://github.com/gsnedders/python-%{srcname}
Source0: %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz

%if %{with python2}
BuildRequires: python2-devel
BuildRequires: python2-pytest
%endif # with python2
BuildRequires: python3-devel
BuildRequires: python3-pytest
BuildRequires: python3-sphinx


%description
%{desc}


%package doc
Summary: Documentation for python-webencodings


%description doc
Documentation for python-webencodings.

%if %{with python2}
%package -n python2-%{srcname}
Summary: %{summary}

%{?python_provide:%python_provide python2-%{srcname}}

Requires: python2


%description -n python2-%{srcname}
%{desc}
%endif # with python2


%package -n python3-%{srcname}
Summary: %{summary}

%{?python_provide:%python_provide python3-%{srcname}}

%{?__python3:Requires: %{__python3}}


%description -n python3-%{srcname}
%{desc}


%prep
%autosetup -n python-%{srcname}-%{version}


%build
%if %{with python2}
%py2_build
%endif # with python2
%py3_build

PYTHONPATH=. sphinx-build-3 docs docs/_build

# Remove unneeded build artifacts.
rm -rf docs/_build/.buildinfo
rm -rf docs/_build/.doctrees


%install
%if %{with python2}
%py2_install
%endif # with python2
%py3_install


%check
%if %{with python2}
py.test-2
%endif # with python2
py.test-3


%files doc
%license LICENSE
%doc docs/_build

%if %{with python2}
%files -n python2-%{srcname}
%license LICENSE
%doc README.rst
%{python2_sitelib}/%{srcname}
%{python2_sitelib}/*.egg-info
%endif # with python2

%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/*.egg-info


%changelog
* Tue Sep 25 2018 Tomas Orsava <torsava@redhat.com> - 0.5.1-6
- Require the Python interpreter directly instead of using the package name
- Resolves: rhbz#1633609

* Fri Jun 22 2018 Charalampos Stratakis <cstratak@redhat.com> - 0.5.1-5
- Conditionalize the python2 subpackage

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jul 25 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 0.5.1-2
- Set the PYTHONPATH when building docs so the library is found.

* Tue Jul 25 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 0.5.1-1
- Initial release
