<template>
    <div class="w-full mb-12 flex flex-col items-center gap-6">
        <div
            class="project-spotlight-card w-full relative rounded-3xl overflow-hidden bg-[#130924] border border-purple-500/10 text-white shadow-2xl h-[500px] md:h-[600px] flex flex-col items-center justify-end p-8 pb-4 md:p-12 md:pb-6 group transition-all duration-500 font-['Outfit']">

            <!-- Floating Section Title -->
            <h2 class="absolute top-6 left-6 md:top-8 md:left-8 z-10 text-lg md:text-2xl font-bold text-white/90 lowercase tracking-wide">
                school & personal projects
            </h2>

            <!-- Dynamic Background Image with Purple Overlay -->
            <div class="absolute inset-0 z-0">
                <transition name="fade" mode="out-in">
                    <div :key="currentProject.title" class="absolute inset-0 w-full h-full">
                        <!-- Image: object-cover to fit perfectly, opacity adjusted for background fade -->
                        <img :src="currentProject.image" :alt="currentProject.title"
                            class="w-full h-full object-cover object-center opacity-80 transition-transform duration-700 ease-out" />
                        <!-- Deep Purple Gradient Overlay (Lighter for visibility) -->
                        <div
                            class="absolute inset-0 bg-linear-to-t from-[#1a0b2e] via-[#1a0b2e]/50 to-[#1a0b2e]/30 pointer-events-none">
                        </div>
                    </div>
                </transition>
            </div>

            <!-- Main Content -->
            <div class="relative z-10 text-center max-w-4xl mx-auto space-y-2 px-12 md:px-20 pointer-events-none">
                <transition name="slide-fade" mode="out-in">
                    <div :key="currentProject.title" class="flex flex-col items-center space-y-4">

                        <!-- Title (Tall Tales style: lowercase, black weight, cute/geometric) -->
                        <h2
                            class="text-lg md:text-xl font-black tracking-tighter text-white drop-shadow-2xl leading-none lowercase transform hover:scale-105 transition-transform duration-300 pointer-events-auto">
                            {{ currentProject.title }}
                        </h2>

                        <!-- Description -->
                        <p
                            class="text-sm md:text-base text-white font-semibold leading-relaxed drop-shadow-lg max-w-2xl text-center pointer-events-auto">
                            {{ currentProject.description }}
                        </p>

                        <!-- Tech Stack (Purple Accent - matching stylistic choice) -->
                        <div class="flex flex-wrap justify-center gap-3 pt-3 pointer-events-auto">
                            <span
                                class="text-xs md:text-sm text-[#e0c2ff] font-extrabold tracking-widest uppercase drop-shadow-lg font-['Outfit'] bg-purple-900/40 px-3 py-1 rounded-full border border-purple-500/30">
                                {{ currentProject.tech.join(' ✦ ') }}
                            </span>
                        </div>

                        <!-- Icons Row -->
                        <div class="flex items-center justify-center gap-6 pt-4 pointer-events-auto">
                            <a :href="currentProject.link" target="_blank" rel="noopener noreferrer"
                                class="text-white hover:text-[#d8b4fe] transition-colors hover:scale-110 transform duration-200 drop-shadow-lg"
                                title="GitHub">
                                <svg class="w-10 h-10" fill="currentColor" viewBox="0 0 24 24">
                                    <path
                                        d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z" />
                                </svg>
                            </a>
                            <a v-if="currentProject.externalLink" :href="currentProject.externalLink" target="_blank" rel="noopener noreferrer"
                                class="text-white hover:text-[#d8b4fe] transition-colors hover:scale-110 transform duration-200 drop-shadow-lg"
                                title="Visit Site">
                                <svg class="w-10 h-10" fill="none" viewBox="0 0 24 24" stroke="currentColor"
                                    stroke-width="2">
                                    <path stroke-linecap="round" stroke-linejoin="round"
                                        d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14" />
                                </svg>
                            </a>
                        </div>
                    </div>
                </transition>

                <!-- Navigation Arrows -->
                <button @click="prevProject"
                    class="absolute top-1/2 left-4 md:left-6 -translate-y-1/2 p-3 text-white/70 hover:text-white hover:scale-110 transition-all cursor-pointer z-20 bg-black/20 hover:bg-black/40 rounded-full backdrop-blur-sm shadow-lg border border-white/10 pointer-events-auto"
                    aria-label="Previous Project">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8 md:h-10 md:w-10" fill="none"
                        viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M15 19l-7-7 7-7" />
                    </svg>
                </button>
                <button @click="nextProject"
                    class="absolute top-1/2 right-4 md:right-6 -translate-y-1/2 p-3 text-white/70 hover:text-white hover:scale-110 transition-all cursor-pointer z-20 bg-black/20 hover:bg-black/40 rounded-full backdrop-blur-sm shadow-lg border border-white/10 pointer-events-auto"
                    aria-label="Next Project">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8 md:h-10 md:w-10" fill="none"
                        viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M9 5l7 7-7 7" />
                    </svg>
                </button>
            </div>

            <!-- Gradual Blur Component -->
            <!-- zIndex=0 ensures it sits behind the z-10 text content -->
            <GradualBlur position="bottom" height="8rem" :strength="2" :divCount="6" :exponential="true" :zIndex="0"
                preset="intense" curve="ease-in-out" animated="scroll" class="pointer-events-none" />
        </div>

        <!-- Pagination Dots -->
        <div class="flex gap-3">
            <button v-for="(p, index) in projects" :key="index" @click="currentIndex = index"
                class="w-12 h-1.5 rounded-full transition-all duration-300 shadow-sm"
                :class="index === currentIndex ? 'bg-[#d8b4fe] opacity-100' : 'bg-slate-300 hover:bg-slate-400 opacity-50'"></button>
        </div>
    </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import GradualBlur from './design/GradualBlur.vue'

