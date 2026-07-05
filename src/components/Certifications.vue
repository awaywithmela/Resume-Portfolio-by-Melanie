<template>
    <FolderCard title="Certifications & Training">
        <div class="space-y-3">
            <div v-for="(cert, index) in certifications" :key="index"
                 :class="['flex items-center justify-between rounded-lg p-3 cursor-pointer transition-all hover:scale-[1.02] hover:shadow-md border', cert.bgColor, cert.borderColor]"
                 @click="openModal(cert)">
                <div>
                    <h4 class="font-bold text-xs" :class="cert.textColor">{{ cert.title }}</h4>
                    <p class="text-[10px] font-medium mt-0.5" :class="cert.dateColor">{{ cert.date }}</p>
                </div>
                <!-- Optional: Icon to indicate clickability -->
                <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 opacity-85" :class="cert.textColor" fill="none" viewBox="0 0 24 24"
                    stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                        d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                        d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z" />
                </svg>
            </div>
        </div>

        <!-- Modal Portal -->
        <Teleport to="body">
            <Transition name="fade">
                <div v-if="selectedCert" class="fixed inset-0 z-60 flex items-center justify-center p-4">
                    <!-- Backdrop -->
                    <div class="absolute inset-0 bg-black/60 backdrop-blur-md" @click="closeModal"></div>

                    <!-- Modal Content -->
                    <div class="relative w-full max-w-lg overflow-hidden rounded-2xl bg-white shadow-2xl scale-100">
                        <!-- Close Button -->
                        <button @click="closeModal"
                            class="absolute top-4 right-4 z-10 rounded-full bg-black/20 p-1 text-white hover:bg-black/40 transition-colors">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24"
                                stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                    d="M6 18L18 6M6 6l12 12" />
                            </svg>
                        </button>

                        <!-- Image Area -->
                        <div class="w-full h-auto bg-transparent flex items-center justify-center overflow-hidden">
                            <img v-if="selectedCert.image" :src="selectedCert.image" :alt="selectedCert.title"
                                class="w-full h-auto block" />
                            <div v-else class="text-slate-300 flex flex-col items-center">
                                <svg xmlns="http://www.w3.org/2000/svg" class="h-12 w-12 mb-2" fill="none"
                                    viewBox="0 0 24 24" stroke="currentColor">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"
                                        d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z" />
                                </svg>
                                <span class="text-xs">Image Placeholder</span>
                            </div>
                        </div>

                        <!-- Content Area -->
                        <div class="p-6">
                            <h3 class="text-xl font-bold text-slate-800 mb-1">{{ selectedCert.title }}</h3>
                            <p class="text-xs text-purple-600 font-semibold mb-4">{{ selectedCert.date }}</p>
                            <p class="text-sm text-slate-600 leading-relaxed">
                                {{ selectedCert.description }}
                            </p>
                        </div>
                    </div>
                </div>
            </Transition>
        </Teleport>
    </FolderCard>
</template>

<script setup>
import { ref } from 'vue'
import FolderCard from './FolderCard.vue'

// Import Certificate Images
import imgPyTsada from '../assets/images/PyTsada.jpg'
import imgTesda from '../assets/images/TesdaCert.jpg'
import imgVolunteers from '../assets/images/Volunteers.png'
import imgWordPress from '../assets/images/WordPress.jpg'
import imgGoogle from '../assets/images/Google Certificate.jpg'
import imgFligno from '../assets/images/Fligno.jpeg'
import imgFastAPI from '../assets/images/FastAPI.png'

const certifications = [
    {
        title: "User Interface Designer (TESDA)",
        date: "Aug 2024",
        bgColor: "bg-orange-500/10",
        borderColor: "border-orange-500/20",
        textColor: "text-orange-200",
        dateColor: "text-orange-300/70",
        description: "Completed intensive UI design training focused on usability principles, layout systems, and responsive prototyping.",
        image: imgTesda
    },
    {
        title: "Linux Fundamentals (Fligno)",
        date: "Sep 2022",
        bgColor: "bg-pink-500/10",
        borderColor: "border-pink-500/20",
        textColor: "text-pink-200",
        dateColor: "text-pink-300/70",
        description: "Gained foundational knowledge in Linux-based environments, terminal commands, and server configuration.",
        image: imgFligno
    },
    {
        title: "Build with AI 2025 (Google Developer Group CDO)",
        date: "May 2025",
        bgColor: "bg-blue-500/10",
        borderColor: "border-blue-500/20",
        textColor: "text-blue-200",
        dateColor: "text-blue-300/70",
        description: "Participated in a community-driven event exploring AI-powered applications, integrating Google AI tools and APIs for real-world projects.",
        image: imgGoogle
    },
    {
        title: "Copilot CDO: AI-Powered Coding for Everyone (DevCon CDO)",
        date: "Aug 2025",
        bgColor: "bg-sky-500/10",
        borderColor: "border-sky-500/20",
        textColor: "text-sky-200",
        dateColor: "text-sky-300/70",
        description: "Hands-on workshop demonstrating GitHub Copilot for enhanced code generation, debugging, and workflow automation.",
        image: imgVolunteers
    },
    {
        title: "WordPress Campus Connect (WordPress CDO)",
        date: "July 2025",
        bgColor: "bg-indigo-500/10",
        borderColor: "border-indigo-500/20",
        textColor: "text-indigo-200",
        dateColor: "text-indigo-300/70",
        description: "Engaged in collaborative sessions on WordPress development, site deployment, and plugin customization for campus projects.",
        image: imgWordPress
    },
    {
        title: "FASTAPI (UDEMY)",
        date: "Nov 28, 2025",
        bgColor: "bg-emerald-500/10",
        borderColor: "border-emerald-500/20",
        textColor: "text-emerald-200",
        dateColor: "text-emerald-300/70",
        description: "Completed training in FastAPI, Git, Django, and Python fundamentals, gaining hands-on experience in building and documenting scalable RESTful APIs, version control and collaboration, web application development, and core programming concepts.",
        image: imgFastAPI
    }
]

const selectedCert = ref(null)

const openModal = (cert) => {
    selectedCert.value = cert
    document.body.style.overflow = 'hidden' // Prevent background scrolling
}

const closeModal = () => {
    selectedCert.value = null
    document.body.style.overflow = ''
}
</script>

<style scoped>
.fade-enter-active,
.fade-leave-active {
    transition: opacity 0.3s ease;
}

.fade-enter-from,
.fade-leave-to {
    opacity: 0;
}
</style>
