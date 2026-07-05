<template>
  <ClickSpark
    sparkColor="#bea7e5"
    :sparkSize="10"
    :sparkRadius="15"
    :sparkCount="8"
    :duration="400"
  >
    <div
      class="portfolio-shell min-h-screen bg-[#070312] flex flex-col relative overflow-hidden transition-colors duration-500"
      :class="{ 'theme-light': isLightTheme }"
      @dblclick="toggleTheme"
    >
    <!-- Global SideRays WebGL background -->
    <SideRays :speed="1.2" rayColor1="#FFFFFF" rayColor2="#96c8ff" :intensity="2.0" :spread="2.2" origin="top-right"
      :tilt="12" :saturation="1.5" :blend="0.7" :falloff="1.5" :opacity="0.8"
      class="fixed inset-0 z-0 pointer-events-none opacity-60 transition-opacity duration-500"
      :class="{ 'opacity-0': isLightTheme }" />

    <LiquidEther :colors="['#4f1fff', '#FF9FFC', '#886bf2']" :mouseForce="20" :cursorSize="100" :isViscous="true"
      :viscous="30" :iterationsViscous="32" :iterationsPoisson="32" :resolution="0.5" :isBounce="true" :autoDemo="true"
      :autoSpeed="0.5" :autoIntensity="2.2" :takeoverDuration="0.25" :autoResumeDelay="3000" :autoRampDuration="0.6"
      class="fixed top-0 left-0 z-0 opacity-40 transition-opacity duration-500"
      :class="{ 'opacity-0': isLightTheme }" />

    <!-- Global PixelBlast, constrained to the lower half of the viewport -->
    <div class="pixel-blast-layer fixed inset-x-0 bottom-0 h-[50vh] z-[1] pointer-events-none opacity-85">
      <PixelBlast
        variant="square"
        :pixelSize="6"
        :color="isLightTheme ? '#ffffff' : '#B497CF'"
        :patternScale="3"
        :patternDensity="2.5"
        :pixelSizeJitter="0.5"
        :enableRipples="true"
        :rippleSpeed="0.4"
        :rippleThickness="0.12"
        :rippleIntensityScale="1.5"
        :liquid="false"
        :liquidStrength="0.12"
        :liquidRadius="1.2"
        :liquidWobbleSpeed="5"
        :speed="0.6"
        :edgeFade="0.25"
        :transparent="true"
      />
    </div>

    <div class="relative z-10 flex-1 w-full max-w-5xl mx-auto py-10 px-4 md:px-8 space-y-12">

      <!-- Top Profile Section -->
      <ProfileCard />

      <!-- About Me -->
      <ScrollReveal>
        <AboutMe />
      </ScrollReveal>

      <!-- Main Content Grid -->
      <div class="grid grid-cols-1 gap-6 md:grid-cols-2 items-start">

        <!-- Left Column -->
        <div class="space-y-6">


          <!-- Work Experience -->
          <ScrollReveal :delay="100">
            <WorkExperience />
          </ScrollReveal>

          <!-- Community & Leadership -->
          <ScrollReveal :delay="200">
            <div class="community-leadership allow-xs">
              <FolderCard title="Community & Leadership">
                <!-- Item 1 -->
                <div class="mb-5">
                  <div class="flex justify-between items-center mb-1">
                    <h3 class="font-bold text-slate-800 text-sm">Volunteer Coach</h3>
                    <span class="rounded-lg bg-pink-100 px-2 py-0.5 text-[10px] font-bold text-pink-600">July 2025</span>
                  </div>
                  <p class="text-xs text-slate-500 italic mb-1">Django Girls CDO</p>
                  <p class="text-xs text-slate-600">Guided first-time developers in building Python/Django apps.</p>
                </div>

                <!-- Item 2 -->
                <div class="mb-5">
                  <div class="flex justify-between items-center mb-1">
                    <h3 class="font-bold text-slate-800 text-sm">Fullstack Bootcamp</h3>
                    <span class="rounded-lg bg-blue-100 px-2 py-0.5 text-[10px] font-bold text-blue-600">May 2024</span>
                  </div>
                  <p class="text-xs text-slate-500 italic mb-1">Fligno</p>
                  <p class="text-xs text-slate-600">Backend with Laravel, Frontend with React/Redux.</p>
                </div>

                <!-- Item 3 -->
                <div>
                  <div class="flex justify-between items-center mb-1">
                    <h3 class="font-bold text-slate-800 text-sm">SBO Associate Treasurer</h3>
                    <span class="rounded-lg bg-green-100 px-2 py-0.5 text-[10px] font-bold text-green-600">July
                      2021</span>
                  </div>
                  <p class="text-xs text-slate-500 italic mb-1">Student Body Organization</p>
                  <p class="text-xs text-slate-600">Financial management and event planning.</p>
                </div>
              </FolderCard>
            </div>
          </ScrollReveal>
        </div>

        <!-- Right Column -->
        <div class="space-y-6">
          <!-- Education -->
          <ScrollReveal :delay="100">
            <div class="education-card allow-xs">
              <FolderCard title="Education">
                <div class="mb-4">
                  <div class="flex justify-between items-start mb-1">
                    <h3 class="text-sm font-bold text-slate-800">BS in Information Technology</h3>
                    <span
                      class="rounded-full bg-purple-100 px-3 py-1 text-[10px] font-bold text-purple-600 whitespace-nowrap ml-2">Dean's
                      Lister</span>
                  </div>
                  <p class="text-xs text-slate-500 italic mb-2">PHINMA – Cagayan de Oro College</p>
                  <ul class="space-y-2 text-xs text-slate-600">
                    <li class="flex items-start gap-2"><span class="text-purple-400 mt-[2px]">✦</span><span>Major in
                        System
                        Development</span></li>
                    <li class="flex items-start gap-2"><span class="text-purple-400 mt-[2px]">✦</span><span>Dean's Lister
                        1st & 2nd Semester, 2021</span></li>
                  </ul>
                </div>
              </FolderCard>
            </div>
          </ScrollReveal>

          <!-- Certifications & Training -->
          <ScrollReveal :delay="200">
            <Certifications />
          </ScrollReveal>

          <!-- Skills -->
          <ScrollReveal :delay="300">
            <FolderCard title="Core Skills">
              <div class="flex flex-wrap gap-2">
                <span class="px-3 py-1 bg-slate-100 text-slate-600 rounded-full text-xs font-semibold">Python
                  (Django)</span>
                <span class="px-3 py-1 bg-blue-100 text-blue-600 rounded-full text-xs font-semibold">React.js</span>
                <span class="px-3 py-1 bg-green-100 text-green-600 rounded-full text-xs font-semibold">Vue.js</span>
                <span class="px-3 py-1 bg-black text-white rounded-full text-xs font-semibold">Next.js</span>
                <span class="px-3 py-1 bg-cyan-100 text-cyan-600 rounded-full text-xs font-semibold">Tailwind CSS</span>
                <span
                  class="px-3 py-1 bg-purple-100 text-purple-600 rounded-full text-xs font-semibold">Bootstrap</span>
                <span
                  class="px-3 py-1 bg-orange-100 text-orange-600 rounded-full text-xs font-semibold">HTML5/CSS3</span>
                <span class="px-3 py-1 bg-yellow-100 text-yellow-600 rounded-full text-xs font-semibold">MySQL</span>
                <span class="px-3 py-1 bg-red-100 text-red-600 rounded-full text-xs font-semibold">RESTful APIs</span>
                <span class="px-3 py-1 bg-slate-200 text-slate-700 rounded-full text-xs font-semibold">Git</span>
                <span class="px-3 py-1 bg-orange-50 text-orange-500 rounded-full text-xs font-semibold">Postman</span>
                <span class="px-3 py-1 bg-blue-50 text-blue-500 rounded-full text-xs font-semibold">Flutter</span>
                <span class="px-3 py-1 bg-indigo-50 text-indigo-500 rounded-full text-xs font-semibold">Figma</span>
              </div>
            </FolderCard>
          </ScrollReveal>
        </div>
      </div>

      <!-- Professional & Client Projects Section -->
      <ScrollReveal>
        <BorderGlow
          className="professional-projects allow-xs w-full relative overflow-hidden"
          :borderRadius="24"
          glowColor="270 70 60"
          backgroundColor="#0b0816"
        >
          <div class="p-8 space-y-6">
            <h2 class="text-2xl font-bold text-white lowercase">Professional & Client Projects</h2>

            <ChromaGrid 
              :radius="340"
              :damping="0.4"
              :fadeOut="0.5"
              ease="power3.out"
            >
              <div class="grid grid-cols-1 md:grid-cols-2 gap-6 relative z-10">

              <!-- Project: Interviewer Self-Service Portal (iReach Timesheet) -->
              <BorderGlow className="h-full rounded-xl overflow-hidden relative">
                <div
                  class="group flex flex-col justify-between p-6 transition-all hover:-translate-y-1 h-full text-slate-800">
                  <div class="flex-grow flex flex-col justify-between h-full">
                    <!-- Text Info -->
                    <div class="flex-grow flex flex-col justify-start">
                      <div class="mb-4 flex items-center justify-between text-purple-600">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8" fill="none" viewBox="0 0 24 24"
                          stroke="currentColor" stroke-width="1.5">
                          <path stroke-linecap="round" stroke-linejoin="round"
                            d="M9.75 17L9 20l-1 1h8l-1-1-.75-3M3 13h18M5 17h14a2 2 0 002-2V5a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
                        </svg>
                        <div class="flex gap-3 items-center">
                          <span
                            class="text-[10px] font-bold text-purple-600 bg-purple-50 px-2 py-0.5 rounded tracking-wide uppercase">Sybergate
                            NZ Ltd</span>
                          <a href="https://timesheet.ipsos.co.nz" target="_blank" rel="noopener noreferrer"
                            class="text-purple-500 hover:text-purple-700 transition-colors" title="Visit Site">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24"
                              stroke="currentColor" stroke-width="2">
                              <path stroke-linecap="round" stroke-linejoin="round"
                                d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h14a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14" />
                            </svg>
                          </a>
                        </div>
                      </div>
                      <h3 class="mb-2 text-lg font-bold text-slate-800 group-hover:text-purple-600 transition-colors">
                        Interviewer Self-Service Portal <br /> (iReach Timesheet)</h3>
                      <p class="mb-4 text-sm leading-relaxed text-slate-600">
                        A secure, responsive timesheet logging system built for Ipsos field interviewers. Features
                        offline-first entry, detailed time tracking (in-field, admin, travel), receipt uploads, and
                        real-time validation.
                      </p>
                    </div>

                    <!-- Interactive Image Preview Section with Borders -->
                    <div class="my-4 space-y-3 mt-auto">
                      <div
                        class="relative overflow-hidden rounded-lg border-2 border-white/10 bg-white/5 shadow-xs aspect-video">
                        <img :src="ireachScreenshots[activeScreenshotIdx]"
                          :alt="'iReach Timesheet screenshot - ' + ireachTitles[activeScreenshotIdx]"
                          class="w-full h-full object-cover transition-all duration-300" />
                        <div class="absolute bottom-0 inset-x-0 bg-black/60 px-3 py-1.5 text-center">
                          <span class="text-[11px] font-bold text-white tracking-wide uppercase">{{
                            ireachTitles[activeScreenshotIdx] }}</span>
                        </div>
                      </div>
                      <!-- Thumbnails with Borders -->
                      <div class="flex gap-2.5 justify-center">
                        <button v-for="(img, idx) in ireachScreenshots" :key="idx" @click="activeScreenshotIdx = idx"
                          class="w-14 h-9 rounded-md border border-white/10 overflow-hidden transition-all duration-200 hover:scale-105 shadow-xs"
                          :class="activeScreenshotIdx === idx ? 'border-purple-600 ring-2 ring-purple-100/20 scale-105' : 'border-white/10 hover:border-white/20'"
                          :title="ireachTitles[idx]">
                          <img :src="img" :alt="ireachTitles[idx]" class="w-full h-full object-cover" />
                        </button>
                      </div>
                    </div>

                    <div class="flex flex-wrap gap-2 text-xs font-medium text-slate-500 mt-2">
                      <span>Flutter</span>
                      <span>Dart</span>
                      <span>RESTful APIs</span>
                      <span>Responsive Web</span>
                    </div>
                  </div>
                </div>
              </BorderGlow>

              <!-- Project: SureLife Client Project -->
              <BorderGlow className="h-full rounded-xl overflow-hidden relative">
                <div
                  class="group flex flex-col justify-between p-6 transition-all hover:-translate-y-1 h-full text-slate-800">
                  <div class="flex-grow flex flex-col justify-between h-full">
                    <!-- Text Info -->
                    <div class="flex-grow flex flex-col justify-start">
                      <div class="mb-4 flex items-center justify-between text-purple-600">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8" fill="none" viewBox="0 0 24 24"
                          stroke="currentColor" stroke-width="1.5">
                          <path stroke-linecap="round" stroke-linejoin="round"
                            d="M3 7v10a2 2 0 002 2h14a2 2 0 002-2V9a2 2 0 00-2-2h-6l-2-2H5a2 2 0 00-2 2z" />
                        </svg>
                        <div class="flex gap-3 items-center">
                          <span
                            class="text-[10px] font-bold text-purple-600 bg-purple-50 px-2 py-0.5 rounded tracking-wide uppercase border border-purple-800/30">Just
                            Click IT Solution</span>
                          <a href="https://surelifenetworkglobal.co/slc" target="_blank" rel="noopener noreferrer"
                            class="text-purple-400 hover:text-purple-300 transition-colors" title="Visit Site">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24"
                              stroke="currentColor" stroke-width="2">
                              <path stroke-linecap="round" stroke-linejoin="round"
                                d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h14a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14" />
                            </svg>
                          </a>
                        </div>
                      </div>
                      <h3 class="mb-2 text-lg font-bold text-slate-800 group-hover:text-purple-600 transition-colors">
                        SureLife Client Project</h3>
                      <p class="mb-4 text-sm leading-relaxed text-slate-600">
                        A professional healthcare and insurance administration system (SureLife) developed during my time at
                        Just Click IT Solution in Cebu, delivering high-quality software solutions and technical expertise.
                      </p>
                    </div>

                    <!-- Screenshot with Borders -->
                    <div class="my-4 space-y-3 mt-auto">
                      <div
                        class="relative overflow-hidden rounded-lg border-2 border-white/10 bg-white/5 shadow-xs aspect-video">
                        <img :src="surelifeProjectImage" alt="SureLife Project screenshot"
                          class="w-full h-full object-cover" />
                      </div>
                      <!-- Invisible thumbnail placeholders to align with left card -->
                      <div class="flex gap-2.5 justify-center invisible select-none pointer-events-none">
                        <div class="w-14 h-9 rounded-md border border-transparent"></div>
                      </div>
                    </div>

                    <div class="flex flex-wrap gap-2 text-xs font-medium text-slate-500 mt-2">
                      <span>C#</span>
                      <span>ASP.NET</span>
                      <span>ReactJS</span>
                      <span>Python</span>
                    </div>
                  </div>
                </div>
              </BorderGlow>

            </div>
          </ChromaGrid>
        </div>
      </BorderGlow>
    </ScrollReveal>

      <!-- School & Personal Projects Section -->
      <div class="space-y-6">
        <!-- Featured Project Spotlight -->
        <ScrollReveal>
          <ProjectSpotlight />
        </ScrollReveal>

        <!-- Bento Grid Showcase -->
        <ScrollReveal :delay="100">
          <MagicBento
            :textAutoHide="false"
            :enableStars="true"
            :enableSpotlight="true"
            :enableBorderGlow="true"
            :enableTilt="false"
            :enableMagnetism="true"
            :clickEffect="true"
            :spotlightRadius="290"
            :particleCount="12"
            glowColor="192, 132, 252"
            :disableAnimations="false"
          >
            <!-- Card 1: Siargao Travel Website (Small) -->
            <BentoCard
              :enableTilt="false"
              :enableMagnetism="true"
              :clickEffect="true"
              glowColor="192, 132, 252"
              className="dark-glow-card lg:col-span-2"
            >
              <div class="group flex flex-col justify-between h-full text-slate-100">
                <div class="flex-grow flex flex-col justify-between">
                  <div class="mb-4 flex items-center justify-between text-purple-400">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8" fill="none" viewBox="0 0 24 24"
                      stroke="currentColor" stroke-width="1.5">
                      <path stroke-linecap="round" stroke-linejoin="round"
                        d="M3.055 11H5a2 2 0 012 2v1a2 2 0 002 2 2 2 0 012 2v2.945M8 3.935V5.5A2.5 2.5 0 0010.5 8h.5a2 2 0 012 2 2 2 0 002 2h2m.358-5.363a9 9 0 11-12.727 0M16.5 16.5L19 19" />
                    </svg>
                    <div class="flex gap-3">
                      <a href="https://github.com/Araanna/IT-133-Siargao" target="_blank" rel="noopener noreferrer"
                        class="hover:text-purple-300 transition-colors">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="currentColor" viewBox="0 0 24 24">
                          <path
                            d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z" />
                        </svg>
                      </a>
                      <a href="https://siargaotravel.netlify.app" target="_blank" rel="noopener noreferrer"
                        class="hover:text-purple-300 transition-colors">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24"
                          stroke="currentColor" stroke-width="2">
                          <path stroke-linecap="round" stroke-linejoin="round"
                            d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h14a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14" />
                        </svg>
                      </a>
                    </div>
                  </div>
                  <h3 class="mb-2 text-lg font-bold text-slate-100 group-hover:text-purple-300 transition-colors">Siargao
                    Travel Website</h3>
                  <p class="mb-4 text-xs leading-relaxed text-slate-300">
                    A beautiful tourist landing guide highlighting the islands, surfing spots, and resorts of Siargao,
                    designed for responsive web.
                  </p>
                </div>
                <div class="flex flex-wrap gap-2 text-[10px] font-medium text-slate-400">
                  <span>HTML5</span>
                  <span>Bootstrap CSS</span>
                  <span>JavaScript</span>
                </div>
              </div>
            </BentoCard>

            <!-- Card 2: Student Expense Tracker (Small) -->
            <BentoCard
              :enableTilt="false"
              :enableMagnetism="true"
              :clickEffect="true"
              glowColor="192, 132, 252"
              className="dark-glow-card lg:col-span-2"
            >
              <div class="group flex flex-col justify-between h-full text-slate-100">
                <div class="flex-grow flex flex-col justify-between">
                  <div class="mb-4 flex items-center justify-between text-purple-400">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8" fill="none" viewBox="0 0 24 24"
                      stroke="currentColor" stroke-width="1.5">
                      <path stroke-linecap="round" stroke-linejoin="round"
                        d="M3 7v10a2 2 0 002 2h14a2 2 0 002-2V9a2 2 0 00-2-2h-6l-2-2H5a2 2 0 00-2 2z" />
                    </svg>
                    <div class="flex gap-3">
                      <a href="https://github.com/Araanna/FASTAPI-PHINMA-COC-STUDENT-EXPENSE-TRACKER" target="_blank" rel="noopener noreferrer"
                        class="hover:text-purple-300 transition-colors">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="currentColor" viewBox="0 0 24 24">
                          <path
                            d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z" />
                        </svg>
                      </a>
                    </div>
                  </div>
                  <h3 class="mb-2 text-lg font-bold text-slate-100 group-hover:text-purple-300 transition-colors">Student
                    Expense Tracker</h3>
                  <p class="mb-4 text-xs leading-relaxed text-slate-300">
                    Mobile budgeting app enabling students to track expenses and set budgets with transaction APIs.
                  </p>
                </div>
                <div class="flex flex-wrap gap-2 text-[10px] font-medium text-slate-400">
                  <span>Flutter</span>
                  <span>FastAPI</span>
                </div>
              </div>
            </BentoCard>

            <!-- Card 3: Unity RPG Game (Small) -->
            <BentoCard
              :enableTilt="false"
              :enableMagnetism="true"
              :clickEffect="true"
              glowColor="192, 132, 252"
              className="dark-glow-card lg:col-span-1"
            >
              <div class="group flex flex-col justify-between h-full text-slate-100">
                <div class="flex-grow flex flex-col justify-between">
                  <div class="mb-4 flex items-center justify-between text-purple-400">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8" fill="none" viewBox="0 0 24 24"
                      stroke="currentColor" stroke-width="1.5">
                      <path stroke-linecap="round" stroke-linejoin="round"
                        d="M3 7v10a2 2 0 002 2h14a2 2 0 002-2V9a2 2 0 00-2-2h-6l-2-2H5a2 2 0 00-2 2z" />
                    </svg>
                    <div class="flex gap-3">
                      <a href="https://github.com/Araanna/gamedev_website" target="_blank" rel="noopener noreferrer"
                        class="hover:text-purple-300 transition-colors">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="currentColor" viewBox="0 0 24 24">
                          <path
                            d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z" />
                        </svg>
                      </a>
                    </div>
                  </div>
                  <h3 class="mb-2 text-lg font-bold text-slate-100 group-hover:text-purple-300 transition-colors">Unity
                    RPG Game</h3>
                  <p class="mb-4 text-xs leading-relaxed text-slate-300">
                    2D platformer RPG built in Unity, implementing animation, collision detection, and player movement.
                  </p>
                </div>
                <div class="flex flex-wrap gap-2 text-[10px] font-medium text-slate-400">
                  <span>Unity</span>
                  <span>C#</span>
                </div>
              </div>
            </BentoCard>

            <!-- Card 4: Reservation Monitoring System (Small) -->
            <BentoCard
              :enableTilt="false"
              :enableMagnetism="true"
              :clickEffect="true"
              glowColor="192, 132, 252"
              className="dark-glow-card lg:col-span-3"
            >
              <div class="group flex flex-col justify-between h-full text-slate-100">
                <div class="flex-grow flex flex-col justify-between">
                  <div class="mb-4 flex items-center justify-between text-purple-400">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8" fill="none" viewBox="0 0 24 24"
                      stroke="currentColor" stroke-width="1.5">
                      <path stroke-linecap="round" stroke-linejoin="round"
                        d="M3 7v10a2 2 0 002 2h14a2 2 0 002-2V9a2 2 0 00-2-2h-6l-2-2H5a2 2 0 00-2 2z" />
                    </svg>
                    <div class="flex gap-3">
                      <a href="https://github.com/Araanna/IT-DAYS-WEB-APP" target="_blank" rel="noopener noreferrer"
                        class="hover:text-purple-300 transition-colors">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="currentColor" viewBox="0 0 24 24">
                          <path
                            d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z" />
                        </svg>
                      </a>
                    </div>
                  </div>
                  <h3 class="mb-2 text-lg font-bold text-slate-100 group-hover:text-purple-300 transition-colors">
                    Reservation Monitoring System</h3>
                  <p class="mb-4 text-xs leading-relaxed text-slate-300">
                    Capstone project implementing a full-scale reservation and monitoring system for campus facilities,
                    significantly improving administrative efficiency.
                  </p>
                </div>
                <div class="flex flex-wrap gap-2 text-[10px] font-medium text-slate-400">
                  <span>Flutter</span>
                  <span>ReactJS</span>
                  <span>PHP</span>
                </div>
              </div>
            </BentoCard>
          </MagicBento>
        </ScrollReveal>
      </div>

      <ScrollReveal :delay="200">
        <Highlights />
      </ScrollReveal>
    </div>

    <div ref="footerRef" class="portfolio-footer relative z-[60] transition-colors duration-500">
      <Footer />
    </div>

    <!-- Global Bottom Gradual Blur -->
    <GradualBlur target="page" position="bottom" height="6rem" :strength="2" :divCount="5" :zIndex="50"
      class="fixed bottom-0 left-0 w-full pointer-events-none transition-opacity duration-300"
      :style="{ opacity: isFooterVisible ? 0 : 1 }" />
  </div>
  </ClickSpark>
