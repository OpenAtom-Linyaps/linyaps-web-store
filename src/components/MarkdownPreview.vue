<template>
  <div>
    <vue3-markdown-it :source="source" />
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import VueMarkdownIt from 'vue3-markdown-it';

export default defineComponent({
  name: 'MarkdownPreview',
  components: {
    'vue3-markdown-it': VueMarkdownIt,
  },
  props: {
    source: {
      type: String,
      default: '',
    },
  },
});
</script>

<style scoped></style>
