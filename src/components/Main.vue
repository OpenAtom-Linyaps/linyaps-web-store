<template>
  <el-dialog v-model="isMarkdownPreviewShow">
    <MarkdownPreview :source="source" />
  </el-dialog>

  <div id="main">
    <div id="topbar">
      <el-button round type="danger" size="small" @click="isMarkdownPreviewShow = true"> 获取玲珑
      </el-button>
      <!-- <label>Linglong Space</label> -->
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
      <div v-for="item in appList" :key="item.appId">
        <AppCard v-if="true" :imageURI="item.icon" :name="item.name" :id="item.appId"> </AppCard>
      </div>
    </div>
    <div id="page-next">
      <span class="demonstration"></span>
      <el-pagination @current-change="nextClick" background layout="prev, pager, next" :total="1000">
      </el-pagination>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, onMounted } from 'vue';
import AppCard from './AppCard.vue';
import MarkdownPreview from './MarkdownPreview.vue';
// import appInfoJSON from './appinfo.json';
import axios from 'axios';

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

### [Click here to install linglong environment.](${process.env.VUE_APP_HOME_PAGE_URL}/guide/start/install.html)
      `,
    };
  },
  methods: {
  },
  setup() {
    const appList = ref([]);
    const service = axios.create({
      baseURL: process.env.VUE_APP_AXIOS_BASEURL, // url = base url + request url
      timeout: 10000, // request timeout
    })
    const getList = (pageIndex = 1, limit = 20) => {
      const offset = limit * (pageIndex - 1)
      service.post('/apps/webstore', {
        limit,        // 参数 firstName
        offset,   // 参数 lastName
      })
        .then(function (response) {
          console.log(response.data.data);
          appList.value = response.data.data
        })
        .catch(function (error) {
          console.log(error);
        });
    }
    onMounted(() => getList());
    return {
      appList,
      nextClick(pageIndex) {
        console.log(pageIndex);
        getList(pageIndex)
      }
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

#topbar>.el-input {
  width: 300px;
  padding-right: 10px;
}

#topbar> :nth-child(1) {
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

#page-next {
  margin-left: auto;
  margin-right: auto;
}
</style>
