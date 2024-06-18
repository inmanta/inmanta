# Expected content of the build directory:
# * NPM package containing the web-console.
# * A checkout of the inmanta_core repository in a directory called inmanta_core.
ARG PYTHON_VERSION
FROM python:${PYTHON_VERSION}-bookworm

ARG PYTHON_VERSION
ARG VERSION
ARG BUILD_TYPE
ARG BUILD_DATE
ARG PIP_INDEX_URL
ARG PRODUCT_VERSION_CONSTRAINT_FOR_PIP

LABEL com.inmanta.version=$VERSION
LABEL com.inmanta.description="Inmanta OSS (OSS-${BUILD_TYPE})"
LABEL com.inmanta.build-type=$BUILD_TYPE
LABEL com.inmanta.build-date=$BUILD_DATE

# Create inmanta directories
RUN mkdir -p /var/lib/inmanta /var/log/inmanta /etc/inmanta/inmanta.d /usr/share/inmanta/web-console /etc/profile.d/ /usr/share/doc/inmanta-oss

RUN apt-get -y update \
    && apt-get -y install git \
                          libffi8 \
                          libffi-dev \
                          which \
                          gcc \
                          cargo \
                          openssl \
    && apt-get clean

# Create build directory
RUN --mount=type=bind,source=.,target=/inmanta_build_dir <<EOF
cd /inmanta_build_dir
# Install LICENSE file
install -p -m 644 inmanta-core/LICENSE /usr/share/doc/inmanta-oss/LICENSE
# Create venv
python${PYTHON_VERSION} -m venv /opt/inmanta
# Install build dependencies
/opt/inmanta/bin/pip install -U wheel setuptools pip
# Install product
if [ "${BUILD_TYPE}" == "stable" ]; then
    PIP_ARGS=""
else
    PIP_ARGS="--pre"
fi
/opt/inmanta/bin/pip install ${PIP_ARGS} ${PRODUCT_VERSION_CONSTRAINT_FOR_PIP}
# Install files required by compiler
/opt/inmanta/bin/python -m inmanta.app
# Add symlinks to venv binaries in /usr/bin
ln -s /opt/inmanta/bin/inmanta /usr/bin/inmanta && ln -s /opt/inmanta/bin/inmanta-cli /usr/bin/inmanta-cli
# Install inmanta-workon
install -p -m 644 inmanta-core/misc/inmanta-workon-register.sh /etc/profile.d/inmanta-workon-register.sh
# Install inmanta config files
install -p -m 644 inmanta-core/misc/inmanta.cfg /etc/inmanta/inmanta.cfg
cat <<EXTENSION_EOF > /etc/inmanta/inmanta.d/extensions.cfg
[server]
enabled_extensions=ui
EXTENSION_EOF
# Install web-console
tar -xf inmanta-web-console-*.tgz --strip-components=2 --directory /usr/share/inmanta/web-console
# Create inmanta group
groupadd -r inmanta
# Create inmanta user
useradd -r -g inmanta -d /var/lib/inmanta -s /bin/bash -c "Account used by the Inmanta daemons" inmanta
EOF

# Run the container using the inmanta user and group
USER inmanta:inmanta

# Document default exposed port
EXPOSE 8888

# Change the workdir to the HOME directory of the inmanta user
WORKDIR /var/lib/inmanta
