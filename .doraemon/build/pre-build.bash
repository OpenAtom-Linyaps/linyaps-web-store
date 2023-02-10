#!/usr/bin/env bash

set -eu

if [ "${NODE16_HOME}" != "" ]; then
  export PATH=${NODE16_HOME}/bin:$PATH
fi

yarn install
yarn build --mode hongkong
