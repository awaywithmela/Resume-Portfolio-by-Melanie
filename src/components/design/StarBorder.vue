<template>
  <component
    :is="as"
    :class="['star-border-container relative overflow-hidden p-[1px] inline-flex items-center justify-center', className]"
    :style="{
      '--border-color': color,
      '--animation-speed': speed,
      'border-radius': borderRadius
    }"
  >
    <!-- Background rotating light -->
    <div class="star-border-bg" />
    
    <!-- Inner content wrapper -->
    <div 
      class="star-border-inner w-full h-full inline-flex items-center justify-center transition-all duration-300"
      :style="{ 'border-radius': `calc(${borderRadius} - 1px)` }"
    >
      <slot />
    </div>
  </component>
</template>

<script setup>
defineProps({
  as: {
    type: [String, Object],
    default: 'button'
  },
  color: {
    type: String,
    default: '#c084fc' // default cute purple
  },
  speed: {
    type: String,
    default: '4s'
  },
  borderRadius: {
    type: String,
    default: '8px'
  },
  className: {
    type: String,
    default: ''
  }
})
</script>

<style scoped>
.star-border-container {
  isolation: isolate;
  background: rgba(168, 85, 247, 0.3);
}

.star-border-bg {
  position: absolute;
  inset: -300%;
  background: conic-gradient(
    from 0deg,
    transparent 0%,
    transparent 42%,
    var(--border-color) 50%,
    transparent 58%,
    transparent 100%
  );
  animation: rotate-border var(--animation-speed) linear infinite;
  z-index: 1;
}

.star-border-inner {
  position: relative;
  z-index: 2;
  background: #120F17; /* matching card background */
  width: 100%;
  height: 100%;
}

.star-border-container:hover .star-border-inner {
  background: rgba(168, 85, 247, 0.15) !important; /* purple tint hover */
}

@keyframes rotate-border {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
</style>
