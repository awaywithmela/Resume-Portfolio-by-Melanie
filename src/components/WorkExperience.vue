<template>
    <FolderCard title="Work Experience">
        <div class="flex flex-col md:flex-row gap-6">
            <!-- Sidebar (Company List) -->
            <!-- Sidebar (Company List) -->
            <div
                class="md:w-1/3 flex md:flex-col gap-1 overflow-x-auto md:overflow-visible pb-2 md:pb-0 border-b md:border-b-0 md:border-r border-slate-200 pr-0">
                <button v-for="(job, index) in experiences" :key="index" @click="selectedJob = job"
                    class="group px-4 py-3 text-left text-xs font-bold tracking-wide transition-all duration-200 border-r-2 md:border-r-4 md:border-l-0 md:mr-[-2px] uppercase whitespace-nowrap md:whitespace-normal"
                    :class="selectedJob.company === job.company ? 'text-purple-700 border-purple-500 bg-transparent hover:bg-purple-50' : 'text-slate-400 border-transparent hover:bg-purple-50 hover:text-purple-700'">
                    {{ job.company }}
                </button>
            </div>

            <!-- Content Area -->
            <div class="flex-1 min-h-[300px]">
                <Transition name="fade" mode="out-in">
                    <div :key="selectedJob.company" class="space-y-4">
                        <!-- Header -->
                        <div>
                            <h3 class="text-lg font-bold text-slate-800">{{ selectedJob.role }}</h3>
                            <div class="flex flex-wrap gap-2 items-center mt-1">
                                <span class="text-xs text-purple-600 font-bold bg-purple-50 px-2 py-1 rounded">{{
                                    selectedJob.date }}</span>
                                <span class="text-xs text-slate-400">@ {{ selectedJob.company }}</span>
                            </div>
                        </div>

                        <!-- Description -->
                        <ul class="space-y-3">
                            <li v-for="(point, i) in selectedJob.points" :key="i" class="flex items-start gap-3">
                                <span class="text-purple-400 mt-1.5 shrink-0">✦</span>
                                <span class="text-xs text-slate-600 leading-relaxed">{{ point }}</span>
                            </li>
                        </ul>

                        <!-- Tech Stack Pills -->
                        <div v-if="selectedJob.tech && selectedJob.tech.length" class="pt-2">
                            <div class="flex flex-wrap gap-2">
                                <span v-for="(tech, tIndex) in selectedJob.tech" :key="tIndex"
                                    class="px-3 py-1 bg-slate-100 text-slate-600 rounded-full text-[10px] font-bold uppercase tracking-wider">
                                    {{ tech }}
                                </span>
                            </div>
                        </div>
                    </div>
                </Transition>
            </div>
        </div>
    </FolderCard>
</template>

<script setup>
import { ref } from 'vue'
import FolderCard from './FolderCard.vue'

const experiences = [
    {
        company: "Just Click IT Solution",
        role: "Fullstack Developer",
        date: "2023 – 2025",
        location: "Remote | Cebu City",
        points: [
            "Designed responsive UI/UX layouts using Figma, ensuring intuitive and user-friendly interfaces.",
            "Developed user-centered web applications using React.js and modern frontend best practices.",
            "Implemented SEO optimization techniques to improve search engine visibility and performance.",
            "Conducted end-to-end (E2E) testing using Cypress to ensure application reliability.",
            "Managed cloud deployment and hosting using cPanel.",
            "Maintained backend systems built with Python (Django REST Framework).",
            "Handled database design, management, and optimization using MySQL."
        ],
        tech: ["Figma", "React.js", "SEO", "Cypress", "cPanel", "Python", "Django", "MySQL"]
    },
    {
        company: "PHINMA-CDO College",
        role: "Lead Developer & Project Manager",
        date: "2024 – 2025",
        location: "Cagayan De Oro",
        points: [
            "Led the development of a Reservation Monitoring System using C# (ASP.NET), GraphQL, RESTful APIs, MySQL, and React.js, supporting real-time tracking of reservations.",
            "Managed project planning, task delegation, and progress tracking using Trello, ensuring on-time delivery of key milestones.",
            "Refactored 80% of the codebase, improving system performance by up to 40% and reducing load times significantly.",
            "Optimized API performance, reducing response time from ~2s to under 1s for key endpoints.",
            "Conducted API testing and validation using Postman, identifying and resolving critical issues before deployment.",
            "Supported concurrent users and ensured system stability during peak usage."
        ],
        tech: ["C#", "ASP.NET", "GraphQL", "REST API", "MySQL", "React.js", "Trello", "Postman"]
    },
    {
        company: "Innovuze Solution Inc.",
        role: "Project Manager Intern",
        date: "2025 – 2026",
        location: "Office",
        points: [
            "Managed internal projects (LunchBuddies App, RevePay) using Azure DevOps.",
            "Monitored and resolved bug tickets to improve system performance.",
            "Used Trello to streamline team collaboration and task tracking.",
            "Performed data scraping and analysis to assess project health.",
            "Built dashboards in Looker Studio for data-driven reporting.",
            "Documented Minutes of Meetings (MoM) for team alignment.",
            "Created SOPs, SOWs, and proposals to standardize processes.",
            "Applied prompt engineering techniques using Claude AI, Ollama, and Codex for productivity and development support."
        ],
        tech: ["Azure DevOps", "Trello", "Looker Studio", "Claude AI", "Ollama", "Codex"]
    }
]

const selectedJob = ref(experiences[0])
</script>

<style scoped>
.fade-enter-active,
.fade-leave-active {
    transition: opacity 0.2s ease, transform 0.2s ease;
}

.fade-enter-from {
    opacity: 0;
    transform: translateY(4px);
}

.fade-leave-to {
    opacity: 0;
    transform: translateY(-4px);
}
</style>
