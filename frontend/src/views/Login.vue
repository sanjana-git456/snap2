<template>
  <div class="min-h-screen flex items-center justify-center bg-gradient-to-br from-indigo-500 to-purple-600 p-6">
    <div class="bg-white w-full max-w-md rounded-3xl shadow-2xl p-10">
      <div class="text-center mb-10">
        <div class="inline-block p-4 bg-indigo-50 rounded-2xl mb-4">
          <Music class="w-8 h-8 text-primary" />
        </div>
        <h2 class="text-3xl font-bold text-slate-800">Welcome Back</h2>
        <p class="text-slate-500 mt-2">Log in to your SnapStage account</p>
      </div>

      <form @submit.prevent="handleLogin" class="space-y-6">
        <div v-if="error" class="p-4 bg-rose-50 text-rose-600 rounded-xl text-sm border border-rose-100">
          {{ error }}
        </div>
        <div>
          <label class="block text-sm font-semibold text-slate-700 mb-2">Username</label>
          <input v-model="form.username" type="text" required class="w-full px-4 py-3 rounded-xl border border-slate-200 focus:ring-2 focus:ring-primary focus:border-transparent outline-none transition">
        </div>
        <div>
          <label class="block text-sm font-semibold text-slate-700 mb-2">Password</label>
          <input v-model="form.password" type="password" required class="w-full px-4 py-3 rounded-xl border border-slate-200 focus:ring-2 focus:ring-primary focus:border-transparent outline-none transition">
        </div>
        <button :disabled="loading" type="submit" class="w-full bg-primary text-white py-4 rounded-xl font-bold hover:bg-indigo-700 transition disabled:opacity-50">
          {{ loading ? 'Logging in...' : 'Log In' }}
        </button>
      </form>

      <p class="text-center mt-8 text-slate-600">
        Don't have an account? 
        <router-link to="/register" class="text-primary font-bold hover:underline">Sign Up</router-link>
      </p>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive } from 'vue';
import { Music } from 'lucide-vue-next';
import { useAuthStore } from '../stores/auth';
import { useRouter } from 'vue-router';

const auth = useAuthStore();
const router = useRouter();

const form = reactive({ username: '', password: '' });
const loading = ref(false);
const error = ref('');

const handleLogin = async () => {
  loading.value = true;
  error.value = '';
  try {
    await auth.login(form.username, form.password);
    router.push('/dashboard');
  } catch (err) {
    error.value = err.response?.data?.detail || 'Login failed. Please check your credentials.';
  } finally {
    loading.value = false;
  }
};
</script>