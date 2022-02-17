# Inmanta OSS official container image

## Build the image
The build uses the rpm released on cloudsmith.  
The build command takes a few parameters:
 - `PRODUCT_REPO_TOKEN`: a token which allows to reach the cloudsmith artifacts.
 - `VERSION`: the full version we want to build a container for (e.g. `2022.1.dev`)
 - `BUILD_TYPE`: the release we want to build a container for (e.g. `dev`)
 - `BUILD_DATE`: the date at which we triggered the build

Building the container by hand is as simple as:
```
docker build \
    --build-arg VERSION=$VERSION \
    --build-arg BUILD_TYPE=$BUILD_TYPE \
    --build-arg BUILD_DATE="$(date -uR)" \
    --build-arg PRODUCT_REPO_TOKEN=$PRODUCT_REPO_TOKEN \
    -f Dockerfile \
    -t iso$MAJOR_VERSION:$BUILD_TYPE \
    .
```
