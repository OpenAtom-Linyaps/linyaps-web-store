<template>
  <div class="app-card">
    <el-image style="width: 226px; height: 140px" :src="imageURI"> </el-image>
    <div class="app-card-control">
      <a>{{ name }}</a>
      <el-button type="warning" size="small" @click="onInstall(id)">Install</el-button>
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
  },
  data() {
    return {
      isMarkdownPreviewShow: false,
      source: `
**If NO \`Linglong Installer Dialog\` popup, you MUST install linglong first:**

\`\`\`text
http://10.20.52.176:32582/guide/start/install.html
\`\`\`
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
  width: 226px;
  height: 200px;
}

.app-card-control {
  display: flex;
  align-items: center;
}

.app-card-control > .el-button {
  margin-left: auto;
}
</style>
