# Created by pyp2rpm-3.3.2
%global pypi_name pulp_file

Name:           python-%{pypi_name}
Version:        0.0.1b9
Release:        1%{?dist}
Summary:        File plugin for the Pulp Project

License:        GPLv2+
URL:            http://www.pulpproject.org/
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/pulp-file-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(pulpcore-plugin) = 0.1.0b21
BuildRequires:  python3dist(setuptools)

%description
pulp_file Plugin This is the pulp_file Plugin for Pulp Project 3.0+ < This
plugin replaces the ISO support in the pulp_rpm plugin for Pulp 2. This plugin
uses the ChangeSet API < to add and remove content from a repository.All REST
API examples bellow use httpie < to perform the requests. The httpie commands
below assume that the user executing the commands has a .netrc file in the
home...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:       python3dist(pulpcore-plugin) = 0.1.0b21
Requires:       python3dist(setuptools)
%description -n python3-%{pypi_name}
pulp_file Plugin This is the pulp_file Plugin for Pulp Project 3.0+ < This
plugin replaces the ISO support in the pulp_rpm plugin for Pulp 2. This plugin
uses the ChangeSet API < to add and remove content from a repository.All REST
API examples bellow use httpie < to perform the requests. The httpie commands
below assume that the user executing the commands has a .netrc file in the
home...


%prep
%autosetup -n pulp-file-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Tue Mar 26 2019 Mike DePaulo <mikedep333@redhat.com> - 0.0.1b9-1
- Initial package.