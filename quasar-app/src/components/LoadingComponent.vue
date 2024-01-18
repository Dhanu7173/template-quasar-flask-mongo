<template>
  <div class="tw-flex tw-flex-col tw-justify-center tw-items-center tw-gap-2">
    <q-spinner-pie size="2em" color="orange" />
    <div class="tw-text-gray-400">
      {{ message || 'Loading' }}
    </div>
  </div>
</template>

<script>
import { defineComponent } from 'vue'

export default defineComponent({
  name: 'LoadingComponent',
  props:['message'],
})
</script>
