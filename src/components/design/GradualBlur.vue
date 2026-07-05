<template>
  <div ref="containerRef"
    :class="['gradual-blur', config.target === 'page' ? 'gradual-blur-page' : 'gradual-blur-parent', config.className]"
    :style="containerStyle" @mouseenter="handleMouseEnter" @mouseleave="handleMouseLeave">
    <div class="gradual-blur-inner relative w-full h-full">
      <div v-for="(style, index) in blurDivs" :key="index" :style="style"></div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, watch, onMounted, onUnmounted } from 'vue'
import { create, all } from 'mathjs' // Import mathjs as requested
const math = create(all)

const props = defineProps({
  position: { type: String, default: 'bottom' },
  strength: { type: Number, default: 2 },
  height: { type: String, default: '6rem' },
  width: { type: String, default: undefined },
  divCount: { type: Number, default: 5 },
  exponential: { type: Boolean, default: false },
  zIndex: { type: Number, default: 1000 },
  animated: { type: [Boolean, String], default: false },
  duration: { type: String, default: '0.3s' },
  easing: { type: String, default: 'ease-out' },
  opacity: { type: Number, default: 1 },
  curve: { type: String, default: 'linear' },
  responsive: { type: Boolean, default: false },
  target: { type: String, default: 'parent' },
  className: { type: String, default: '' },
  style: { type: Object, default: () => ({}) },
  preset: { type: String, default: '' },
  hoverIntensity: { type: Number, default: undefined },
  onAnimationComplete: { type: Function, default: undefined },
  // Responsive config props
  mobileHeight: String,
  tabletHeight: String,
  desktopHeight: String,
  mobileWidth: String,
  tabletWidth: String,
  desktopWidth: String,
})

const DEFAULT_CONFIG = {
  position: 'bottom',
  strength: 9,
  height: '6rem',
  divCount: 5,
  exponential: false,
  zIndex: 1000,
  animated: false,
  duration: '0.3s',
  easing: 'ease-out',
  opacity: 1,
  curve: 'linear',
  responsive: false,
  target: 'parent',
  className: '',
  style: {}
}

const PRESETS = {
  top: { position: 'top', height: '6rem' },
  bottom: { position: 'bottom', height: '6rem' },
  left: { position: 'left', height: '6rem' },
  right: { position: 'right', height: '6rem' },
  subtle: { height: '4rem', strength: 1, opacity: 0.8, divCount: 3 },
  intense: { height: '10rem', strength: 4, divCount: 8, exponential: true },
  smooth: { height: '8rem', curve: 'bezier', divCount: 10 },
  sharp: { height: '5rem', curve: 'linear', divCount: 4 },
  header: { position: 'top', height: '8rem', curve: 'ease-out' },
  footer: { position: 'bottom', height: '8rem', curve: 'ease-out' },
  sidebar: { position: 'left', height: '6rem', strength: 2.5 },
  'page-header': { position: 'top', height: '10rem', target: 'page', strength: 3 },
  'page-footer': { position: 'bottom', height: '10rem', target: 'page', strength: 3 }
}

const CURVE_FUNCTIONS = {
  linear: p => p,
  bezier: p => p * p * (3 - 2 * p),
  'ease-in': p => p * p,
  'ease-out': p => 1 - Math.pow(1 - p, 2),
  'ease-in-out': p => (p < 0.5 ? 2 * p * p : 1 - Math.pow(-2 * p + 2, 2) / 2)
}

const containerRef = ref(null)
const isHovered = ref(false)
const isVisible = ref(false)
// Responsive dimensions state
const currentHeight = ref(props.height)
const currentWidth = ref(props.width)

function mergeConfigs(defaults, preset, props) {
  return { ...defaults, ...preset, ...props }
}

const config = computed(() => {
  const presetConfig = props.preset && PRESETS[props.preset] ? PRESETS[props.preset] : {}
  // Merge all props
  const merged = mergeConfigs(DEFAULT_CONFIG, presetConfig, props)
  return merged
})

// Responsive Logic
function updateDimensions() {
  if (!config.value.responsive) {
    currentHeight.value = config.value.height
    currentWidth.value = config.value.width
    return
  }

  const w = window.innerWidth

  // Height
  let h = config.value.height
  if (w <= 480 && props.mobileHeight) h = props.mobileHeight
  else if (w <= 768 && props.tabletHeight) h = props.tabletHeight
  else if (w <= 1024 && props.desktopHeight) h = props.desktopHeight
  currentHeight.value = h

  // Width
  let wd = config.value.width
  if (w <= 480 && props.mobileWidth) wd = props.mobileWidth
  else if (w <= 768 && props.tabletWidth) wd = props.tabletWidth
  else if (w <= 1024 && props.desktopWidth) wd = props.desktopWidth
  currentWidth.value = wd
}

