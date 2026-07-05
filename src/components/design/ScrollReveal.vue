<template>
    <div ref="elRef" class="w-full h-full">
        <div class="transition-all duration-700 ease-out transform will-change-transform w-full h-full"
            :class="[isVisible ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-10']">
            <slot />
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

const props = defineProps({
    threshold: {
        type: Number,
        default: 0.1
    },
    once: {
        type: Boolean,
        default: false
    }
})

const elRef = ref(null)
const isVisible = ref(false)
let observer = null

onMounted(() => {
    observer = new IntersectionObserver(([entry]) => {
        if (entry.isIntersecting && entry.intersectionRatio >= props.threshold) {
            isVisible.value = true
            if (props.once && elRef.value) {
                observer.unobserve(elRef.value)
            }
        } else if (!entry.isIntersecting && !props.once) {
            isVisible.value = false
        }
    }, { threshold: [0, props.threshold] })

    if (elRef.value) {
        observer.observe(elRef.value)
    }
})

onUnmounted(() => {
    if (observer) observer.disconnect()
})
</script>
