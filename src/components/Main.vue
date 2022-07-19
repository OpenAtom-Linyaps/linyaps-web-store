<template>
  <el-dialog v-model="isMarkdownPreviewShow">
    <MarkdownPreview :source="source" />
  </el-dialog>

  <div id="main">
    <div id="topbar">
      <el-button round type="danger" size="small" @click="isMarkdownPreviewShow = true"
        >Get Linglong
      </el-button>
      <label>Linglong Space</label>
      <!-- <el-input
        id="topbar-search"
        size="medium"
        maxlength="10"
        placeholder="enter serach keywords"
        prefix-icon="el-icon-search"
      >
      </el-input> -->
    </div>
    <div id="card-gird">
      <div v-for="item in appList" :key="item.id">
        <AppCard  v-if="item.isShow" :imageURI="item.imageURI" :name="item.name" :id="item.id"> </AppCard>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, onMounted } from 'vue';
import AppCard from './AppCard.vue';
import MarkdownPreview from './MarkdownPreview.vue';
import appInfoJSON from './appinfo.json';

export default defineComponent({
  name: 'Main',
  components: {
    AppCard,
    MarkdownPreview,
  },
  data() {
    return {
      isMarkdownPreviewShow: false,
      source: `
Install linglong tools by:
\`\`\`bash
http://10.20.52.176:32582/guide/start/install.html
\`\`\`
      `,
    };
  },
  methods: {},
  setup() {
    const appList = ref([]);
    onMounted(() => {
       appList.value = appInfoJSON.info.filter(function(item){
              return item.isShow
            });
    });
    return {
      appList,
    };
  },
});
</script>

<style scoped>
#main {
  display: flex;
  flex-direction: column;
  height: 100%;
  width: 100%;
}

#topbar {
  height: 60px;
  width: 100%;
  flex: 0 0 auto;
  border-bottom: 1px solid rgba(0, 0, 0, 0.1);
  background-color: #f9f9fa;

  align-items: center;
  display: flex;
  justify-content: space-between;
  flex-direction: row;
}

#topbar > .el-input {
  width: 300px;
  padding-right: 10px;
}

#topbar > :nth-child(1) {
  margin: 10px;
}

#card-gird {
  margin: 1% 5% 1% 5%;
  flex: 1 1 auto;

  display: grid;
  grid-template-columns: repeat(auto-fit, 226px);
  gap: 2em;
  align-items: center;

  justify-content: center;
}
</style>
