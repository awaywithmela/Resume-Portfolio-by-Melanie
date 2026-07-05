<template>
  <div class="relative w-full"> <!-- Container -->

    <!-- Tab Wrapper -->
    <div ref="tabRef" class="inline-block relative z-20">
      <BorderGlow
        className="tab-glow-card rounded-t-3xl overflow-visible -mb-[1px]"
        backgroundColor="#120F17"
        :fillOpacity="1"
      >
        <div class="px-7 py-2">
          <span class="text-sm font-bold tracking-wide text-[#c084fc]">
            {{ title }}
          </span>
        </div>
      </BorderGlow>
    </div>

    <!-- Right Header Actions Slot -->
    <div class="absolute top-0 right-0 z-10 p-1">
      <slot name="header-actions" />
    </div>

    <!-- Card Body -->
    <BorderGlow
      className="folder-glow-card rounded-2xl rounded-tl-none overflow-hidden"
      backgroundColor="#120F17"
      :fillOpacity="1"
      :style="{ '--tab-width': `${tabWidth}px` }"
    >
      <div class="p-8">
        <slot />
      </div>
    </BorderGlow>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import BorderGlow from './design/BorderGlow.vue'

defineProps({
  title: {
    type: String,
    required: true,
    default: 'Section'
  }
})

const tabRef = ref(null)
const tabWidth = ref(180) // default fallback

onMounted(() => {
  if (tabRef.value) {
    tabWidth.value = tabRef.value.offsetWidth
  }
})
</script>
