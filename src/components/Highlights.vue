<template>
  <div class="w-full max-w-5xl mx-auto mt-20 px-4 pb-16">

    <div ref="scrollContainer" class="flex overflow-x-auto gap-32 py-12 px-12 snap-x snap-mandatory scrollbar-hide"
      @mouseenter="isPaused = true" @mouseleave="isPaused = false">
      <div class="flex gap-32 min-w-full">
        <div v-for="(highlight, index) in highlights" :key="index" class="snap-center shrink-0">
          <TiltedCard :isFocused="currentIndex === index" :imageSrc="highlight.image" :altText="highlight.alt"
            :captionText="highlight.caption" containerHeight="300px" containerWidth="300px" imageHeight="300px"
            imageWidth="300px" :rotateAmplitude="12" :scaleOnHover="1.2" :showMobileWarning="false" :showTooltip="true"
            :displayOverlayContent="true">
            <template #overlay>
              <p class="tilted-card-demo-text text-white font-bold text-lg p-4">
                {{ highlight.text }}
              </p>
            </template>
          </TiltedCard>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import TiltedCard from './design/TiltedCard.vue'
import imageMtKulago from '../assets/images/image 5.jpg'
import imageBohol from '../assets/images/image.png'
import imageGameExpo from '../assets/images/IMG_4199.JPG'
import imageDjangoGirls from '../assets/images/django girls coach.jpg'
import imageDataEngineering from '../assets/images/image copy.png'

const scrollContainer = ref(null)
const currentIndex = ref(0)
const isPaused = ref(false)
let intervalId = null

const highlights = [
  {
    image: imageDataEngineering,
    alt: 'Data Engineering Workshop',
    caption: 'Data Engineering Workshop',
    text: 'Attend Workshop In Data Engineering Cebu'
  },
  {
    image: imageGameExpo,
    alt: 'Game Expo',
    caption: 'College Game Expo',
    text: 'Game Expo - Software Dev Majors'
  },
  {
    image: imageDjangoGirls,
    alt: 'Django Girls Coach',
    caption: 'Django Girls Achievement',
    text: 'Coaching at Django Girls'
  },

  {
    image: imageMtKulago,
    alt: 'Hiking in Mt. Kulago',
    caption: 'Mt. Kulago Adventure',
    text: 'Hiking in Mt. Kulago'
  },
  {
    image: imageBohol,
    alt: 'Travel in Bohol',
    caption: 'Bohol Travel',
    text: 'Travel in Bohol'
  },

]

const scrollNext = () => {
  if (isPaused.value || !scrollContainer.value) return

  // Advance index logic
  const items = scrollContainer.value.querySelectorAll('.snap-center')
  if (items.length === 0) return

  currentIndex.value = (currentIndex.value + 1) % items.length

  // Scroll to new current item
  const item = items[currentIndex.value]

  // Center alignment calculation
  const container = scrollContainer.value
  const itemLeft = item.offsetLeft
  const itemWidth = item.offsetWidth
  const containerWidth = container.offsetWidth

  const scrollTo = itemLeft - (containerWidth / 2) + (itemWidth / 2)

  container.scrollTo({
    left: scrollTo,
    behavior: 'smooth'
  })
}

onMounted(() => {
  // Start auto-scroll loop (every 3 seconds)
  intervalId = setInterval(scrollNext, 3000)
})

onUnmounted(() => {
  if (intervalId) clearInterval(intervalId)
})
</script>

<style scoped>
.tilted-card-demo-text {
  color: #ffffff !important;
  text-shadow: none !important;
}

:global(.portfolio-shell.theme-light) .tilted-card-demo-text {
  color: #ffffff !important;
  text-shadow: none !important;
}
</style>
