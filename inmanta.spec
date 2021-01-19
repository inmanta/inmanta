# Provide: dashboard_version  and inmanta_core_version to mock command via --define
# Example --define="dashboard_version 1.0.0" --define="inmanta_core_version 4.1.0.dev0"

# Use release 1 for stable releases
%define release 0
%define version 2020.7
%define buildid %{nil}
%define buildid_egg %{nil}
%define python_version 3.6
%define undotted_python_version %(v=%{python_version}; echo "${v//\./}")
%define venv %{buildroot}/opt/inmanta
%define _p3 %{venv}/bin/python%{python_version}
%define _unique_build_ids 0
%define _debugsource_packages 0
%define _debuginfo_subpackages 0
%define _enable_debug_packages 0
%define debug_package %{nil}

%define sourceversion %{version}%{?buildid}
%define sourceversion_egg %{version}%{?buildid_egg}
%define inmanta_core_dir inmanta-core-%{inmanta_core_version}

Name:           inmanta-oss
Version:        %{version}

Release:        %{release}%{?buildid}%{?tag}%{?dist}
Summary:        Inmanta automation and orchestration tool

Group:          Development/Languages
License:        ASL 2
URL:            http://inmanta.com
Source0:        inmanta-%{sourceversion_egg}.tar.gz
Source1:        dependencies.tar.gz
Source2:        inmanta-inmanta-dashboard-%{dashboard_version}.tgz
Source3:        inmanta-core-%{inmanta_core_version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  systemd
BuildRequires:  sed
BuildRequires:  libffi-devel

Requires:       git
Requires:       gcc
Requires:       logrotate
Requires:       libffi
Requires(pre):  shadow-utils

%if 0%{?el7}
BuildRequires:  openssl11-devel
Requires:       openssl11
%else
BuildRequires:  openssl-devel >= 1:1.1.1
Requires:       openssl >= 1:1.1.1
%endif

BuildRequires:  python%{undotted_python_version}-devel
Requires:       python%{undotted_python_version}
Requires:       python%{undotted_python_version}-devel

Obsoletes: python3-inmanta
Obsoletes: python3-inmanta-core

%define __python3 /usr/bin/python%{python_version}

%package -n inmanta-oss-server
Summary:        The configuration and service files to start the Inmanta server
Requires:       inmanta-oss
Obsoletes:      python3-inmanta-server

%package -n inmanta-oss-agent
Summary:        The configuration and service files to start the Inmanta agent
Requires:       inmanta-oss
Obsoletes:      python3-inmanta-agent

%description

%description -n inmanta-oss-server

%description -n inmanta-oss-agent

%prep
%setup -q -n inmanta-%{sourceversion_egg}
%setup -T -D -a 1 -n inmanta-%{sourceversion_egg}
%setup -T -D -a 2 -n inmanta-%{sourceversion_egg}
%setup -T -D -a 3 -n inmanta-%{sourceversion_egg}
cp ${RPM_SOURCE_DIR}/inmanta-core-%{inmanta_core_version}.tar.gz ${RPM_BUILD_DIR}/inmanta-%{sourceversion_egg}/dependencies

%build

%install

%if 0%{?el7}
export CFLAGS=$(pkg-config --cflags-only-I openssl11)
export LDFLAGS=$(pkg-config --libs-only-L openssl11)
%endif

rm -rf %{buildroot}
mkdir -p %{buildroot}/opt/inmanta
%{__python3} -m venv --symlinks %{venv}
%{_p3} -m pip install -U --no-index --find-links dependencies wheel setuptools pip
%{_p3} -m pip install --no-index --find-links dependencies .
%{_p3} -m inmanta.app

# Use the correct python for bycompiling
%define __python %{_p3}

# Fix shebang
find %{venv}/bin/ -type f | xargs sed -i "s|%{buildroot}||g"
find %{venv} -name RECORD | xargs sed -i "s|%{buildroot}||g"

# Make sure we use the correct python version and don't have dangeling symlink
ln -sf /usr/bin/python%{python_version} %{venv}/bin/python3

# Put symlinks
mkdir -p %{buildroot}%{_bindir}
ln -s /opt/inmanta/bin/inmanta %{buildroot}%{_bindir}/inmanta
ln -s /opt/inmanta/bin/inmanta-cli %{buildroot}%{_bindir}/inmanta-cli

# Additional dirs and config
chmod -x LICENSE
mkdir -p %{buildroot}%{_localstatedir}/lib/inmanta
mkdir -p %{buildroot}/etc/inmanta
mkdir -p %{buildroot}/etc/inmanta/inmanta.d
mkdir -p %{buildroot}/var/log/inmanta
mkdir -p %{buildroot}/etc/logrotate.d
install -p -m 644 %{inmanta_core_dir}/misc/inmanta.cfg %{buildroot}/etc/inmanta/inmanta.cfg
install -p -m 644 %{inmanta_core_dir}/misc/logrotation_config %{buildroot}/etc/logrotate.d/inmanta

# Setup systemd
mkdir -p %{buildroot}%{_unitdir}
install -p -m 644 %{inmanta_core_dir}/misc/inmanta-agent.service $RPM_BUILD_ROOT%{_unitdir}/inmanta-agent.service
install -p -m 644 %{inmanta_core_dir}/misc/inmanta-server.service $RPM_BUILD_ROOT%{_unitdir}/inmanta-server.service
mkdir -p %{buildroot}/etc/sysconfig
touch %{buildroot}/etc/sysconfig/inmanta-server
touch %{buildroot}/etc/sysconfig/inmanta-agent

# Install the dashboard
cp -a package/dist %{venv}/dashboard

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc LICENSE %{inmanta_core_dir}/docs/*
/opt/inmanta/bin
/opt/inmanta/lib
/opt/inmanta/lib64
/opt/inmanta/include
/opt/inmanta/pyvenv.cfg
%{_bindir}/inmanta
%{_bindir}/inmanta-cli
%attr(-, inmanta, inmanta) %{_localstatedir}/lib/inmanta
%attr(-, inmanta, inmanta) /var/log/inmanta
%config %attr(-, root, root)/etc/inmanta
%config(noreplace) %attr(-, root, root)/etc/inmanta/inmanta.cfg
%config %attr(-, root, root)/etc/inmanta/inmanta.d
%config(noreplace) %attr(-, root, root)/etc/logrotate.d/inmanta
%config(noreplace) %attr(-, root, root)/etc/sysconfig/inmanta-server
%config(noreplace) %attr(-, root, root)/etc/sysconfig/inmanta-agent

%files -n inmanta-oss-server
/opt/inmanta/dashboard
%attr(-,root,root) %{_unitdir}/inmanta-server.service

%files -n inmanta-oss-agent
%attr(-,root,root) %{_unitdir}/inmanta-agent.service

%post -n inmanta-oss-agent
%systemd_post inmanta-agent.service

%preun -n inmanta-oss-agent
%systemd_preun inmanta-agent.service

%postun -n inmanta-oss-agent
%systemd_postun_with_restart inmanta-agent.service

%post -n inmanta-oss-server
%systemd_post inmanta-server.service

# Move server.cfg file for backward compatibility
if [ -e "/etc/inmanta/server.cfg" ]; then
  mv /etc/inmanta/server.cfg /etc/inmanta/inmanta.d/
fi

%preun -n inmanta-oss-server
%systemd_preun inmanta-server.service

%postun -n inmanta-oss-server
%systemd_postun_with_restart inmanta-server.service

%pre
getent group inmanta >/dev/null || groupadd -r inmanta
getent passwd inmanta >/dev/null || \
    useradd -r -g inmanta -d /var/lib/inmanta -s /bin/bash \
    -c "Account used by the Inmanta daemons" inmanta
exit

%changelog
* Mon Jan 18 2021 Arnaud Schoonjans <arnaud.schoonjans@inmanta.com> - 2016.3
- Initial commit

