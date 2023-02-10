// SPDX-FileCopyrightText: 2017 - 2022 UnionTech Software Technology Co., Ltd.
//
// SPDX-License-Identifier: LGPL-3.0-or-later

import { createApp } from 'vue';

import ElementPlus from 'element-plus';
import '@element-plus/theme-chalk/dist/index.css';

import VueMarkdownIt from 'vue3-markdown-it';
import 'highlight.js/styles/monokai.css';

import App from './App.vue';

createApp(App)
    .use(ElementPlus)
    .use(VueMarkdownIt)
    .mount('#app');
