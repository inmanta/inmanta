# Use release 0 for prerelease version.
%define release 0
%define version 2020.6
%define buildid .dev202012211003
%define buildid_egg .dev202012211003
%define venv inmanta-venv
%define _p3 %{venv}/bin/python3
%define _unique_build_ids 0
%define _debugsource_packages 0
%define _debuginfo_subpackages 0
%define _enable_debug_packages 0
%define debug_package %{nil}

%define sourceversion %{version}%{?buildid}
%define sourceversion_egg %{version}%{?buildid_egg}

Name:           python3-inmanta
Version:        %{version}

Release:        %{release}%{?buildid}%{?tag}%{?dist}
Summary:        Inmanta Service Orchestrator

Group:          Development/Languages
License:        EULA
URL:            http://inmanta.com
Source0:        inmanta-%{sourceversion_egg}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  python3-inmanta-core
BuildRequires:  systemd

Requires:  python3-inmanta-core

# Use the correct python for bycompiling
%define __python %{_p3}

%description

%prep
%setup -q -n inmanta-%{sourceversion_egg}

%build

%install
# Copy the inmanta venv to BUILD directory to work around ownership issue
cp -r --no-preserve=ownership /opt/inmanta inmanta-venv
chmod -x LICENSE

site_packages_dir="inmanta-venv/lib/python3.6/site-packages"
files=$(find "${site_packages_dir}" -maxdepth 1 -mindepth 1)

# Install inmanta
%{_p3} -m pip install --no-index .

# Only keep new packages
rm -rf ${files}

mkdir -p %{buildroot}/opt/inmanta/
cp -r inmanta-venv/lib/ %{buildroot}/opt/inmanta/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc LICENSE
/opt/inmanta/lib/

%preun
# Stop and disable the inmanta-server service before this package is uninstalled
%systemd_preun inmanta-server.service

%postun
# Restart the inmanta-server service after an upgrade of this package
%systemd_postun_with_restart inmanta-server.service

%changelog
* Thu Dec 05 2019 Andras Kovari <bart.vanbrabant@inmanta.com> - 3.0.0
- Package version 3
