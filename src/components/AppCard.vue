// SPDX-FileCopyrightText: 2017 - 2022 UnionTech Software Technology Co., Ltd.
//
// SPDX-License-Identifier: LGPL-3.0-or-later

<template>
  <div class="app-card" :title="description">
    <el-image style="width: auto; height: 160px" :src="imageURI"> </el-image>
    <div class="app-card-control">
      <span>
        {{ name }}
        <el-button type="default" class="install-button" size="small" @click="onInstall(id)" round>Install</el-button>
      </span>
    </div>
  </div>
  <el-dialog v-model="isMarkdownPreviewShow">
    <MarkdownPreview :source="source" />
  </el-dialog>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import MarkdownPreview from './MarkdownPreview.vue';

export default defineComponent({
  name: 'AppCard',
  components: {
    MarkdownPreview,
  },
  props: {
    name: {
      type: String,
      default: '',
    },
    id: {
      type: String,
      default: '',
    },
    imageURI: {
      type: String,
      default: '',
    },
    description: {
      type: String,
      default: '',
    }
  },
  data() {
    return {
      isMarkdownPreviewShow: false,
      source: `
**If NO \`Linglong Installer Dialog\` popup, you MUST install linglong first:**

### [Click here to install linglong environment.](${process.env.VUE_APP_HOME_PAGE_URL}/guide/start/install.html)
      `,
    };
  },
  methods: {
    onInstall(id) {
      window.location.href = 'og://' + id;
      this.isMarkdownPreviewShow = true;
    },
  },
});
</script>

<style scoped>
.app-card {
  width: 320px;
  height: 224px;
}

.app-card-control {
  display: flex;
  align-items: center;
  text-align: center;
  justify-content: center;
}

.app-card-control > .el-button {
  margin-left: auto;
}

.install-button {
  font-size: 12px;
  line-height: 1;
  font-weight: 700;
  letter-spacing: 0em;
  font-family: "SF Pro Text","SF Pro Icons","Helvetica Neue","Helvetica","Arial",sans-serif;
  border-radius: 18px;
  padding: 6px 14px;
  background-color: #f5f5f7;
  color: #0071e3;
}

</style>
