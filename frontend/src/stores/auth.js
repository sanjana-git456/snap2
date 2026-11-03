import { defineStore } from 'pinia';
import client from '../api/client';

export const useAuthStore = defineStore('auth', {
  state: () => ({
    user: null,
    token: localStorage.getItem('token') || null,
  }),
  getters: {
    isAuthenticated: (state) => !!state.token,
  },
  actions: {
    async login(username, password) {
      const response = await client.post('/auth/login', { username, password });
      this.token = response.data.access_token;
      this.user = response.data.user;
      localStorage.setItem('token', this.token);
      return response.data;
    },
    async register(username, email, password) {
      const response = await client.post('/auth/register', { username, email, password });
      this.token = response.data.access_token;
      this.user = response.data.user;
      localStorage.setItem('token', this.token);
      return response.data;
    },
    async fetchMe() {
      if (!this.token) return;
      try {
        const response = await client.get('/auth/me');
        this.user = response.data;
      } catch (e) {
        this.logout();
      }
    },
    logout() {
      this.token = null;
      this.user = null;
      localStorage.removeItem('token');
    },
  },
});