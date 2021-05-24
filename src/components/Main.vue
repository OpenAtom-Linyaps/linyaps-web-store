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
      <el-input
        id="topbar-search"
        size="medium"
        maxlength="10"
        placeholder="enter serach keywords"
        prefix-icon="el-icon-search"
      >
      </el-input>
    </div>
    <div id="card-gird">
      <div v-for="item in appList" :key="item.id">
        <AppCard :imageURI="item.imageURI" :name="item.name" :id="item.id"> </AppCard>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, onMounted } from 'vue';
import AppCard from './AppCard.vue';
import MarkdownPreview from './MarkdownPreview.vue';

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
curl https://sh.linglong.space | sh 
\`\`\`
      `,
    };
  },
  methods: {},
  setup() {
    const appList = ref([]);
    onMounted(() => {
      appList.value = [
        {
          id: 'com.qq.weixin.deepin',
          name: '微信',
          imageURI:
            'https://dstore-metadata.deepin.cn/images/deepin.com.wechat_cover_zh-CN_bc82a1b5.jpeg',
        },
        {
          id: 'cn.wps.wps-office',
          name: 'WPS Office 2019 For Linux',
          imageURI:
            'https://dstore-metadata.deepin.cn/images/wps-office_coverHD_zh-CN_fd6b8447.jpeg',
        },
        {
          id: 'com.qq.im.deepin',
          name: 'QQ',
          imageURI: 'https://dstore-metadata.deepin.cn/images/deepin.com.qq.im_cover_en-US.png',
        },
        {
          id: 'cn.google.chrome',
          name: 'Google Chrome',
          imageURI:
            'https://dstore-metadata.deepin.cn/images/google-chrome-stable_cover_zh-CN_c766e6da.jpeg',
        },
        {
          id: 'com.163.music',
          name: 'Netease Cloud Music',
          imageURI:
            'https://dstore-metadata.deepin.cn/images/netease-cloud-music_cover_zh-CN_088c14f3.jpeg',
        },
        {
          id: 'org.mozilla.firefox',
          name: 'Firefox',
          imageURI:
            'https://dstore-metadata.deepin.cn/images/firefox-dde_coverHD_en-US_197bc29e.jpeg',
        },
        {
          id: 'com.visualstudio.code',
          name: 'VS Code',
          imageURI: 'https://dstore-metadata.deepin.cn/images/code_coverHD_zh-CN_946f8495.jpeg',
        },
        {
          id: 'org.videolan.vlc',
          name: 'VLC',
          imageURI: 'https://dstore-metadata.deepin.cn/images/vlc_cover_en-US.jpg',
        },
        {
          id: 'com.baidu.baidunetdisk',
          name: 'Baidu Netdisk',
          imageURI: 'https://dstore-metadata.deepin.cn/images/deepin.com.baidu.pan_cover_en-US.png',
        },
        {
          id: 'com.xunlei.download',
          name: 'ThunderSpeed',
          imageURI:
            'https://dstore-metadata.deepin.cn/images/deepin.com.thunderspeed_cover_en-US.png',
        },
      ];
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
