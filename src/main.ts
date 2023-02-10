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
