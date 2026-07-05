<template>
  <footer class="footer-compact allow-xs mt-4 w-full py-4">
    <div class="max-w-5xl mx-auto px-4 flex flex-col md:flex-row items-center justify-between gap-2">

      <!-- Left: Copyright -->
      <div class="footer-copy font-medium text-slate-400">
        &copy; 2024 Melanie Abalde. All rights preserved.
      </div>

      <!-- Right: Tech Stack -->
      <div class="flex items-center space-x-2">
        <p class="footer-title font-bold text-purple-300 uppercase tracking-widest">Tech Stack</p>

        <!-- Vue.js -->
        <div class="group relative flex flex-col items-center">
          <div
            class="footer-icon h-5 w-5 flex items-center justify-center rounded-md bg-green-50 text-green-600 shadow-sm transition-transform hover:scale-110">
            <svg viewBox="0 0 24 24" class="h-2.5 w-2.5 fill-current" xmlns="http://www.w3.org/2000/svg">
              <path d="M2 3h2.553l6.447 11.071L17.447 3H20L11 19 2 3z" />
              <path d="M5.5 3h3.5L11 6.3 13 3h3.5L11 12.6 5.5 3z" fill="#35495E" />
            </svg>
          </div>
        </div>

        <!-- Tailwind CSS -->
        <div class="group relative flex flex-col items-center">
          <div
            class="footer-icon h-5 w-5 flex items-center justify-center rounded-md bg-cyan-50 text-cyan-500 shadow-sm transition-transform hover:scale-110">
            <svg viewBox="0 0 24 24" class="h-2.5 w-2.5 fill-current" xmlns="http://www.w3.org/2000/svg">
              <path
                d="M12.001,4.8c-3.2,0-5.2,1.6-6,4.8c1.2-1.6,2.6-2.2,4.2-1.8c0.913,0.228,1.565,0.89,2.288,1.624 C13.666,10.618,15.027,12,18.001,12c3.2,0,5.2-1.6,6-4.8c-1.2,1.6-2.6,2.2-4.2,1.8c-0.913-0.228-1.565-0.89-2.288-1.624 C16.337,6.182,14.976,4.8,12.001,4.8z M6.001,12c-3.2,0-5.2,1.6-6,4.8c1.2-1.6,2.6-2.2,4.2-1.8c0.913,0.228,1.565,0.89,2.288,1.624 c1.177,1.194,2.538,2.576,5.512,2.576c3.2,0,5.2-1.6,6-4.8c-1.2,1.6-2.6,2.2-4.2,1.8c-0.913-0.228-1.565-0.89-2.288-1.624 C10.337,13.382,8.976,12,6.001,12z" />
            </svg>
          </div>
        </div>

        <!-- Vite -->
        <div class="group relative flex flex-col items-center">
          <div
            class="footer-icon h-5 w-5 flex items-center justify-center rounded-md bg-purple-50 text-purple-600 shadow-sm transition-transform hover:scale-110">
            <svg viewBox="0 0 24 24" class="h-2.5 w-2.5 fill-current" xmlns="http://www.w3.org/2000/svg">
              <path d="M2.67 2.04h18.66l-1.6 2.9-7.73 17.02L4.27 4.94l-1.6-2.9z" fill="#ffb433" />
              <path d="M6.3 4.94h11.4l-5.7 13.84z" fill="#fff" />
            </svg>
          </div>
        </div>
      </div>

    </div>
  </footer>
</template>

<style scoped>
.footer-compact {
  background: transparent;
  border-top: 0;
}

.footer-copy,
.footer-title {
  font-size: 10px !important;
  line-height: 1.2;
}

.footer-title {
  letter-spacing: 0.14em;
}
</style>
