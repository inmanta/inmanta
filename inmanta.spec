# The following parameters have to be provided to mock via --define="<key> <value>"
#
# * release: Use release 1 for stable releases and 0 for pre-releases
# * version: Version of inmanta-service-orchestrator release (without build_tag)
# * buildid: Build_tag inmanta-oss RPM
# * buildid_egg: Build_tag inmanta pypi package
# * web_console_version: Fully qualified version web-console NPM package (version number + build_tag)
# * python_version: Create an RPM containing a venv for this python version. Only pass
#                   the version number. For example: "3.6", "3.9", etc.
# * pip_index: PIP index for package build

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
%define inmanta_rpm_state_dir %{_localstatedir}/lib/rpm-state/inmanta

Name:           inmanta-oss
Version:        %{version}

Release:        %{release}%{?buildid}%{?tag}%{?dist}
Summary:        Inmanta automation and orchestration tool

Group:          Development/Languages
License:        ASL 2
URL:            http://inmanta.com
Source0:        inmanta-%{sourceversion_egg}.tar.gz
Source1:        dependencies.tar.gz
Source3:        inmanta-web-console-%{web_console_version}.tgz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  systemd
BuildRequires:  sed
BuildRequires:  libffi-devel
Requires:       libffi-devel

Requires:       git
Requires:       logrotate
Requires:       libffi
Requires(pre):  shadow-utils
# for inmanta-workon
Requires:       which

# Requirements cryptography
BuildRequires:  redhat-rpm-config
Requires:       redhat-rpm-config
BuildRequires:  gcc
Requires:       gcc
BuildRequires:  cargo
Requires:       cargo
%if 0%{?el7}
BuildRequires:  openssl11-devel
Requires:       openssl11
%else
BuildRequires:  openssl-devel >= 1:1.1.1
Requires:       openssl >= 1:1.1.1
%endif

%if "%{#undotted_python_version}" == "2"
BuildRequires:  python%{undotted_python_version}-devel
Requires:       python%{undotted_python_version}
Requires:       python%{undotted_python_version}-devel
%else
BuildRequires:  python%{python_version}-devel
Requires:       python%{python_version}
Requires:       python%{python_version}-devel
%endif

Obsoletes: python3-inmanta
Obsoletes: python3-inmanta-core

%define __python3 /usr/bin/python%{python_version}

%package -n inmanta-oss-server
Summary:        The configuration and service files to start the Inmanta server
Requires:       inmanta-oss = %{version}-%{release}
Obsoletes:      python3-inmanta-server
Obsoletes:      inmanta-oss-agent

%description

%description -n inmanta-oss-server


%prep
%setup -q -n inmanta-%{sourceversion_egg}
%setup -T -D -a 1 -n inmanta-%{sourceversion_egg}
# Unpack inmanta-core
mkdir inmanta_core
tar -xf dependencies/inmanta_core-*.tar.gz --strip-components=1 --directory inmanta_core

%build

%install

%if 0%{?el7}
export CFLAGS=$(pkg-config --cflags-only-I openssl11)
export LDFLAGS=$(pkg-config --libs-only-L openssl11)
%endif

pre_opt=$([ -z "%{?buildid}" ] && echo "--pre" || echo "")
find_links_opt=$([ -d "dependencies" ] && echo "--find-links dependencies" || echo "")
index_url_opt=$([ -z "%{?pip_index}" ] && echo "--no-index" || echo '--index-url %{pip_index}')
requirements_file="dependencies/requirements.txt"
requirements_opt=$([ -f "${requirements_file}" ] && echo "-c ${requirements_file}" || echo "")

rm -rf %{buildroot}
mkdir -p %{buildroot}/opt/inmanta
%{__python3} -m venv --symlinks %{venv}
%{_p3} -m pip install -U ${index_url_opt} ${find_links_opt} ${requirements_opt} wheel setuptools pip
%{_p3} -m pip install ${pre_opt} ${index_url_opt} ${find_links_opt} ${requirements_opt} .
%{_p3} -m inmanta.app

# Use the correct python for bycompiling
%define __python %{_p3}

# Fix shebang
find %{venv}/bin/ -type f | xargs sed -i "s|%{buildroot}||g"
find %{venv} -name RECORD | xargs sed -i "s|%{buildroot}||g"

# Remove the shebang on the first line
if [ -e "%{venv}/lib/python%{python_version}/site-packages/google/protobuf/internal/_parameterized.py" ]; then
  sed -i "1d" %{venv}/lib/python%{python_version}/site-packages/google/protobuf/internal/_parameterized.py
fi

# Fix path in pyvenv.cfg file
sed -i "s|%{buildroot}||g" %{venv}/pyvenv.cfg

# Make sure we use the correct python version and don't have dangeling symlink
ln -sf /usr/bin/python%{python_version} %{venv}/bin/python3

# Put symlinks
mkdir -p %{buildroot}%{_bindir}
ln -s /opt/inmanta/bin/inmanta %{buildroot}%{_bindir}/inmanta
ln -s /opt/inmanta/bin/inmanta-cli %{buildroot}%{_bindir}/inmanta-cli

