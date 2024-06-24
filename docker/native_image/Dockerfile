# Expected files/directories in the build context:
# * NPM package containing the web-console.
# * A checkout of the inmanta-core repository in a directory called inmanta-core.
# * A checkout of the product repository in a directory called product
ARG PYTHON_VERSION_INMANTA_VENV
FROM python:${PYTHON_VERSION_INMANTA_VENV}-bookworm

ARG PYTHON_VERSION_INMANTA_VENV
ARG VERSION
ARG BUILD_TYPE
ARG BUILD_DATE
ARG PIP_INDEX_URL
ARG PRODUCT_VERSION_CONSTRAINT_FOR_PIP

LABEL com.inmanta.version=$VERSION
LABEL com.inmanta.description="Inmanta OSS (OSS-${BUILD_TYPE})"
LABEL com.inmanta.build-type=$BUILD_TYPE
LABEL com.inmanta.build-date=$BUILD_DATE

# Set the deploy and repair interval for backwards compatibility reasons.
# Their actual default values differ from the values set in the inmanta.cfg
# file of the RPM. Here we make sure we use the values from the inmanta.cfg file.
ENV INMANTA_CONFIG_DEPLOY_INTERVAL="600"
ENV INMANTA_CONFIG_REPAIR_INTERVAL="86400"
ENV INMANTA_CONFIG_STATE_DIR="/var/lib/inmanta"
ENV INMANTA_CONFIG_LOG_DIR="/var/log/inmanta"
ENV INMANTA_SERVER_ENABLED_EXTENSIONS="ui"

# Create inmanta directories
RUN mkdir -p /var/lib/inmanta /var/log/inmanta /etc/inmanta/inmanta.d /usr/share/inmanta/web-console /etc/profile.d/ /usr/share/doc/inmanta-oss

# Copy files from buildcontext
COPY product/LICENSE /usr/share/doc/inmanta-oss/
COPY inmanta-core/misc/inmanta-workon-register.sh /etc/
COPY inmanta-web-console-*.tgz /usr/share/inmanta/web-console/
RUN <<EOF
# Install packages
apt-get -y update
apt-get -y install git \
                   libffi8 \
                   libffi-dev \
                   which \
                   gcc \
                   cargo \
                   openssl
apt-get clean
# Create venv
python${PYTHON_VERSION_INMANTA_VENV} -m venv /opt/inmanta
# Install build dependencies
# Disable the cache directory to prevent making the image bigger than required.
/opt/inmanta/bin/pip install --no-cache-dir -U wheel setuptools pip
# Install product
# Disable the cache directory to prevent making the image bigger than required.
if [ "${BUILD_TYPE}" == "stable" ]; then
    PIP_ARGS=""
else
    PIP_ARGS="--pre"
fi
/opt/inmanta/bin/pip install --no-cache-dir ${PIP_ARGS} ${PRODUCT_VERSION_CONSTRAINT_FOR_PIP}
# Install files required by compiler
/opt/inmanta/bin/python -m inmanta.app
# Add symlinks to venv binaries in /usr/bin
ln -s /opt/inmanta/bin/inmanta /usr/bin/inmanta && ln -s /opt/inmanta/bin/inmanta-cli /usr/bin/inmanta-cli
# Install web-console
tar -xf /usr/share/inmanta/web-console/inmanta-web-console-*.tgz --strip-components=2 --directory /usr/share/inmanta/web-console
rm -f /usr/share/inmanta/web-console/inmanta-web-console-*.tgz
# Create inmanta group
groupadd -r -g 995 inmanta
# Create inmanta user
useradd -r -g inmanta -u 997 -d /var/lib/inmanta -s /bin/bash -c "Account used by the Inmanta daemons" inmanta
# Make sure that the inmanta-workon-register.sh script is sourced when a bash shell is started
echo "source /etc/inmanta-workon-register.sh" >> /etc/bash.bashrc
# Make the inmanta user the owner of the state and log directory
chown -R inmanta:inmanta /var/lib/inmanta /var/log/inmanta
EOF

# Run the container using the inmanta user and group
USER inmanta:inmanta

# Document default exposed port
EXPOSE 8888

# Make sure data is stored in a volume
VOLUME  ["/var/log/inmanta", "/var/lib/inmanta/"]

# Change the workdir to the HOME directory of the inmanta user
WORKDIR /var/lib/inmanta

ENTRYPOINT ["/usr/bin/inmanta"]
CMD ["--log-file", "/var/log/inmanta/server.log", "--log-file-level", "2", "--timed-logs", "server", "--db-wait-time", "15"]
