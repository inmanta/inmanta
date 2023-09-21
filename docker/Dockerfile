ARG EL_VERSION=8
ARG PYTHON_VERSION=39

FROM registry.access.redhat.com/ubi${EL_VERSION}/python-${PYTHON_VERSION}:latest

# We need to be root to setup the container image
USER 0

# Install required packages and setup ssh
RUN yum install -y yum-utils openssh-server git sudo curl nc

# Installing iso from rpm
ARG BUILD_TYPE
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
	usermod -aG wheel inmanta && \
	usermod -s /usr/bin/bash inmanta && \
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