</template>

<script setup>
import { ref, onMounted, onUnmounted, computed, watch } from 'vue'
import ProfileCard from './components/ProfileCard.vue'
import Certifications from './components/Certifications.vue'
import WorkExperience from './components/WorkExperience.vue'
import BorderGlow from './components/design/BorderGlow.vue'
import MagicBento from './components/design/MagicBento.vue'
import BentoCard from './components/design/BentoCard.vue'
import ChromaGrid from './components/design/ChromaGrid.vue'
import ClickSpark from './components/design/ClickSpark.vue'
import PixelBlast from './components/design/PixelBlast.vue'

const clientProjectItems = computed(() => [
  {
    image: ireachDashboard,
    title: "Interviewer Self-Service Portal (iReach)",
    subtitle: "Flutter • Dart • RESTful APIs • Responsive Web. Features offline-first entry, detailed time tracking, receipt uploads, and real-time validation.",
    handle: "Sybergate NZ Ltd",
    borderColor: "#a855f7",
    gradient: "linear-gradient(145deg, #4f1fff, #120F17)",
    url: "https://timesheet.ipsos.co.nz"
  },
  {
    image: surelifeProjectImage,
    title: "SureLife Client Project",
    subtitle: "C# • ASP.NET • ReactJS • Python. A professional healthcare and insurance administration system delivering high-quality client solutions.",
    handle: "Just Click IT Solution",
    borderColor: "#ec4899",
    gradient: "linear-gradient(145deg, #ec4899, #120F17)",
    url: "https://surelifenetworkglobal.co/slc"
  }
])

