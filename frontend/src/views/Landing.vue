<template>
  <div class="min-h-screen bg-gradient-to-br from-indigo-600 via-purple-600 to-pink-500 text-white">
    <nav class="max-w-7xl mx-auto px-6 py-8 flex justify-between items-center">
      <div class="flex items-center gap-2">
        <Music class="w-8 h-8" />
        <span class="text-2xl font-bold">SnapStage</span>
      </div>
      <div class="space-x-4">
        <router-link to="/login" class="hover:text-indigo-100 transition">Log in</router-link>
        <router-link to="/register" class="bg-white text-indigo-600 px-6 py-2 rounded-full font-semibold hover:bg-indigo-50 transition">Get started</router-link>
      </div>
    </nav>

    <main class="max-w-7xl mx-auto px-6 pt-20 pb-32">
      <div class="text-center max-w-3xl mx-auto space-y-8">
        <h1 class="text-6xl font-extrabold leading-tight">The Stage for the Next Generation of Talent</h1>
        <p class="text-xl text-indigo-100">Host quick jam sessions, stream mini-concerts, and grow your fanbase with transparent metrics and direct fan support.</p>
        <div class="flex justify-center gap-4">
          <router-link to="/register" class="bg-white text-indigo-600 px-8 py-4 rounded-xl text-lg font-bold shadow-xl hover:scale-105 transition">Start Jamming Now</router-link>
          <router-link to="/login" class="bg-indigo-700/30 backdrop-blur-sm border border-white/20 px-8 py-4 rounded-xl text-lg font-bold hover:bg-indigo-700/50 transition">Explore Talent</router-link>
        </div>
      </div>

      <div class="grid md:grid-cols-3 gap-8 mt-32">
        <div class="bg-white/10 backdrop-blur-md p-8 rounded-2xl border border-white/10">
          <Radio class="w-12 h-12 mb-6 text-pink-300" />
          <h3 class="text-2xl font-bold mb-4">One-Click Jam Rooms</h3>
          <p class="text-indigo-100">Instantly go live and collaborate with other musicians in real-time with zero friction.</p>
        </div>
        <div class="bg-white/10 backdrop-blur-md p-8 rounded-2xl border border-white/10">
          <Ticket class="w-12 h-12 mb-6 text-indigo-300" />
          <h3 class="text-2xl font-bold mb-4">Micro-Event Tickets</h3>
          <p class="text-indigo-100">Sell virtual tickets for pop-up concerts and keep the majority of your earnings.</p>
        </div>
        <div class="bg-white/10 backdrop-blur-md p-8 rounded-2xl border border-white/10">
          <Award class="w-12 h-12 mb-6 text-emerald-300" />
          <h3 class="text-2xl font-bold mb-4">Reputation Badges</h3>
          <p class="text-indigo-100">Earn badges for consistent performances and high audience engagement.</p>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup>
import { Music, Radio, Ticket, Award } from 'lucide-vue-next';
</script>