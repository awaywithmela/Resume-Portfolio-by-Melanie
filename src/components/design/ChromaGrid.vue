<template>
  <div
    ref="rootRef"
    @pointermove="handleMove"
    @pointerleave="handleLeave"
    :class="['chroma-grid-root relative w-full overflow-visible', className]"
    :style="{
      '--r': `${radius}px`,
      '--x': `${pos.x}px`,
      '--y': `${pos.y}px`
    }"
  >
    <!-- Slot for the actual grid content (keeps original card structures fully intact) -->
    <slot />

    <!-- Grayscale / Dark overlay masks for the spotlight effect -->
    <div
      class="absolute inset-0 pointer-events-none z-30 chroma-mask-dark"
      style="
        backdrop-filter: grayscale(1) brightness(0.78);
        -webkit-backdrop-filter: grayscale(1) brightness(0.78);
        background: rgba(0, 0, 0, 0.001);
        mask-image: radial-gradient(circle var(--r) at var(--x) var(--y), transparent 0%, transparent 15%, rgba(0,0,0,0.10) 30%, rgba(0,0,0,0.22) 45%, rgba(0,0,0,0.35) 60%, rgba(0,0,0,0.50) 75%, rgba(0,0,0,0.68) 88%, white 100%);
        -webkit-mask-image: radial-gradient(circle var(--r) at var(--x) var(--y), transparent 0%, transparent 15%, rgba(0,0,0,0.10) 30%, rgba(0,0,0,0.22) 45%, rgba(0,0,0,0.35) 60%, rgba(0,0,0,0.50) 75%, rgba(0,0,0,0.68) 88%, white 100%);
      "
    />
    <div
      ref="fadeRef"
      class="absolute inset-0 pointer-events-none transition-opacity duration-[250ms] z-40 chroma-mask-fade"
      style="
        backdrop-filter: grayscale(1) brightness(0.78);
        -webkit-backdrop-filter: grayscale(1) brightness(0.78);
        background: rgba(0, 0, 0, 0.001);
        mask-image: radial-gradient(circle var(--r) at var(--x) var(--y), white 0%, white 15%, rgba(255,255,255,0.90) 30%, rgba(255,255,255,0.78) 45%, rgba(255,255,255,0.65) 60%, rgba(255,255,255,0.50) 75%, rgba(255,255,255,0.32) 88%, transparent 100%);
        -webkit-mask-image: radial-gradient(circle var(--r) at var(--x) var(--y), white 0%, white 15%, rgba(255,255,255,0.90) 30%, rgba(255,255,255,0.78) 45%, rgba(255,255,255,0.65) 60%, rgba(255,255,255,0.50) 75%, rgba(255,255,255,0.32) 88%, transparent 100%);
        opacity: 1;
      "
    />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { gsap } from 'gsap'

const props = defineProps({
  className: {
    type: String,
    default: ''
  },
  radius: {
    type: Number,
    default: 340
  },
  damping: {
    type: Number,
    default: 0.45
  },
  fadeOut: {
    type: Number,
    default: 0.6
  },
  ease: {
    type: String,
    default: 'power3.out'
  }
})

const rootRef = ref(null)
const fadeRef = ref(null)
const pos = ref({ x: 0, y: 0 })

let setX = null
let setY = null

onMounted(() => {
  const el = rootRef.value
  if (!el) return

  // set up GSAP setters to update css variables --x and --y directly for performance
  setX = gsap.quickSetter(el, '--x', 'px')
  setY = gsap.quickSetter(el, '--y', 'px')

  const { width, height } = el.getBoundingClientRect()
  pos.value = { x: width / 2, y: height / 2 }
  setX(pos.value.x)
  setY(pos.value.y)
})

const moveTo = (x, y) => {
  gsap.to(pos.value, {
    x,
    y,
    duration: props.damping,
    ease: props.ease,
    onUpdate: () => {
      if (setX && setY) {
        setX(pos.value.x)
        setY(pos.value.y)
      }
    },
    overwrite: true
  })
}

const handleMove = (e) => {
  const el = rootRef.value
  if (!el) return
  const r = el.getBoundingClientRect()
  moveTo(e.clientX - r.left, e.clientY - r.top)
  if (fadeRef.value) {
    gsap.to(fadeRef.value, { opacity: 0, duration: 0.25, overwrite: true })
  }
}

const handleLeave = () => {
  if (fadeRef.value) {
    gsap.to(fadeRef.value, {
      opacity: 1,
      duration: props.fadeOut,
      overwrite: true
    })
  }
}
</script>

<style scoped>
.chroma-grid-root {
  --mouse-x: 50%;
  --mouse-y: 50%;
}

.chroma-mask-dark,
.chroma-mask-fade {
  pointer-events: none;
  width: 100%;
  height: 100%;
}
</style>
