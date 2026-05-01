<template>
    <div ref="elRef" class="transition-all duration-700 ease-out transform will-change-transform"
        :class="[isVisible ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-10']">
        <slot />
    </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

const props = defineProps({
    threshold: {
        type: Number,
        default: 0.1
    }
})

const elRef = ref(null)
const isVisible = ref(false)
let observer = null

onMounted(() => {
    observer = new IntersectionObserver(([entry]) => {
        if (entry.isIntersecting) {
            isVisible.value = true
            if (elRef.value) observer.unobserve(elRef.value)
        }
    }, { threshold: props.threshold })

    if (elRef.value) {
        observer.observe(elRef.value)
    }
})

onUnmounted(() => {
    if (observer) observer.disconnect()
})
</script>