// Import images
import imgMobile from '../assets/images/Mobile.png'
import imgGame from '../assets/images/Game.png'
import imgAMS from '../assets/images/AMS.png'
import imgGSD from '../assets/images/GSD.png'

const currentIndex = ref(0)
const projects = [
    {
        title: "Student Expense Tracker",
        description: "A comprehensive mobile budgeting application designed for students. Features real-time transaction tracking, budget goals, and data visualization.",
        tech: ["Flutter", "FastAPI"],
        image: imgMobile,
        link: "https://github.com/Araanna/FASTAPI-PHINMA-COC-STUDENT-EXPENSE-TRACKER"
    },
    {
        title: "Reservation Monitoring System",
        description: "Capstone project implementing a full-scale reservation and monitoring system for campus facilities, significantly improving administrative efficiency.",
        tech: ["Flutter", "ReactJS", "C#"],
        image: imgGSD,
        link: null,
    },
    {
        title: "Attendance and Management System",
        description: "Attendance and Management System for student campus events and activities.",
        image: imgAMS,
        tech: ["Vuejs", "FastAPI", "MySQL"],
        link: "https://github.com/Araanna/IT-DAYS---ATTENDANCE-MONITORING-SYSTEM"
    },
    {
        title: "Unity RPG Game",
        description: "2D Action RPG implementing classic platformer mechanics, custom physics, inventory systems, and enemy AI behaviors.",
        tech: ["Unity", "C#"],
        image: imgGame,
        link: "https://github.com/Araanna/gamedev_website"
    }
]

const currentProject = computed(() => projects[currentIndex.value])

const nextProject = () => {
    currentIndex.value = (currentIndex.value + 1) % projects.length
}

const prevProject = () => {
    currentIndex.value = (currentIndex.value - 1 + projects.length) % projects.length
}
</script>

<style scoped>
.fade-enter-active,
.fade-leave-active {
    transition: opacity 0.5s ease;
}

.fade-enter-from,
.fade-leave-to {
    opacity: 0;
}

.slide-fade-enter-active {
    transition: all 0.4s ease-out;
}

.slide-fade-leave-active {
    transition: all 0.4s cubic-bezier(1, 0.5, 0.8, 1);
}

.slide-fade-enter-from {
    transform: translateY(20px);
    opacity: 0;
}

.slide-fade-leave-to {
    transform: translateY(-20px);
    opacity: 0;
}
</style>