import FolderCard from './components/FolderCard.vue'
import Highlights from './components/Highlights.vue'
import Footer from './components/Footer.vue'
import ProjectSpotlight from './components/ProjectSpotlight.vue'
import GradualBlur from './components/design/GradualBlur.vue'
import LiquidEther from './components/design/LiquidEther.vue'
import ScrollReveal from './components/design/ScrollReveal.vue'
import SideRays from './components/design/SideRays.vue'

// Import iReach client project screenshots
import ireachLogin from './assets/images/ireach_login.png'
import ireachDashboard from './assets/images/ireach_dashboard.png'
import ireachTimesheet from './assets/images/ireach_timesheet.png'
import surelifeProjectImage from './assets/images/CebuProject.png'

const ireachScreenshots = [ireachLogin, ireachDashboard, ireachTimesheet]
const ireachTitles = ["Login Page", "Dashboard Overview", "Timesheet Form"]
const activeScreenshotIdx = ref(1) // Default to dashboard screenshot

const isLightTheme = ref(false)
const footerRef = ref(null)
const isFooterVisible = ref(false)
let observer = null

const toggleTheme = () => {
  isLightTheme.value = !isLightTheme.value
}

const syncRootTheme = (enabled) => {
  document.documentElement.classList.toggle('theme-light-root', enabled)
  document.body.classList.toggle('theme-light-root', enabled)
}

watch(isLightTheme, syncRootTheme, { immediate: true })

onMounted(() => {
  observer = new IntersectionObserver(([entry]) => {
    isFooterVisible.value = entry.isIntersecting
  }, { threshold: 0, rootMargin: '100px' })
  if (footerRef.value) {
    observer.observe(footerRef.value)
  }
})

onUnmounted(() => {
  if (observer) observer.disconnect()
  syncRootTheme(false)
})
</script>
