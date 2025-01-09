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
ENV INMANTA_SERVER_BIND_PORT="8888"
ENV INMANTA_SERVER_BIND_ADDRESS="0.0.0.0"
ENV INMANTA_CONFIG_STATE_DIR="/var/lib/inmanta"
ENV INMANTA_CONFIG_LOG_DIR="/var/log/inmanta"
ENV INMANTA_SERVER_ENABLED_EXTENSIONS="ui"

RUN --mount=type=bind,target=/inmanta_build_dir <<EOF
# Create required directories
mkdir -p /var/lib/inmanta /var/log/inmanta /usr/share/inmanta/web-console /usr/share/doc/inmanta-oss /etc/inmanta/{inmanta.d,logging}
# Copy files from build directory
cp /inmanta_build_dir/product/LICENSE /usr/share/doc/inmanta-oss/
cp /inmanta_build_dir/inmanta-core/misc/inmanta-workon-register.sh /usr/bin/
# Add logging configuration
cp /inmanta_build_dir/inmanta-core/misc/server_log_container.yml /etc/inmanta/logging/server.yml
cat <<EOF2 >/etc/inmanta/inmanta.d/logging.cfg
[logging]
server = /etc/inmanta/logging/server.yml
EOF2
# Install packages
apt-get -y update
apt-get -y install git \
                   libffi8 \
                   libffi-dev \
                   which \
                   gcc \
                   cargo \
                   openssl \
                   tini
apt-get clean
# Create venv
python${PYTHON_VERSION_INMANTA_VENV} -m venv /opt/inmanta
# Install build dependencies
# Disable the cache directory to prevent making the image bigger than required.
/opt/inmanta/bin/pip install --no-cache-dir -U wheel setuptools pip
# Install product
if [ -e /inmanta_build_dir/product/requirements.txt ]; then
    # Take product constraint file into account to allow repeatable builds.
    MIN_C_OPTION="-c /inmanta_build_dir/product/requirements.txt"
else
    MIN_C_OPTION=""
fi
# Disable the cache directory to prevent making the image bigger than required.
/opt/inmanta/bin/pip install --no-cache-dir ${MIN_C_OPTION} ${PRODUCT_VERSION_CONSTRAINT_FOR_PIP}
# Install files required by compiler
/opt/inmanta/bin/python -m inmanta.app
# Add symlinks to venv binaries in /usr/bin
ln -s /opt/inmanta/bin/inmanta /usr/bin/inmanta
ln -s /opt/inmanta/bin/inmanta-cli /usr/bin/inmanta-cli
# Install web-console
tar -xf /inmanta_build_dir/inmanta-web-console-*.tgz --strip-components=2 --directory /usr/share/inmanta/web-console
# Create inmanta group
groupadd -r -g 995 inmanta
# Create inmanta user
useradd -r -g inmanta -u 997 -d /var/lib/inmanta -s /bin/bash -c "Account used by the Inmanta daemons" inmanta
# Make sure that the inmanta-workon-register.sh script is sourced when a bash shell is started
echo "source /usr/bin/inmanta-workon-register.sh" >> /etc/bash.bashrc
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

# Configure a healthcheck which validates that the api is responsive
HEALTHCHECK --interval=10s --timeout=3s --start-period=5m --start-interval=5s --retries=3 \
    CMD /opt/inmanta/bin/python -c "from inmanta import config as c, protocol as p; c.Config.load_config(config_dir='/etc/inmanta/inmanta.d'); r = p.SyncClient('client').get_server_status(); assert r.code == 200 and {s['name']: s for s in r.result['data']['slices']}['core.database']['status']['connected'], str(r.result)"

ENTRYPOINT ["/usr/bin/tini", "--", "/usr/bin/inmanta"]
CMD ["--log-file", "/var/log/inmanta/server.log", "--log-file-level", "INFO", "--timed-logs", "server", "--db-wait-time", "15"]
