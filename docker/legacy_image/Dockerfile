# The format of the EL_VERSION argument is a single number, for example: 9
# This argument is set by IRT.
ARG EL_VERSION
# The format of the PYTHON_VERSION argument is a non-dotted python version, for example 311
# This argument is set by IRT.
ARG PYTHON_VERSION

FROM registry.access.redhat.com/ubi${EL_VERSION}/python-${PYTHON_VERSION}:latest

# We need to be root to setup the container image
USER 0

# Install required packages and setup ssh
RUN yum install -y yum-utils openssh-server git sudo nc

# Create the Inmanta user and group and pin the uid and gid to a specific value.
# We do this here, because otherwise the RPM will create the user and group instead.
RUN groupadd -r -g 995 inmanta && \
    useradd -r -g inmanta -G wheel -u 997 -d /var/lib/inmanta -s /usr/bin/bash -c "Account used by the Inmanta daemons" inmanta

# Installing iso from rpm
ARG BUILD_TYPE
ARG EL_VERSION=8
RUN curl -1sLf "https://packages.inmanta.com/public/oss-$BUILD_TYPE/config.rpm.txt?distro=el&codename=$EL_VERSION" \
	> "/tmp/inmanta-oss.repo" && \
	yum-config-manager --add-repo '/tmp/inmanta-oss.repo' && \
	yum -q makecache -y --disablerepo='*' --enablerepo="inmanta-oss-${BUILD_TYPE}" && \
	yum install -y inmanta-oss inmanta-oss-server && \
	yum clean all && \
	rm /etc/yum.repos.d/inmanta-oss.repo && \
	rm /tmp/inmanta-oss.repo

# Overwriting container entrypoint with our own file
COPY resources/container-entrypoint-with-env /container-entrypoint-with-env

# Ensure that environment variables are loaded
COPY resources/profile /etc/profile.d/inmanta.sh

# Change the default shell of the inmanta user, to use a script loading env var from a file first
RUN echo "%wheel ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers && \
	chmod 755 /container-entrypoint-with-env && \
	chown root:root /container-entrypoint-with-env

# Overwrite the default config we received from the rpm with our own
COPY resources/default-server-config.cfg /etc/inmanta/inmanta.cfg

# Adding label to the recently built container
ARG VERSION
ARG BUILD_DATE
LABEL com.inmanta.version=$VERSION \
	com.inmanta.description="Inmanta OSS (OSS-${BUILD_TYPE})" \
	com.inmanta.build-type=$BUILD_TYPE \
	com.inmanta.build-date=$BUILD_DATE

# Document default exposed port
EXPOSE 8888

# Overwriting the entry point of ubi8 with our own
ENTRYPOINT ["/container-entrypoint-with-env"]

CMD ["server"]
