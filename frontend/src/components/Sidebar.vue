<template>
  <aside class="w-64 bg-white border-r border-slate-200 min-h-[calc(100vh-64px)] p-4 hidden md:block">
    <div class="space-y-2">
      <router-link 
        v-for="item in menuItems" 
        :key="item.path" 
        :to="item.path"
        class="flex items-center gap-3 px-4 py-3 rounded-xl transition-colors"
        :class="route.path === item.path ? 'bg-indigo-50 text-primary' : 'text-slate-600 hover:bg-slate-50'"
      >
        <component :is="item.icon" class="w-5 h-5" />
        <span class="font-medium">{{ item.name }}</span>
      </router-link>
    </div>
  </aside>
</template>

<script setup>
import { LayoutDashboard, Radio, Calendar, User } from 'lucide-vue-next';
import { useRoute } from 'vue-router';

const route = useRoute();

const menuItems = [
  { name: 'Dashboard', path: '/dashboard', icon: LayoutDashboard },
  { name: 'Jam Rooms', path: '/rooms', icon: Radio },
  { name: 'Events', path: '/events', icon: Calendar },
  { name: 'Profile', path: '/profile', icon: User },
];
</script>