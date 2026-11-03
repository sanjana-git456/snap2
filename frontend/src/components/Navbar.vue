<template>
  <nav class="bg-white border-b border-slate-200 px-6 py-3 flex justify-between items-center sticky top-0 z-50">
    <div class="flex items-center gap-2">
      <Music class="text-primary w-8 h-8" />
      <span class="text-xl font-bold tracking-tight text-slate-800">SnapStage</span>
    </div>
    <div class="flex items-center gap-4">
      <div class="text-right">
        <p class="text-sm font-semibold text-slate-700">{{ auth.user?.username }}</p>
        <p class="text-xs text-slate-500">Reputation: {{ auth.user?.reputation_score || 0 }}</p>
      </div>
      <button @click="handleLogout" class="p-2 hover:bg-slate-100 rounded-full text-slate-600">
        <LogOut class="w-5 h-5" />
      </button>
    </div>
  </nav>
</template>

<script setup>
import { Music, LogOut } from 'lucide-vue-next';
import { useAuthStore } from '../stores/auth';
import { useRouter } from 'vue-router';

const auth = useAuthStore();
const router = useRouter();

const handleLogout = () => {
  auth.logout();
  router.push('/');
};
</script>