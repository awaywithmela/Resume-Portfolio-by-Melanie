<template>
  <div
    ref="cardRef"
    :class="[
      'magic-bento-card',
      textAutoHide ? 'magic-bento-card--text-autohide' : '',
      enableBorderGlow ? 'magic-bento-card--border-glow' : '',
      enableStars ? 'particle-container' : '',
      className
    ]"
    :style="{
      '--glow-color': glowColor
    }"
  >
    <slot />
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import { gsap } from 'gsap'

const props = defineProps({
  className: { type: String, default: '' },
  textAutoHide: { type: Boolean, default: true },
  enableBorderGlow: { type: Boolean, default: true },
  enableStars: { type: Boolean, default: false },
  glowColor: { type: String, default: '132, 0, 255' },
  enableTilt: { type: Boolean, default: false },
  clickEffect: { type: Boolean, default: true },
  enableMagnetism: { type: Boolean, default: true },
  disableAnimations: { type: Boolean, default: false },
  particleCount: { type: Number, default: 12 }
})

const cardRef = ref(null)
const particles = []
const timeouts = []
let isHovered = false
let memoizedParticles = []
let particlesInitialized = false
let magnetismAnimation = null

const createParticleElement = (x, y, color) => {
  const el = document.createElement('div')
  el.className = 'particle'
  el.style.cssText = `
    position: absolute;
    width: 4px;
    height: 4px;
    border-radius: 50%;
    background: rgba(${color}, 1);
    box-shadow: 0 0 6px rgba(${color}, 0.6);
    pointer-events: none;
    z-index: 100;
    left: ${x}px;
    top: ${y}px;
  `
  return el
}

const initializeParticles = () => {
  if (particlesInitialized || !cardRef.value) return
  const { width, height } = cardRef.value.getBoundingClientRect()
  memoizedParticles = Array.from({ length: props.particleCount }, () =>
    createParticleElement(Math.random() * width, Math.random() * height, props.glowColor)
  )
  particlesInitialized = true
}

const clearAllParticles = () => {
  timeouts.forEach(clearTimeout)
  timeouts.length = 0
  if (magnetismAnimation) magnetismAnimation.kill()

  particles.forEach(particle => {
    gsap.to(particle, {
      scale: 0,
      opacity: 0,
      duration: 0.3,
      ease: 'back.in(1.7)',
      onComplete: () => {
        if (particle.parentNode) particle.parentNode.removeChild(particle)
      }
    })
  })
  particles.length = 0
}

const animateParticles = () => {
  if (!cardRef.value || !isHovered) return
  if (!particlesInitialized) initializeParticles()

  memoizedParticles.forEach((particle, index) => {
    const timeoutId = setTimeout(() => {
      if (!isHovered || !cardRef.value) return
      const clone = particle.cloneNode(true)
      cardRef.value.appendChild(clone)
      particles.push(clone)

      gsap.fromTo(clone, { scale: 0, opacity: 0 }, { scale: 1, opacity: 1, duration: 0.3, ease: 'back.out(1.7)' })
      gsap.to(clone, {
        x: (Math.random() - 0.5) * 100,
        y: (Math.random() - 0.5) * 100,
        rotation: Math.random() * 360,
        duration: 2 + Math.random() * 2,
        ease: 'none',
        repeat: -1,
        yoyo: true
      })
      gsap.to(clone, {
        opacity: 0.3,
        duration: 1.5,
        ease: 'power2.inOut',
        repeat: -1,
        yoyo: true
      })
    }, index * 100)
    timeouts.push(timeoutId)
  })
}

onMounted(() => {
  if (props.disableAnimations || !cardRef.value) return
  const element = cardRef.value

  const handleMouseEnter = () => {
    isHovered = true
    if (props.enableStars) {
      animateParticles()
    }
    if (props.enableTilt) {
      gsap.to(element, {
        rotateX: 5,
        rotateY: 5,
        duration: 0.3,
        ease: 'power2.out',
        transformPerspective: 1000
      })
    }
  }

  const handleMouseLeave = () => {
    isHovered = false
    if (props.enableStars) {
      clearAllParticles()
    }
    if (props.enableTilt) {
      gsap.to(element, {
        rotateX: 0,
        rotateY: 0,
        duration: 0.3,
        ease: 'power2.out'
      })
    }
    if (props.enableMagnetism) {
      gsap.to(element, {
        x: 0,
        y: 0,
        duration: 0.3,
        ease: 'power2.out'
      })
    }
  }

  const handleMouseMove = e => {
    if (!props.enableTilt && !props.enableMagnetism) return
    const rect = element.getBoundingClientRect()
    const x = e.clientX - rect.left
    const y = e.clientY - rect.top
    const centerX = rect.width / 2
    const centerY = rect.height / 2

    if (props.enableTilt) {
      const rotateX = ((y - centerY) / centerY) * -10
      const rotateY = ((x - centerX) / centerX) * 10
      gsap.to(element, {
        rotateX,
        rotateY,
        duration: 0.1,
        ease: 'power2.out',
        transformPerspective: 1000
      })
    }

    if (props.enableMagnetism) {
      const magnetX = (x - centerX) * 0.05
      const magnetY = (y - centerY) * 0.05
      magnetismAnimation = gsap.to(element, {
        x: magnetX,
        y: magnetY,
        duration: 0.3,
        ease: 'power2.out'
      })
    }
  }

  const handleClick = e => {
    if (!props.clickEffect) return
    const rect = element.getBoundingClientRect()
    const x = e.clientX - rect.left
    const y = e.clientY - rect.top
    const maxDistance = Math.max(
      Math.hypot(x, y),
      Math.hypot(x - rect.width, y),
      Math.hypot(x, y - rect.height),
      Math.hypot(x - rect.width, y - rect.height)
    )

    const ripple = document.createElement('div')
    ripple.style.cssText = `
      position: absolute;
      width: ${maxDistance * 2}px;
      height: ${maxDistance * 2}px;
      border-radius: 50%;
      background: radial-gradient(circle, rgba(${props.glowColor}, 0.4) 0%, rgba(${props.glowColor}, 0.2) 30%, transparent 70%);
      left: ${x - maxDistance}px;
      top: ${y - maxDistance}px;
      pointer-events: none;
      z-index: 1000;
    `
    element.appendChild(ripple)

    gsap.fromTo(
      ripple,
      { scale: 0, opacity: 1 },
      {
        scale: 1,
        opacity: 0,
        duration: 0.8,
        ease: 'power2.out',
        onComplete: () => ripple.remove()
      }
    )
  }

  element.addEventListener('mouseenter', handleMouseEnter)
  element.addEventListener('mouseleave', handleMouseLeave)
  element.addEventListener('mousemove', handleMouseMove)
  element.addEventListener('click', handleClick)

  onUnmounted(() => {
    isHovered = false
    element.removeEventListener('mouseenter', handleMouseEnter)
    element.removeEventListener('mouseleave', handleMouseLeave)
    element.removeEventListener('mousemove', handleMouseMove)
    element.removeEventListener('click', handleClick)
    clearAllParticles()
  })
})
</script>
