#!/usr/bin/env bash

set -eux

# yarn --registry=http://registry-npm.sndu.cn/ install
NODE_OPTIONS=--openssl-legacy-provider yarn build  --mode hongkong
