<template>
  <div id="main">
    <div id="topbar">
      <el-button round type="danger" size="small" @click="gotoLink()"> Get Linglong </el-button>
    </div>
    <div id="card-gird" v-loading="dataLoadingFlag">
      <div v-for="item in appList" :key="item.appId">
        <AppCard v-if="true" :imageURI="item.icon" :name="item.name" :id="item.appId" :description="item.description">
        </AppCard>
      </div>
    </div>
    <div id="page-next">
      <span class="demonstration"></span>
      <el-pagination
      @current-change="nextClick"
      background layout="prev, pager, next"
      :page-size="size"
      :total="total">
      </el-pagination>
    </div>
  </div>
  <br>
</template>

<script lang="ts">
import { defineComponent, ref, onMounted } from 'vue';
import AppCard from './AppCard.vue';
import axios from 'axios';

export default defineComponent({
  name: 'Main',
  components: {
    AppCard,
  },
  data() {
    return {
    }
  },
  methods: {
    gotoLink() {
      window.open(`${process.env.VUE_APP_HOME_PAGE_URL}/guide/start/install.html`)
    }
  },
  setup() {
    const appList = ref([])
    const dataLoadingFlag = ref()
    const total = ref()
    const size = 20
    const service = axios.create({
      baseURL: process.env.VUE_APP_AXIOS_BASEURL, // url = base url + request url
      timeout: 10000, // request timeout
    })
    const getList = (pageIndex = 1, pageSize = size) => {
      dataLoadingFlag.value = true
      service.post('/apps/webstore', {
        pageSize,        // 参数 firstName
        page:pageIndex,   // 参数 lastName
      }).then(function (response) {
        appList.value = response.data.data.list
        total.value = response.data.data.total
        dataLoadingFlag.value = false
      }).catch(function (error) {
        console.log(error);
      });
    }
    onMounted(() => getList());
    return {
      appList,
      total,
      size,
      dataLoadingFlag,
      nextClick(pageIndex) {
        console.log(pageIndex);
        getList(pageIndex)
      },
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
  grid-template-columns: repeat(auto-fit, 320px);
  gap: 2em;
  align-items: center;
  justify-content: center;
  text-align: center;
}

#page-next {
  margin-left: auto;
  margin-right: auto;
}
</style>
