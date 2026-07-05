<template>
  <div class="card-grid bento-section" ref="gridRef" :style="{ '--glow-color': glowColor }">
    <slot :shouldDisableAnimations="shouldDisableAnimations" />
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted, computed } from 'vue'
import { gsap } from 'gsap'

const props = defineProps({
  textAutoHide: { type: Boolean, default: true },
  enableStars: { type: Boolean, default: true },
  enableSpotlight: { type: Boolean, default: true },
  enableBorderGlow: { type: Boolean, default: true },
  disableAnimations: { type: Boolean, default: false },
  spotlightRadius: { type: Number, default: 290 },
  particleCount: { type: Number, default: 12 },
  enableTilt: { type: Boolean, default: false },
  glowColor: { type: String, default: '192, 132, 252' }, // pastel purple glow
  clickEffect: { type: Boolean, default: true },
  enableMagnetism: { type: Boolean, default: true }
})

const gridRef = ref(null)
const isMobile = ref(false)

const shouldDisableAnimations = computed(() => props.disableAnimations || isMobile.value)

const checkMobile = () => {
  isMobile.value = window.innerWidth <= 768
}

// Spotlight DOM element ref
let spotlightEl = null

const calculateSpotlightValues = (radius) => ({
  proximity: radius * 0.5,
  fadeDistance: radius * 0.75
})

const updateCardGlowProperties = (card, mouseX, mouseY, glow, radius) => {
  const rect = card.getBoundingClientRect()
  const relativeX = ((mouseX - rect.left) / rect.width) * 100
  const relativeY = ((mouseY - rect.top) / rect.height) * 100

  card.style.setProperty('--glow-x', `${relativeX}%`)
  card.style.setProperty('--glow-y', `${relativeY}%`)
  card.style.setProperty('--glow-intensity', glow.toString())
  card.style.setProperty('--glow-radius', `${radius}px`)
}

onMounted(() => {
  checkMobile()
  window.addEventListener('resize', checkMobile)

  if (props.enableSpotlight && !shouldDisableAnimations.value) {
    spotlightEl = document.createElement('div')
    spotlightEl.className = 'global-spotlight'
    spotlightEl.style.cssText = `
      position: fixed;
      width: 800px;
      height: 800px;
      border-radius: 50%;
      pointer-events: none;
      background: radial-gradient(circle,
        rgba(${props.glowColor}, 0.15) 0%,
        rgba(${props.glowColor}, 0.08) 15%,
        rgba(${props.glowColor}, 0.04) 25%,
        rgba(${props.glowColor}, 0.02) 40%,
        rgba(${props.glowColor}, 0.01) 65%,
        transparent 70%
      );
      z-index: 200;
      opacity: 0;
      transform: translate(-50%, -50%);
      mix-blend-mode: screen;
    `
    document.body.appendChild(spotlightEl)

    const handleMouseMove = (e) => {
      if (!spotlightEl || !gridRef.value) return

      const section = gridRef.value.closest('.bento-section')
      const rect = section?.getBoundingClientRect()
      const mouseInside =
        rect && e.clientX >= rect.left && e.clientX <= rect.right && e.clientY >= rect.top && e.clientY <= rect.bottom

      const cards = gridRef.value.querySelectorAll('.magic-bento-card')

      if (!mouseInside) {
        gsap.to(spotlightEl, {
          opacity: 0,
          duration: 0.3,
          ease: 'power2.out'
        })
        cards.forEach(card => {
          card.style.setProperty('--glow-intensity', '0')
        })
        return
      }

      const { proximity, fadeDistance } = calculateSpotlightValues(props.spotlightRadius)
      let minDistance = Infinity

      cards.forEach(card => {
        const cardRect = card.getBoundingClientRect()
        const centerX = cardRect.left + cardRect.width / 2
        const centerY = cardRect.top + cardRect.height / 2
        const distance =
          Math.hypot(e.clientX - centerX, e.clientY - centerY) - Math.max(cardRect.width, cardRect.height) / 2
        const effectiveDistance = Math.max(0, distance)

        minDistance = Math.min(minDistance, effectiveDistance)

        let glowIntensity = 0
        if (effectiveDistance <= proximity) {
          glowIntensity = 1
        } else if (effectiveDistance <= fadeDistance) {
          glowIntensity = (fadeDistance - effectiveDistance) / (fadeDistance - proximity)
        }

        updateCardGlowProperties(card, e.clientX, e.clientY, glowIntensity, props.spotlightRadius)
      })

      gsap.to(spotlightEl, {
        left: e.clientX,
        top: e.clientY,
        duration: 0.1,
        ease: 'power2.out'
      })

      const targetOpacity =
        minDistance <= proximity
          ? 0.8
          : minDistance <= fadeDistance
            ? ((fadeDistance - minDistance) / (fadeDistance - proximity)) * 0.8
            : 0

      gsap.to(spotlightEl, {
        opacity: targetOpacity,
        duration: targetOpacity > 0 ? 0.2 : 0.5,
        ease: 'power2.out'
      })
    }

    const handleMouseLeave = () => {
      gridRef.value?.querySelectorAll('.magic-bento-card').forEach(card => {
        card.style.setProperty('--glow-intensity', '0')
      })
      if (spotlightEl) {
        gsap.to(spotlightEl, {
          opacity: 0,
          duration: 0.3,
          ease: 'power2.out'
        })
      }
    }

    document.addEventListener('mousemove', handleMouseMove)
    document.addEventListener('mouseleave', handleMouseLeave)

    onUnmounted(() => {
      document.removeEventListener('mousemove', handleMouseMove)
      document.removeEventListener('mouseleave', handleMouseLeave)
      if (spotlightEl && spotlightEl.parentNode) {
        spotlightEl.parentNode.removeChild(spotlightEl)
      }
    })
  }
})

