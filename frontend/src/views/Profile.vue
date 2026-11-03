<template>
  <div class="max-w-4xl mx-auto">
    <div class="bg-white rounded-3xl shadow-sm border border-slate-100 overflow-hidden mb-8">
      <div class="h-40 bg-gradient-to-r from-primary to-secondary"></div>
      <div class="px-8 pb-8">
        <div class="relative flex justify-between items-end -mt-12 mb-6">
          <div class="w-24 h-24 bg-white rounded-2xl p-1 shadow-lg">
            <div class="w-full h-full bg-slate-100 rounded-xl flex items-center justify-center text-slate-400">
              <User class="w-12 h-12" />
            </div>
          </div>
          <button class="bg-slate-50 text-slate-700 px-6 py-2 rounded-xl font-bold border border-slate-200 hover:bg-slate-100 transition">Edit Profile</button>
        </div>
        <h1 class="text-3xl font-bold text-slate-800">{{ auth.user?.username }}</h1>
        <p class="text-slate-500 mt-1">{{ auth.user?.email }}</p>
        <p class="mt-4 text-slate-700 max-w-2xl">{{ auth.user?.bio || 'No bio yet. Tell the world about your music!' }}</p>
      </div>
    </div>

    <div class="grid md:grid-cols-3 gap-8">
      <div class="md:col-span-2 space-y-8">
        <section class="bg-white rounded-3xl p-8 border border-slate-100">
          <h2 class="text-xl font-bold mb-6 flex items-center gap-2">
            <Award class="w-6 h-6 text-primary" />
            Earned Badges
          </h2>
          <div class="grid grid-cols-4 gap-4">
            <div v-for="i in 4" :key="i" class="flex flex-col items-center gap-2 grayscale opacity-40">
              <div class="w-16 h-16 bg-slate-100 rounded-full flex items-center justify-center">
                <Award class="w-8 h-8 text-slate-400" />
              </div>
              <span class="text-xs font-bold text-slate-400">Locked</span>
            </div>
          </div>
          <p class="text-center text-slate-400 mt-6 text-sm">Perform more to unlock badges!</p>
        </section>
      </div>

      <div class="space-y-6">
        <div class="bg-white rounded-3xl p-6 border border-slate-100">
          <h3 class="font-bold text-slate-800 mb-4">Stats</h3>
          <div class="space-y-4">
            <div class="flex justify-between">
              <span class="text-slate-500">Reputation</span>
              <span class="font-bold">{{ auth.user?.reputation_score || 0 }}</span>
            </div>
            <div class="flex justify-between">
              <span class="text-slate-500">Followers</span>
              <span class="font-bold">0</span>
            </div>
            <div class="flex justify-between">
              <span class="text-slate-500">Total Jams</span>
              <span class="font-bold">0</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { User, Award } from 'lucide-vue-next';
import { useAuthStore } from '../stores/auth';

const auth = useAuthStore();
</script>