# Inmanta Service Orchestrator official container image

# Build
The build uses the rpm released on cloudsmith.  
The build command takes a few parameters:
 - `PRODUCT_REPO_TOKEN`: a token which allows to reach the cloudsmith artifacts.
 - `MAJOR_VERSION`: the major version we want to build a container for (e.g. `5`)
 - `VERSION`: the full version we want to build a container for (e.g. `5.0.2.dev`)
 - `BUILD_TYPE`: the release we want to build a container for (e.g. `dev`)
 - `BUILD_DATE`: the date at which we triggered the build

Building the container by hand is as simple as:
```
docker build \
    --build-arg MAJOR_VERSION=$MAJOR_VERSION \
    --build-arg VERSION=$VERSION \
    --build-arg BUILD_TYPE=$BUILD_TYPE \
    --build-arg BUILD_DATE="$(date -uR)" \
    --build-arg PRODUCT_REPO_TOKEN=$PRODUCT_REPO_TOKEN \
    -f Dockerfile \
    -t iso$MAJOR_VERSION:$BUILD_TYPE \
    .
```

# Run the container
The container can be run using the simple `docker-compose.yml` file below:
```yaml
version: '3'
services:
    postgres:
        container_name: iso_postgres
        image: postgres:10
        environment:
            POSTGRES_USER: inmanta
            POSTGRES_PASSWORD: inmanta
        networks:
            iso_net:
                ipv4_address: 172.30.0.2

    inmanta-server:
        container_name: iso_server
        image: iso5:stable
        ports:
            - 8888:80
        volumes:
            - ./resources/dev.inmanta.com.license:/etc/inmanta/license/.license
            - ./resources/dev.inmanta.com.jwe:/etc/inmanta/license/.jwe
        depends_on:
            - postgres
        networks:
            iso_net:
                ipv4_address: 172.30.0.3

networks:
    iso_net:
        ipam:
            driver: default
            config:
                - subnet: 172.30.0.0/16

```
To start it, simply run the following command:
```
docker-compose up
```

## Configure the server

By default the server will use this [configuration file](resources/server.cfg).  If you want to change it, you can copy this file, edit it, then mount it in the container, where the default file is currently located: `/etc/inmanta/inmanta.cfg`.

If you use docker-compose, you can simply update this section of the example above:
```yaml
    inmanta-server:
        container_name: iso_server
        image: iso5:stable
        ports:
            - 8888:80
        volumes:
            - ./resources/dev.inmanta.com.license:/etc/inmanta/license/.license
            - ./resources/dev.inmanta.com.jwe:/etc/inmanta/license/.jwe
            - ./resources/my-server-conf.cfg:/etc/inmanta/inmanta.cfg
```