# Install inmanta-workon
mkdir -p %{buildroot}/%{_sysconfdir}/profile.d/
install -p -m 644 inmanta_core/misc/inmanta-workon-register.sh %{buildroot}/%{_sysconfdir}/profile.d/inmanta-workon-register.sh

# Additional dirs and config
chmod -x LICENSE
mkdir -p %{buildroot}%{_localstatedir}/lib/inmanta
mkdir -p %{buildroot}/etc/inmanta
mkdir -p %{buildroot}/etc/inmanta/inmanta.d
mkdir -p %{buildroot}/var/log/inmanta
mkdir -p %{buildroot}/etc/logrotate.d
install -p -m 644 inmanta_core/misc/inmanta.cfg %{buildroot}/etc/inmanta/inmanta.cfg
install -p -m 644 inmanta_core/misc/logrotation_config %{buildroot}/etc/logrotate.d/inmanta
cat <<EOF > %{buildroot}/etc/inmanta/inmanta.d/extensions.cfg
[server]
enabled_extensions=ui
EOF


# Setup systemd
mkdir -p %{buildroot}%{_unitdir}
install -p -m 644 inmanta_core/misc/inmanta-server.service $RPM_BUILD_ROOT%{_unitdir}/inmanta-server.service
mkdir -p %{buildroot}/etc/sysconfig
touch %{buildroot}/etc/sysconfig/inmanta-server


# Install web-console
mkdir -p %{buildroot}/usr/share/inmanta/web-console
tar -xf %{SOURCE3} --strip-components=2 --directory %{buildroot}/usr/share/inmanta/web-console

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc LICENSE
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
%config(noreplace) %attr(-, root, root)/etc/inmanta/inmanta.d/extensions.cfg
%config(noreplace) %attr(-, root, root)/etc/logrotate.d/inmanta
%config(noreplace) %attr(-, root, root)/etc/sysconfig/inmanta-server

%files -n inmanta-oss-server
/usr/share/inmanta/web-console
%{_sysconfdir}/profile.d/inmanta-workon-register.sh
%attr(-,root,root) %{_unitdir}/inmanta-server.service


# The save_service_state() and the restore_service_state() macros
# are required to make sure that the service state (enable/disabled,
# started/stopped) remains unchanged when migrating from the
# python3-inmanta-server and python3-inmanta-agent RPMs to the
# inmanta-oss-server and inmanta-oss-agent RPMs respectively.
%define save_service_state() \
if [ -e "%{_unitdir}/%{1}.service" ]; then \
  mkdir -p "%{inmanta_rpm_state_dir}" \
  if systemctl is-enabled -q %{1}.service; then \
    touch "%{inmanta_rpm_state_dir}/%{1}_enabled" \
  fi \
  if systemctl is-active -q %1.service; then \
    touch "%{inmanta_rpm_state_dir}/%{1}_active" \
  fi \
fi

%define restore_service_state() \
if [ -e "%{inmanta_rpm_state_dir}/%{1}_enabled" ] && ! systemctl is-enabled -q %{1}.service; then \
  systemctl enable %{1}.service \
fi \
if [ -e "%{inmanta_rpm_state_dir}/%{1}_active" ] && ! systemctl is-active -q %{1}.service; then \
  systemctl start %{1}.service \
fi \
rm -f "%{inmanta_rpm_state_dir}/%{1}_enabled" "%{inmanta_rpm_state_dir}/%{1}_active"


%pre -n inmanta-oss-server
%save_service_state inmanta-server

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

%posttrans -n inmanta-oss-server
%restore_service_state inmanta-server

%pre
getent group inmanta >/dev/null || groupadd -r inmanta
getent passwd inmanta >/dev/null || \
    useradd -r -g inmanta -d /var/lib/inmanta -s /bin/bash \
    -c "Account used by the Inmanta daemons" inmanta
exit

%changelog
* Fri Nov 29 2024 Wouter De Borger <wouter.deborger@inmanta.com> - 2024.5
- Remove inmanta-service-orchestrator-agent

* Tue Nov 29 2022 Sander Van Balen <sander.vanbalen@inmanta.com> - 2022.4
- Added which as a dependency

* Wed Nov 23 2022 Sander Van Balen <sander.vanbalen@inmanta.com> - 2022.4
- Packaged inmanta-workon-register.sh into /etc/profile.d

* Tue Jan 11 2022 Florent Lejoly <florent.lejoly@inmanta.com> - 2022.1
- Enable ui extension by default

* Tue Jan 11 2022 Arnaud Schoonjans <arnaud.schoonjans@inmanta.com> - 2022.1
- Make python_version of RPM venv configurable

* Thu Jan 06 2022 Sander Van Balen <sander.vanbalen@inmanta.com> - 2022.1
- Include inmanta-ui and web-console

* Mon Jan 18 2021 Arnaud Schoonjans <arnaud.schoonjans@inmanta.com> - 2016.3
- Initial commit

