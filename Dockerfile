# SPDX-FileCopyrightText: 2017 - 2022 UnionTech Software Technology Co., Ltd.
#
# SPDX-License-Identifier: LGPL-3.0-or-later

FROM hub.deepin.com/library/nginx:latest
COPY ./dist/ /usr/share/nginx/html
