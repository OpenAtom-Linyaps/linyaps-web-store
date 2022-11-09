#!/usr/bin/env bash
set -eux

tag=${1:?}

NODE_OPTIONS=--openssl-legacy-provider yarn build --mode proxy
docker buildx build --platform linux/amd64 --pull --push -t "hub.deepin.com/wuhan_v23_linglong/linglong-web-store:${tag}" .