// Debounce
function debounce(fn, wait) {
  let t
  return (...a) => {
    clearTimeout(t)
    t = setTimeout(() => fn(...a), wait)
  }
}

onMounted(() => {
  updateDimensions()
  const debouncedResize = debounce(updateDimensions, 100)
  window.addEventListener('resize', debouncedResize)

  // Intersection Observer
  if (config.value.animated === 'scroll' && containerRef.value) {
    // Start invisible if scrolling
    isVisible.value = false
    const observer = new IntersectionObserver(([entry]) => {
      isVisible.value = entry.isIntersecting
    }, { threshold: 0.1 })
    observer.observe(containerRef.value)

    // Cleanup observer on unmount
    onUnmounted(() => {
      observer.disconnect()
      window.removeEventListener('resize', debouncedResize)
    })
  } else {
    // Default visible if not scroll animated (or basic animated)
    isVisible.value = !config.value.animated || config.value.animated === true // Using simple true for fade-in logic in style
    // Actually per React code: useState(!shouldObserve). So if animated=scroll, start false.
    if (config.value.animated !== 'scroll') isVisible.value = true
  }
})

function getGradientDirection(position) {
  const directions = {
    top: 'to top',
    bottom: 'to bottom',
    left: 'to left',
    right: 'to right'
  }
  return directions[position] || 'to bottom'
}

const blurDivs = computed(() => {
  const divs = []
  const increment = 100 / config.value.divCount
  const currentStrength = isHovered.value && config.value.hoverIntensity
    ? config.value.strength * config.value.hoverIntensity
    : config.value.strength

  const curveFunc = CURVE_FUNCTIONS[config.value.curve] || CURVE_FUNCTIONS.linear

  for (let i = 1; i <= config.value.divCount; i++) {
    let progress = i / config.value.divCount
    progress = curveFunc(progress)

    let blurValue
    if (config.value.exponential) {
      blurValue = math.pow(2, progress * 4) * 0.0625 * currentStrength
    } else {
      blurValue = 0.0625 * (progress * config.value.divCount + 1) * currentStrength
    }

    // Using math.round as requested
    const p1 = math.round((increment * i - increment) * 10) / 10
    const p2 = math.round(increment * i * 10) / 10
    const p3 = math.round((increment * i + increment) * 10) / 10
    const p4 = math.round((increment * i + increment * 2) * 10) / 10

    let gradient = `transparent ${p1}%, black ${p2}%`
    if (p3 <= 100) gradient += `, black ${p3}%`
    if (p4 <= 100) gradient += `, transparent ${p4}%`

    const direction = getGradientDirection(config.value.position)

    divs.push({
      position: 'absolute',
      inset: '0',
      maskImage: `linear-gradient(${direction}, ${gradient})`,
      WebkitMaskImage: `linear-gradient(${direction}, ${gradient})`,
      backdropFilter: `blur(${blurValue.toFixed(3)}rem)`,
      WebkitBackdropFilter: `blur(${blurValue.toFixed(3)}rem)`,
      opacity: config.value.opacity,
      transition: config.value.animated && config.value.animated !== 'scroll'
        ? `backdrop-filter ${config.value.duration} ${config.value.easing}`
        : undefined
    })
  }
  return divs
})

const containerStyle = computed(() => {
  const isVertical = ['top', 'bottom'].includes(config.value.position)
  const isHorizontal = ['left', 'right'].includes(config.value.position)
  const isPageTarget = config.value.target === 'page'

  const baseStyle = {
    position: isPageTarget ? 'fixed' : 'absolute',
    pointerEvents: config.value.hoverIntensity ? 'auto' : 'none',
    opacity: isVisible.value ? 1 : 0,
    transition: config.value.animated ? `opacity ${config.value.duration} ${config.value.easing}` : undefined,
    zIndex: isPageTarget ? config.value.zIndex + 100 : config.value.zIndex,
    ...config.value.style
  }

  if (isVertical) {
    baseStyle.height = currentHeight.value
    baseStyle.width = currentWidth.value || '100%'
    baseStyle[config.value.position] = 0
    baseStyle.left = 0
    baseStyle.right = 0
  } else if (isHorizontal) {
    baseStyle.width = currentWidth.value || currentHeight.value
    baseStyle.height = '100%'
    baseStyle[config.value.position] = 0
    baseStyle.top = 0
    baseStyle.bottom = 0
  }

  return baseStyle
})

// Animation Complete Callback
watch(isVisible, (newVal) => {
  if (newVal && config.value.animated === 'scroll' && props.onAnimationComplete) {
    setTimeout(() => props.onAnimationComplete(), parseFloat(config.value.duration) * 1000)
  }
})

function handleMouseEnter() {
  if (config.value.hoverIntensity) isHovered.value = true
}

function handleMouseLeave() {
  if (config.value.hoverIntensity) isHovered.value = false
}
</script>

<style scoped>
/* No specific CSS needed as it's inline styled by logic */
</style>
