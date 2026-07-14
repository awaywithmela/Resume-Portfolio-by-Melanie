<template>
  <div class="folder-card-wrap relative w-full">
    <div
      class="folder-tab relative z-10 inline-block rounded-t-3xl border border-[var(--folder-border)] border-b-0 bg-[var(--folder-tab-bg)] px-7 py-1 -mb-[1px]">
      <span class="text-sm font-bold tracking-wide text-[var(--folder-title)]">
        {{ title }}
      </span>
    </div>

    <div class="absolute top-0 right-0 z-20 p-1">
      <slot name="header-actions" />
    </div>

    <div
      class="folder-body relative rounded-2xl rounded-tl-none border border-[var(--folder-border)] bg-[var(--folder-body-bg)] p-6 shadow-xl backdrop-blur-md overflow-hidden md:p-8">
      <slot />
    </div>
  </div>
</template>

<script setup>
defineProps({
  title: {
    type: String,
    required: true,
    default: 'Section'
  }
})
</script>

<style scoped>
.folder-card-wrap {
  --folder-tab-bg: rgba(18, 15, 23, 0.94);
  --folder-body-bg: rgba(18, 15, 23, 0.9);
  --folder-border: rgba(192, 132, 252, 0.32);
  --folder-title: #c084fc;
}

:global(.theme-light-root) .folder-card-wrap,
:global(.portfolio-shell.theme-light) .folder-card-wrap {
  --folder-tab-bg: #ffffff;
  --folder-body-bg: rgba(255, 255, 255, 0.92);
  --folder-border: rgb(216 180 254);
  --folder-title: #a855f7;
}

.folder-tab::after {
  content: "";
  position: absolute;
  left: 1px;
  right: 1px;
  bottom: -1px;
  height: 2px;
  background: var(--folder-tab-bg);
  pointer-events: none;
}

:global(.theme-light-root) .folder-body,
:global(.portfolio-shell.theme-light) .folder-body {
  box-shadow:
    0 20px 42px rgb(15 23 42 / 10%),
    0 12px 28px rgb(168 85 247 / 10%),
    0 0 0 1px rgb(216 180 254 / 20%);
}
</style>
