FROM registry.access.redhat.com/ubi8/python-39:latest

# We need to be root to setup the container image
USER 0

# Creating inmanta user
RUN echo "%wheel ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers && \
	useradd -G wheel -ms /bin/bash inmanta -d /var/lib/inmanta && \
	mkdir -p /var/lib/inmanta/.ssh

# Setting up common config
RUN yum install -y yum-utils openssh-server git sudo curl && \
	sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd && \
	ssh-keygen -t rsa -f /etc/ssh/ssh_host_rsa_key -N '' && \
	ssh-keygen -t dsa -f /etc/ssh/ssh_host_dsa_key -N ''

# Copying default config files
COPY resources/license.cfg /etc/inmanta/inmanta.d/license.cfg
COPY resources/server.cfg /etc/inmanta/inmanta.cfg

# Installing iso from rpm
ARG MAJOR_VERSION
ARG BUILD_TYPE
ARG PRODUCT_REPO_TOKEN
RUN curl -1sLf "https://packages.inmanta.com/oss-$BUILD_TYPE/config.rpm.txt?distro=el&codename=8" \
	> "/tmp/inmanta-oss.repo" && \
	yum-config-manager --add-repo '/tmp/inmanta-oss.repo' && \
	yum -q makecache -y --disablerepo='*' --enablerepo="inmanta-oss-${BUILD_TYPE}" && \
	yum install -y inmanta-oss inmanta-oss-server && \
	yum clean all && \
	rm /etc/yum.repos.d/inmanta-oss.repo && \
	rm /tmp/inmanta-oss.repo

# Adding label to the recently built container
ARG VERSION
ARG BUILD_DATE
LABEL com.inmanta.version=$VERSION \
    com.inmanta.description="Inmanta service orchestrator (OSS${MAJOR_VERSION}-${BUILD_TYPE})" \
    com.inmanta.build-type=$BUILD_TYPE \
	com.inmanta.build-date=$BUILD_DATE

# Overwriting the entry point of ubi8
ENTRYPOINT ["bash", "-c"]

CMD ["/usr/bin/inmanta", "-vvv", "server"]
