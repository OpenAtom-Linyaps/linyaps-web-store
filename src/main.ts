// SPDX-FileCopyrightText: 2023 UnionTech Software Technology Co., Ltd.
//
// SPDX-License-Identifier: LGPL-3.0-or-later

import { createApp } from 'vue';

import '@element-plus/theme-chalk/dist/index.css';

import VueGtag from 'vue-gtag-next';
import App from './App.vue';

const app = createApp(App);
app.use(VueGtag, {
  property: { id: 'G-JBPRYNBJZ7' },
});
app.mount('#app');
