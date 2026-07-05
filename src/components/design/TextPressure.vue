<template>
  <div ref="containerRef" class="relative w-full h-full overflow-hidden bg-transparent">
    <component :is="'style'" v-if="styleElement">{{ styleElement }}</component>
    <div
      ref="titleRef"
      :class="[
        'text-pressure-title',
        className,
        flex ? 'flex justify-between' : '',
        stroke ? 'stroke' : '',
        'uppercase text-center'
      ]"
      :style="{
        fontFamily,
        fontSize: fontSize + 'px',
        lineHeight: lineHeight,
        transform: `scale(1, ${scaleY})`,
        transformOrigin: 'center top',
        margin: 0,
        fontWeight: 100,
        color: stroke ? undefined : textColor
      }"
    >
      <span
        v-for="(char, i) in chars"
        :key="i"
        :ref="el => { if (el) spans[i] = el }"
        :data-char="char"
        class="inline-block"
      >
        {{ char }}
      </span>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted, computed, watch, nextTick } from 'vue'

const props = defineProps({
  text: { type: String, default: 'Compressa' },
  fontFamily: { type: String, default: 'Roboto Flex' },
  fontUrl: { type: String, default: 'https://fonts.googleapis.com/css2?family=Roboto+Flex:opsz,wdth,wght@8..144,25..151,100..1000&display=swap' },
  width: { type: Boolean, default: true },
  weight: { type: Boolean, default: true },
  italic: { type: Boolean, default: true },
  alpha: { type: Boolean, default: false },
  flex: { type: Boolean, default: true },
  stroke: { type: Boolean, default: false },
  scale: { type: Boolean, default: false },
  textColor: { type: String, default: '#FFFFFF' },
  strokeColor: { type: String, default: '#FF0000' },
  strokeWidth: { type: Number, default: 2 },
  className: { type: String, default: '' },
  minFontSize: { type: Number, default: 24 }
})

const containerRef = ref(null)
const titleRef = ref(null)
const spans = ref([])

const mouse = ref({ x: 0, y: 0 })
const cursor = ref({ x: 0, y: 0 })

const fontSize = ref(props.minFontSize)
const scaleY = ref(1)
const lineHeight = ref(1)

const chars = computed(() => props.text.split(''))

const dist = (a, b) => {
  const dx = b.x - a.x
  const dy = b.y - a.y
  return Math.sqrt(dx * dx + dy * dy)
}

const getAttr = (distance, maxDist, minVal, maxVal) => {
  const val = maxVal - Math.abs((maxVal * distance) / maxDist)
  return Math.max(minVal, val + minVal)
}

const debounce = (func, delay) => {
  let timeoutId
  return (...args) => {
    clearTimeout(timeoutId)
    timeoutId = setTimeout(() => {
      func(...args)
    }, delay)
  }
}

const handleMouseMove = (e) => {
  cursor.value.x = e.clientX
  cursor.value.y = e.clientY
}

const handleTouchMove = (e) => {
  const t = e.touches[0]
  cursor.value.x = t.clientX
  cursor.value.y = t.clientY
}

const setSize = () => {
  if (!containerRef.value || !titleRef.value) return

  const { width: containerW, height: containerH } = containerRef.value.getBoundingClientRect()

  let newFontSize = containerW / (chars.value.length / 2)
  newFontSize = Math.max(newFontSize, props.minFontSize)

  fontSize.value = newFontSize
  scaleY.value = 1
  lineHeight.value = 1

  requestAnimationFrame(() => {
    if (!titleRef.value) return
    const textRect = titleRef.value.getBoundingClientRect()

    if (props.scale && textRect.height > 0) {
      const yRatio = containerH / textRect.height
      scaleY.value = yRatio
      lineHeight.value = yRatio
    }
  })
}

const styleElement = computed(() => {
  return `
    @import url('${props.fontUrl}');
    .stroke span {
      position: relative;
      color: ${props.textColor};
    }
    .stroke span::after {
      content: attr(data-char);
      position: absolute;
      left: 0;
      top: 0;
      color: transparent;
      z-index: -1;
      -webkit-text-stroke-width: ${props.strokeWidth}px;
      -webkit-text-stroke-color: ${props.strokeColor};
    }
  `
})

let rafId = null
let time = 0

const animate = () => {
  time += 0.04
  mouse.value.x += (cursor.value.x - mouse.value.x) / 15
  mouse.value.y += (cursor.value.y - mouse.value.y) / 15

  if (titleRef.value) {
    const titleRect = titleRef.value.getBoundingClientRect()
    const maxDist = titleRect.width / 2

    spans.value.forEach((span, i) => {
      if (!span) return

      const rect = span.getBoundingClientRect()
      const charCenter = {
        x: rect.x + rect.width / 2,
        y: rect.y + rect.height / 2
      }

      const d = dist(mouse.value, charCenter)

      // Base auto-animation wave (wavy rhythm offset per letter)
      const phase = time + (i * 0.8)
      const wave = (Math.sin(phase) + 1) / 2 // ranges 0 to 1

      // Cursor hover intensity (closer = larger value up to 1)
      const hoverIntensity = Math.max(0, 1 - d / (maxDist || 1))

      // Merge wave and hover (whichever is stronger)
      const effectiveVal = Math.max(hoverIntensity, wave)

      const wdth = props.width ? Math.floor(25 + effectiveVal * 125) : 100
      const wght = props.weight ? Math.floor(100 + effectiveVal * 900) : 400
      const italVal = props.italic ? effectiveVal.toFixed(2) : '0'
      const alphaVal = props.alpha ? effectiveVal.toFixed(2) : '1'

      const newFontVariationSettings = `'wght' ${wght}, 'wdth' ${wdth}, 'ital' ${italVal}`

      if (span.style.fontVariationSettings !== newFontVariationSettings) {
        span.style.fontVariationSettings = newFontVariationSettings
      }
      if (props.alpha && span.style.opacity !== alphaVal) {
        span.style.opacity = alphaVal
      }
    })
  }

  rafId = requestAnimationFrame(animate)
}

onMounted(() => {
  window.addEventListener('mousemove', handleMouseMove)
  window.addEventListener('touchmove', handleTouchMove, { passive: true })

  if (containerRef.value) {
    const { left, top, width: containerW, height: containerH } = containerRef.value.getBoundingClientRect()
    mouse.value.x = left + containerW / 2
    mouse.value.y = top + containerH / 2
    cursor.value.x = mouse.value.x
    cursor.value.y = mouse.value.y
  }

  setSize()
  const debouncedSetSize = debounce(setSize, 100)
  window.addEventListener('resize', debouncedSetSize)

  rafId = requestAnimationFrame(animate)

  onUnmounted(() => {
    window.removeEventListener('mousemove', handleMouseMove)
    window.removeEventListener('touchmove', handleTouchMove)
    window.removeEventListener('resize', debouncedSetSize)
    if (rafId) {
      cancelAnimationFrame(rafId)
    }
  })
})

watch(() => props.text, () => {
  spans.value = []
  nextTick(() => {
    setSize()
  })
})
</script>
