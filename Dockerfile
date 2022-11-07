# SPDX-FileCopyrightText: 2017 - 2022 UnionTech Software Technology Co., Ltd.
#
# SPDX-License-Identifier: LGPL-3.0-or-later

FROM hub.deepin.com/library/node:16 AS builder
WORKDIR /src
COPY . .
RUN set -eux; \
    yarn install; \
    yarn build

FROM hub.deepin.com/library/nginx:latest
COPY --from=builder /src/dist/ /usr/share/nginx/html