Name:           syscontainer-build
Version:        0.0.3
Release:        1%{?dist}
Summary:        Simple toolbox for building system containers

License:        GPLv3+
URL:            https://github.com/ashcrow/syscontainer-build/
Source0:        https://github.com/ashcrow/syscontainer-build/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel, python3-setuptools
Requires:       python3-jinja2

%description
Simple toolbox for building system containers.


%prep
%autosetup -n %{name}-%{version}


%build
%{__python3} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python3} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT
# Force python3
sed -i 's|/usr/bin/env python|/usr/bin/python3|' $RPM_BUILD_ROOT%{python3_sitelib}/syscontainer_build/cli.py


%files
%license LICENSE COPYING
%doc README.md
%{python3_sitelib}/*
%{_bindir}/%{name}


%changelog
* Mon Apr 10 2017 Steve Milner <smilner@redhat.com> - 0.0.3-1
- Initial spec