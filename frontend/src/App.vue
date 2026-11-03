<template>
  <div class="min-h-screen">
    <Navbar v-if="showNav" />
    <div :class="{'flex': showNav}">
      <Sidebar v-if="showNav" />
      <main :class="{'flex-1 p-8': showNav, 'w-full': !showNav}">
        <router-view></router-view>
      </main>
    </div>
  </div>
</template>

<script setup>
import { computed, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import { useAuthStore } from './stores/auth';
import Navbar from './components/Navbar.vue';
import Sidebar from './components/Sidebar.vue';

const route = useRoute();
const auth = useAuthStore();

const showNav = computed(() => {
  return !['/', '/login', '/register'].includes(route.path);
});

onMounted(() => {
  if (auth.isAuthenticated) {
    auth.fetchMe();
  }
});
</script>