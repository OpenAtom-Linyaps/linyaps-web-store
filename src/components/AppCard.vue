<!-- 
SPDX-FileCopyrightText: 2017 - 2022 UnionTech Software Technology Co., Ltd. 
SPDX-License-Identifier: LGPL-3.0-or-later 
-->

<template>
  <div class="app-card" :title="description">
    <el-image class="app-logo" :src="imageURI">
      <template #error>
        <el-image class="app-logo" src="assets/application-x-executable.svg"> </el-image>
      </template>
    </el-image>
    <div class="app-card-control">
      <span>
        {{ name }}
        <el-button class="install-button" type="default" size="small" @click="onInstall(id)" round>INSTALL</el-button>
      </span>
    </div>
  </div>
  <el-dialog v-model="isInstallDialogShow">
    <div>
      <p>
        <strong>If NO <code>Linglong Installer Dialog</code> popup, you MUST install linglong
          first:</strong>
      </p>
      <h3>
        <a href="https://linglong.dev/guide/start/install.html">Click here to install linglong environment.</a>
      </h3>
    </div>
  </el-dialog>
</template>

<script lang="ts">
import { ElButton, ElDialog, ElImage } from 'element-plus';
import { defineComponent } from 'vue';
import { useGtag } from 'vue-gtag-next';

export default defineComponent({
  name: 'AppCard',
  components: {
    ElButton,
    ElDialog,
    ElImage,
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
    },
  },
  data() {
    return {
      isInstallDialogShow: false,
    };
  },
  methods: {
    onInstall(id: string) {
      console.log('install', id);
      window.location.href = 'og://' + id;
      this.isInstallDialogShow = true;
      // 记录安装按钮点击事件
      const { event } = useGtag();
      event('install', { event_label: id });
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

.app-card-control>.el-button {
  margin-left: auto;
}

.install-button {
  font-size: 12px;
  line-height: 1;
  font-weight: 700;
  letter-spacing: 0;
  font-family: 'SF Pro Text', 'SF Pro Icons', 'Helvetica Neue', 'Helvetica', 'Arial', sans-serif;
  border-radius: 18px;
  padding: 6px 14px;
  background-color: #f5f5f7;
  color: #0071e3;
}

.app-logo {
  width: 160px;
  height: 160px;
}
</style>
