<template>
  <div class="relative w-full min-h-screen" @click="handleClick">
    <canvas ref="canvasRef" class="fixed inset-0 pointer-events-none z-50" />
    <slot />
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

const props = defineProps({
  sparkColor: {
    type: String,
    default: '#c084fc' // cute purple spark default
  },
  sparkSize: {
    type: Number,
    default: 10
  },
  sparkRadius: {
    type: Number,
    default: 15
  },
  sparkCount: {
    type: Number,
    default: 8
  },
  duration: {
    type: Number,
    default: 400
  },
  easing: {
    type: String,
    default: 'ease-out'
  },
  extraScale: {
    type: Number,
    default: 1.0
  }
})

const canvasRef = ref(null)
const sparks = ref([])
const startTimeRef = ref(null)

const easeFunc = (t) => {
  switch (props.easing) {
    case 'linear':
      return t
    case 'ease-in':
      return t * t
    case 'ease-in-out':
      return t < 0.5 ? 2 * t * t : -1 + (4 - 2 * t) * t
    default:
      return t * (2 - t)
  }
}

let animationId = null

const draw = (timestamp) => {
  if (!startTimeRef.value) {
    startTimeRef.value = timestamp
  }
  
  const canvas = canvasRef.value
  if (!canvas) {
    animationId = requestAnimationFrame(draw)
    return
  }

  const ctx = canvas.getContext('2d')
  if (!ctx) {
    animationId = requestAnimationFrame(draw)
    return
  }

  ctx.clearRect(0, 0, canvas.width, canvas.height)

  sparks.value = sparks.value.filter((spark) => {
    const elapsed = timestamp - spark.startTime
    if (elapsed >= props.duration) {
      return false
    }

    const progress = elapsed / props.duration
    const eased = easeFunc(progress)

    const distance = eased * props.sparkRadius * props.extraScale
    const lineLength = props.sparkSize * (1 - eased)

    const x1 = spark.x + distance * Math.cos(spark.angle)
    const y1 = spark.y + distance * Math.sin(spark.angle)
    const x2 = spark.x + (distance + lineLength) * Math.cos(spark.angle)
    const y2 = spark.y + (distance + lineLength) * Math.sin(spark.angle)

    ctx.strokeStyle = props.sparkColor
    ctx.lineWidth = 2
    ctx.beginPath()
    ctx.moveTo(x1, y1)
    ctx.lineTo(x2, y2)
    ctx.stroke()

    return true
  })

  animationId = requestAnimationFrame(draw)
}

const handleClick = (e) => {
  const canvas = canvasRef.value
  if (!canvas) return
  
  // Since the canvas is fixed to the viewport, client coordinates map 1:1
  const x = e.clientX
  const y = e.clientY

  const now = performance.now()
  const newSparks = Array.from({ length: props.sparkCount }, (_, i) => ({
    x,
    y,
    angle: (2 * Math.PI * i) / props.sparkCount,
    startTime: now
  }))

  sparks.value.push(...newSparks)
}

onMounted(() => {
  const canvas = canvasRef.value
  if (!canvas) return

  const resizeCanvas = () => {
    if (canvas.width !== window.innerWidth || canvas.height !== window.innerHeight) {
      canvas.width = window.innerWidth
      canvas.height = window.innerHeight
    }
  }

  window.addEventListener('resize', resizeCanvas)
  resizeCanvas()

  animationId = requestAnimationFrame(draw)

  onUnmounted(() => {
    window.removeEventListener('resize', resizeCanvas)
    if (animationId) {
      cancelAnimationFrame(animationId)
    }
  })
})
</script>
