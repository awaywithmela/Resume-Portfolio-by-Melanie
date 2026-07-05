<template>
  <!-- Light Theme: Clean HTML Folder Card from Vercel -->
  <div v-if="isLight" class="relative w-full">
    <!-- Tab -->
    <div
      class="folder-tab-wrap-vercel relative z-10 inline-block rounded-t-3xl border border-purple-300 border-b-0 bg-white px-7 py-1 -mb-[1px]">
      <span class="text-sm font-bold tracking-wide text-purple-500">
        {{ title }}
      </span>
    </div>

    <!-- Right Header Actions Slot -->
    <div class="absolute top-0 right-0 z-10 p-1">
      <slot name="header-actions" />
    </div>

    <!-- Card Body -->
    <div
      class="relative rounded-2xl rounded-tl-none border border-purple-300 bg-white/90 p-8 shadow-xl backdrop-blur-md overflow-hidden">
      <slot />
    </div>
  </div>

  <!-- Dark Theme: Custom Animated BorderGlow Folder Card -->
  <div v-else class="folder-card relative w-full">
    <!-- Tab Wrapper -->
    <div ref="tabRef" class="folder-tab-wrap inline-block relative z-30">
      <BorderGlow
        className="tab-glow-card overflow-visible"
        backgroundColor="#120F17"
        :fillOpacity="1"
      >
        <div class="px-7 py-2">
          <span class="folder-tab-title text-sm font-bold tracking-wide text-[#c084fc]">
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
      className="folder-glow-card overflow-hidden"
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
import { ref, onMounted, onUnmounted } from 'vue'
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
const isLight = ref(false)
let observer = null

onMounted(() => {
  if (tabRef.value) {
    tabWidth.value = tabRef.value.offsetWidth
  }

  isLight.value = document.body.classList.contains('theme-light-root')
  observer = new MutationObserver(() => {
    isLight.value = document.body.classList.contains('theme-light-root')
  })
  observer.observe(document.body, { attributes: true, attributeFilter: ['class'] })
})

onUnmounted(() => {
  if (observer) {
    observer.disconnect()
  }
})
</script>

<style scoped>
.folder-card {
  --folder-bg: #120F17;
  --folder-border: rgba(255, 255, 255, 0.1);
}

.folder-tab-wrap {
  margin-bottom: -1px;
  margin-left: 0;
}

/* Inverted fillet curve ONLY at the bottom right of the tab for dark theme */
.folder-tab-wrap::before {
  content: "";
  position: absolute;
  right: -16px;
  bottom: 0;
  width: 16px;
  height: 16px;
  z-index: 10;
  pointer-events: none;
  background: radial-gradient(
    circle 16px at 16px 0px,
    transparent 15px,
    var(--folder-border) 15px,
    var(--folder-border) 16px,
    var(--folder-bg) 16px
  );
}

.folder-tab-wrap::after {
  content: "";
  position: absolute;
  left: 1px;
  right: 1px;
  bottom: -2px;
  height: 4px;
  background: var(--folder-bg);
  z-index: 5;
}

/* Square bottom tab corners for both themes */
.folder-card :deep(.tab-glow-card),
.folder-card :deep(.tab-glow-card::before),
.folder-card :deep(.tab-glow-card::after),
.folder-card :deep(.tab-glow-card .edge-light),
.folder-card :deep(.tab-glow-card .border-glow-inner) {
  border-bottom-left-radius: 0 !important;
  border-bottom-right-radius: 0 !important;
}

/* Default (Dark Theme) card body overrides: square top-left corner under flush tab */
.folder-card :deep(.folder-glow-card),
.folder-card :deep(.folder-glow-card::before),
.folder-card :deep(.folder-glow-card::after),
.folder-card :deep(.folder-glow-card .edge-light),
.folder-card :deep(.folder-glow-card .border-glow-inner) {
  border-top-left-radius: 0 !important;
}

.folder-card :deep(.tab-glow-card .border-glow-inner),
.folder-card :deep(.folder-glow-card .border-glow-inner) {
  background: transparent;
}

/* Inverted fillet curve at the bottom right of the tab for light theme Vercel card */
.folder-tab-wrap-vercel::before {
  content: "";
  position: absolute;
  right: -16px;
  bottom: 0;
  width: 16px;
  height: 16px;
  z-index: 10;
  pointer-events: none;
  background: radial-gradient(
    circle 16px at 16px 0px,
    transparent 15px,
    rgb(216 180 254) 15px, /* purple-300 border-color */
    rgb(216 180 254) 16px,
    #ffffff 16px
  );
}
</style>
