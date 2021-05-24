import { createApp } from 'vue';

import ElementPlus from 'element-plus';
import 'element-plus/lib/theme-chalk/index.css';

import VueMarkdownIt from 'vue3-markdown-it';
import 'highlight.js/styles/monokai.css';

import App from './App.vue';

const app = createApp(App);

app
  .use(ElementPlus)
  .use(VueMarkdownIt)
  .mount('#app');
