<template>
  <figure
    ref="figureRef"
    class="relative w-full h-full flex flex-col items-center justify-center [perspective:800px]"
    :style="{
      height: containerHeight,
      width: containerWidth
    }"
    @mousemove="handleMouse"
    @mouseenter="handleMouseEnter"
    @mouseleave="handleMouseLeave"
  >
    <!-- Mobile Warning -->
    <div v-if="showMobileWarning" class="absolute top-4 text-center text-sm block sm:hidden">
      This effect is not optimized for mobile. Check on desktop.
    </div>

    <!-- 3D Card Container -->
    <div
      class="relative [transform-style:preserve-3d]"
      :style="{
        width: imageWidth,
        height: imageHeight,
        transform: `rotateX(${rotateX}deg) rotateY(${rotateY}deg) scale(${scale})`
      }"
    >
      <!-- Image -->
      <img
        :src="imageSrc"
        :alt="altText"
        class="absolute top-0 left-0 object-cover rounded-[15px] will-change-transform [transform:translateZ(0)]"
        :style="{
          width: imageWidth,
          height: imageHeight
        }"
      />

      <!-- Overlay Content -->
      <div
        v-if="displayOverlayContent"
        class="absolute top-0 left-0 z-10 will-change-transform [transform:translateZ(30px)]"
      >
        <slot name="overlay"></slot>
      </div>
    </div>

    <!-- Tooltip -->
    <div
      v-if="showTooltip"
      class="pointer-events-none absolute left-0 top-0 rounded-[4px] bg-white px-[10px] py-[4px] text-[10px] text-[#2d2d2d] opacity-0 z-20 hidden sm:block"
      :style="{
        opacity: opacity,
        transform: `translate(${mouseX}px, ${mouseY}px) rotate(${rotateFigcaption}deg)`
      }"
    >
      {{ captionText }}
    </div>
  </figure>
</template>

<script setup>
import { ref, watch } from 'vue'
import { useRafFn } from '@vueuse/core'

const props = defineProps({
  imageSrc: { type: String, required: true },
  altText: { type: String, default: 'Tilted card image' },
  captionText: { type: String, default: '' },
  containerHeight: { type: String, default: '300px' },
  containerWidth: { type: String, default: '100%' },
  imageHeight: { type: String, default: '300px' },
  imageWidth: { type: String, default: '300px' },
  scaleOnHover: { type: Number, default: 1.1 },
  rotateAmplitude: { type: Number, default: 14 },
  showMobileWarning: { type: Boolean, default: true },
  showTooltip: { type: Boolean, default: true },
  displayOverlayContent: { type: Boolean, default: false },
  isFocused: { type: Boolean, default: false },
  objectFit: { type: String, default: 'cover' }
})

const figureRef = ref(null)

const mouseX = ref(0)
const mouseY = ref(0)
const lastY = ref(0)

// Target Refs (Sources for the springs)
const rotateXTarget = ref(0)
const rotateYTarget = ref(0)
const scaleTarget = ref(1)
const opacityTarget = ref(0)
const rotateFigcaptionTarget = ref(0)

// ---------------------------------------------------------
// Custom Spring Implementation
// Replicates framer-motion's spring physics: F = -kx - cv
// ---------------------------------------------------------

function useSpring(source, { stiffness = 100, damping = 30, mass = 1 } = {}) {
  // Initial value resolution
  const initialValue = typeof source === 'object' && source.value !== undefined ? source.value : source
  
  const current = ref(initialValue)
  const velocity = ref(0)
  
  useRafFn(() => {
    const targetValue = typeof source === 'object' && source.value !== undefined ? source.value : source
    const dist = targetValue - current.value
    
    // Spring Force: F = -kx
    const force = dist * stiffness
    
    // Damping: F_damping = -cv
    const dampingForce = velocity.value * damping
    
    // Total Force
    const acceleration = (force - dampingForce) / mass
    
    // Integration (Euler)
    const dt = 0.016
    
    velocity.value += acceleration * dt
    current.value += velocity.value * dt

    // Snap to rest if very close
    if (Math.abs(dist) < 0.001 && Math.abs(velocity.value) < 0.001) {
       current.value = targetValue
       velocity.value = 0
    }
  })

  return current
}

// Spring configuration
const springOptions = {
  stiffness: 50,
  damping: 15,
  mass: 2
}

const tooltipSpringOptions = {
  stiffness: 350,
  damping: 30,
  mass: 1
}

// Create Springs linked to the Targets
const rotateX = useSpring(rotateXTarget, springOptions)
const rotateY = useSpring(rotateYTarget, springOptions)
const scale = useSpring(scaleTarget, springOptions)
const opacity = useSpring(opacityTarget, { stiffness: 100, damping: 20, mass: 1 })
const rotateFigcaption = useSpring(rotateFigcaptionTarget, tooltipSpringOptions)

// Local hover tracking
const isHovering = ref(false)

// Watch `isFocused` for auto-hover interaction
watch(() => props.isFocused, (newVal) => {
  if (newVal) {
    scaleTarget.value = props.scaleOnHover
    opacityTarget.value = 1
  } else {
    if (!isHovering.value) { 
        ResetState()
    }
  }
})

function handleMouse(e) {
  if (!figureRef.value) return
  
  isHovering.value = true
  const rect = figureRef.value.getBoundingClientRect()
  const offsetX = e.clientX - rect.left - rect.width / 2
  const offsetY = e.clientY - rect.top - rect.height / 2

  const rotationX = (offsetY / (rect.height / 2)) * -props.rotateAmplitude
  const rotationY = (offsetX / (rect.width / 2)) * props.rotateAmplitude

  // Update targets
  rotateXTarget.value = rotationX
  rotateYTarget.value = rotationY

  mouseX.value = e.clientX - rect.left 
  mouseY.value = e.clientY - rect.top

  const velocityY = offsetY - lastY.value
  rotateFigcaptionTarget.value = -velocityY * 0.6
  lastY.value = offsetY
}

function handleMouseEnter() {
  isHovering.value = true
  scaleTarget.value = props.scaleOnHover
  opacityTarget.value = 1
}

function handleMouseLeave() {
  isHovering.value = false
  if (props.isFocused) {
      scaleTarget.value = props.scaleOnHover
      opacityTarget.value = 1
      rotateXTarget.value = 0
      rotateYTarget.value = 0
  } else {
      ResetState()
  }
}

function ResetState() {
  scaleTarget.value = 1
  opacityTarget.value = 0
  rotateXTarget.value = 0
  rotateYTarget.value = 0
  rotateFigcaptionTarget.value = 0
}
</script>

<style scoped>
.tilted-card-figure {
  position: relative;
  width: 100%;
  height: 100%;
  perspective: 800px; /* Tailwind equivalent: [perspective:800px] */
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.tilted-card-mobile-alert {
  position: absolute;
  top: 1rem;
  text-align: center;
  font-size: 0.875rem;
  display: none;
}

@media (max-width: 640px) {
  .tilted-card-mobile-alert {
    display: block;
  }
}

.tilted-card-caption {
  pointer-events: none;
  position: absolute;
  left: 0;
  top: 0;
  border-radius: 4px; /* Tailwind: rounded-[4px] */
  background-color: #fff; /* Tailwind: bg-white */
  padding: 4px 10px; /* Tailwind: px-[10px] py-[4px] */
  font-size: 10px; /* Tailwind: text-[10px] */
  color: #2d2d2d; /* Tailwind: text-[#2d2d2d] */
  opacity: 0;
  z-index: 3;
  width: max-content;
  will-change: transform, opacity;
}
</style>
