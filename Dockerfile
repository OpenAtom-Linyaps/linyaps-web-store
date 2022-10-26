# SPDX-FileCopyrightText: 2017 - 2022 UnionTech Software Technology Co., Ltd.
#
# SPDX-License-Identifier: LGPL-3.0-or-later

FROM hub.deepin.com/library/node:16 AS builder
WORKDIR /linglong-web-store
COPY . .
RUN yarn --registry=http://registry-npm.sndu.cn/ install && yarn build

FROM hub.deepin.com/library/nginx:latest
COPY --from=builder /linglong-web-store/dist/ /usr/share/nginx/html