import { createRouter, createWebHistory } from 'vue-router';
import Landing from './views/Landing.vue';
import Login from './views/Login.vue';
import Register from './views/Register.vue';
import Dashboard from './views/Dashboard.vue';
import JamRooms from './views/JamRooms.vue';
import Events from './views/Events.vue';
import Profile from './views/Profile.vue';
import { useAuthStore } from './stores/auth';

const routes = [
  { path: '/', component: Landing },
  { path: '/login', component: Login },
  { path: '/register', component: Register },
  {
    path: '/dashboard',
    component: Dashboard,
    meta: { requiresAuth: true }
  },
  {
    path: '/rooms',
    component: JamRooms,
    meta: { requiresAuth: true }
  },
  {
    path: '/events',
    component: Events,
    meta: { requiresAuth: true }
  },
  {
    path: '/profile',
    component: Profile,
    meta: { requiresAuth: true }
  },
];

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
});

router.beforeEach((to, from, next) => {
  const auth = useAuthStore();
  if (to.meta.requiresAuth && !auth.isAuthenticated) {
    next('/login');
  } else {
    next();
  }
});

export default router;