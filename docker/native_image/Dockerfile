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

# Copy files from buildcontext
COPY product/LICENSE /usr/share/doc/inmanta-oss/
COPY inmanta-core/misc/inmanta.cfg /etc/inmanta/
COPY inmanta-core/misc/inmanta-workon-register.sh /var/lib/inmanta/.inmanta/
COPY inmanta-web-console-*.tgz /usr/share/inmanta/web-console/
RUN python${PYTHON_VERSION_INMANTA_VENV} -m venv /opt/inmanta
RUN <<EOF
# Create venv
python${PYTHON_VERSION_INMANTA_VENV} -m venv /opt/inmanta
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
# Install inmanta config files
cat <<EXTENSION_EOF > /etc/inmanta/inmanta.d/extensions.cfg
[server]
enabled_extensions=ui
EXTENSION_EOF
# Install web-console
tar -xf /usr/share/inmanta/web-console/inmanta-web-console-*.tgz --strip-components=2 --directory /usr/share/inmanta/web-console
rm -f /usr/share/inmanta/web-console/inmanta-web-console-*.tgz
# Create inmanta group
groupadd -r -g 999 inmanta
# Create inmanta user
useradd -r -g inmanta -u 999 -d /var/lib/inmanta -s /bin/bash -c "Account used by the Inmanta daemons" inmanta
# Make sure that the inmanta-workon-register.sh script is sourced when a bash shell is started
echo "source /var/lib/inmanta/.inmanta/inmanta-workon-register.sh" >> /var/lib/inmanta/.bashrc
# Make the inmanta user the owner of the state and log directory
for path in /var/lib/inmanta /var/log/inmanta
do
  chown -R inmanta:inmanta "${path}"
done
EOF

# Run the container using the inmanta user and group
USER inmanta:inmanta

# Document default exposed port
EXPOSE 8888

# Change the workdir to the HOME directory of the inmanta user
WORKDIR /var/lib/inmanta

ENTRYPOINT ["/usr/bin/inmanta"]
CMD ["--log-file", "/var/log/inmanta/server.log", "--log-file-level", "2", "--timed-logs", "server", "--db-wait-time", "15"]
