FROM registry.access.redhat.com/ubi8/python-39:latest

# We need to be root to setup the container image
USER 0

# Install required packages and setup ssh
RUN yum install -y yum-utils openssh-server git sudo curl && \
	sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd && \
	ssh-keygen -t rsa -f /etc/ssh/ssh_host_rsa_key -N '' && \
	ssh-keygen -t dsa -f /etc/ssh/ssh_host_dsa_key -N ''

# Copying default config files and inmanta user login shell
COPY resources/shell-with-env /usr/bin/shell-with-env
COPY resources/server.cfg /etc/inmanta/inmanta.cfg

# Installing iso from rpm
ARG BUILD_TYPE
ARG PRODUCT_REPO_TOKEN
RUN curl -1sLf "https://packages.inmanta.com/public/oss-$BUILD_TYPE/config.rpm.txt?distro=el&codename=8" \
	> "/tmp/inmanta-oss.repo" && \
	yum-config-manager --add-repo '/tmp/inmanta-oss.repo' && \
	yum -q makecache -y --disablerepo='*' --enablerepo="inmanta-oss-${BUILD_TYPE}" && \
	yum install -y inmanta-oss inmanta-oss-server && \
	yum clean all && \
	rm /etc/yum.repos.d/inmanta-oss.repo && \
	rm /tmp/inmanta-inmanta-service-orchestrator.repo

# Change the default shell of the inmanta user, to use a script loading env var from a file first
RUN echo "%wheel ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers && \
	usermod -aG wheel inmanta && \
	usermod -s /usr/bin/shell-with-env inmanta && \
	chmod 755 /usr/bin/shell-with-env && \
	chown root:root /usr/bin/shell-with-env

# Adding label to the recently built container
ARG VERSION
ARG BUILD_DATE
LABEL com.inmanta.version=$VERSION \
    com.inmanta.description="Inmanta OSS (OSS-${BUILD_TYPE})" \
    com.inmanta.build-type=$BUILD_TYPE \
	com.inmanta.build-date=$BUILD_DATE

# By default we want to execute process in the container as the inmanta user
USER inmanta

# Overwriting the entry point of ubi8 with our own
ENTRYPOINT ["/usr/bin/shell-with-env", "-c"]

CMD ["/usr/bin/inmanta -vvv --timed-logs server"]