onUnmounted(() => {
  window.removeEventListener('resize', checkMobile)
})
</script>

<style>
.bento-section {
  --glow-x: 50%;
  --glow-y: 50%;
  --glow-intensity: 0;
  --glow-radius: 290px;
  --glow-color: 192, 132, 252;
  --border-color: rgba(255, 255, 255, 0.15); /* Visible borders */
  --background-dark: #120F17;
  --white: hsl(0, 0%, 100%);
  --purple-glow: rgba(192, 132, 252, 0.2);
  position: relative;
  user-select: none;
}

.card-grid {
  display: grid;
  gap: 1.5rem;
  padding: 0.75rem;
  width: 100%;
  max-width: 100%;
}

.magic-bento-card {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  position: relative;
  min-height: 240px;
  width: 100%;
  max-width: 100%;
  padding: 1.5rem;
  border-radius: 20px;
  border: 1px solid var(--border-color);
  background: var(--background-dark);
  overflow: hidden;
  transition: box-shadow 0.3s ease, border-color 0.3s ease;
}

.magic-bento-card:hover {
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.3);
}

@media (max-width: 767px) {
  .card-grid {
    grid-template-columns: 1fr;
    padding: 0.5rem;
  }

  .magic-bento-card {
    width: 100%;
    min-height: 200px;
  }
}

@media (min-width: 768px) and (max-width: 1023px) {
  .card-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (min-width: 1024px) {
  .card-grid {
    grid-template-columns: repeat(4, 1fr);
  }
}

/* Border glow effect */
.magic-bento-card--border-glow::after {
  content: '';
  position: absolute;
  inset: 0;
  padding: 1px;
  background: radial-gradient(
    var(--glow-radius) circle at var(--glow-x) var(--glow-y),
    rgba(var(--glow-color), calc(var(--glow-intensity) * 0.9)) 0%,
    rgba(var(--glow-color), calc(var(--glow-intensity) * 0.4)) 30%,
    transparent 65%
  );
  border-radius: inherit;
  -webkit-mask:
    linear-gradient(#fff 0 0) content-box,
    linear-gradient(#fff 0 0);
  -webkit-mask-composite: xor;
  mask:
    linear-gradient(#fff 0 0) content-box,
    linear-gradient(#fff 0 0);
  mask-composite: exclude;
  pointer-events: none;
  opacity: 1;
  transition: opacity 0.3s ease;
  z-index: 5;
}

.magic-bento-card--border-glow:hover {
  border-color: rgba(var(--glow-color), 0.4);
  box-shadow:
    0 4px 20px rgba(46, 24, 78, 0.4),
    0 0 30px rgba(132, 0, 255, 0.15);
}

.particle-container {
  position: relative;
  overflow: hidden;
}

.particle::before {
  content: '';
  position: absolute;
  top: -2px;
  left: -2px;
  right: -2px;
  bottom: -2px;
  background: rgba(132, 0, 255, 0.2);
  border-radius: 50%;
  z-index: -1;
}

.particle-container:hover {
  box-shadow:
    0 4px 20px rgba(46, 24, 78, 0.2),
    0 0 30px rgba(132, 0, 255, 0.15);
}

/* Global spotlight styles */
.global-spotlight {
  mix-blend-mode: screen;
  will-change: transform, opacity;
  z-index: 200 !important;
  pointer-events: none;
}
</style>
