<template>
  <div class="max-w-6xl mx-auto">
    <header class="mb-10">
      <h1 class="text-3xl font-bold text-slate-800">Welcome back, {{ auth.user?.username }}!</h1>
      <p class="text-slate-500">Here's what's happening on SnapStage today.</p>
    </header>

    <div class="grid md:grid-cols-3 gap-6 mb-10">
      <div class="bg-white p-6 rounded-2xl shadow-sm border border-slate-100">
        <div class="flex items-center gap-4 mb-4">
          <div class="p-3 bg-indigo-50 rounded-xl text-primary">
            <Radio class="w-6 h-6" />
          </div>
          <h3 class="font-semibold text-slate-700">Active Jams</h3>
        </div>
        <p class="text-3xl font-bold text-slate-900">{{ stats.rooms }}</p>
      </div>
      <div class="bg-white p-6 rounded-2xl shadow-sm border border-slate-100">
        <div class="flex items-center gap-4 mb-4">
          <div class="p-3 bg-pink-50 rounded-xl text-secondary">
            <Calendar class="w-6 h-6" />
          </div>
          <h3 class="font-semibold text-slate-700">Upcoming Events</h3>
        </div>
        <p class="text-3xl font-bold text-slate-900">{{ stats.events }}</p>
      </div>
      <div class="bg-white p-6 rounded-2xl shadow-sm border border-slate-100">
        <div class="flex items-center gap-4 mb-4">
          <div class="p-3 bg-emerald-50 rounded-xl text-emerald-600">
            <Award class="w-6 h-6" />
          </div>
          <h3 class="font-semibold text-slate-700">Reputation</h3>
        </div>
        <p class="text-3xl font-bold text-slate-900">{{ auth.user?.reputation_score || 0 }}</p>
      </div>
    </div>

    <div class="grid md:grid-cols-2 gap-8">
      <section>
        <div class="flex justify-between items-center mb-6">
          <h2 class="text-xl font-bold text-slate-800">Live Now</h2>
          <router-link to="/rooms" class="text-primary text-sm font-semibold hover:underline">View All</router-link>
        </div>
        <div class="space-y-4">
          <div v-for="room in recentRooms" :key="room.id" class="bg-white p-4 rounded-xl border border-slate-100 flex items-center justify-between">
            <div>
              <h4 class="font-bold text-slate-800">{{ room.title }}</h4>
              <p class="text-sm text-slate-500">{{ room.genre }} • {{ room.host.username }}</p>
            </div>
            <div class="flex items-center gap-2 text-rose-500 text-sm font-bold">
              <span class="w-2 h-2 bg-rose-500 rounded-full animate-pulse"></span>
              {{ room.listener_count }} listeners
            </div>
          </div>
          <p v-if="recentRooms.length === 0" class="text-slate-500 text-center py-8">No rooms live right now.</p>
        </div>
      </section>

      <section>
        <div class="flex justify-between items-center mb-6">
          <h2 class="text-xl font-bold text-slate-800">Upcoming Concerts</h2>
          <router-link to="/events" class="text-primary text-sm font-semibold hover:underline">View All</router-link>
        </div>
        <div class="space-y-4">
          <div v-for="event in recentEvents" :key="event.id" class="bg-white p-4 rounded-xl border border-slate-100">
            <div class="flex justify-between items-start">
              <div>
                <h4 class="font-bold text-slate-800">{{ event.title }}</h4>
                <p class="text-sm text-slate-500">{{ formatDate(event.start_time) }}</p>
              </div>
              <span class="bg-indigo-50 text-primary px-3 py-1 rounded-full text-xs font-bold">${{ event.ticket_price }}</span>
            </div>
          </div>
          <p v-if="recentEvents.length === 0" class="text-slate-500 text-center py-8">No upcoming events.</p>
        </div>
      </section>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { Radio, Calendar, Award } from 'lucide-vue-next';
import { useAuthStore } from '../stores/auth';
import client from '../api/client';

const auth = useAuthStore();
const stats = ref({ rooms: 0, events: 0 });
const recentRooms = ref([]);
const recentEvents = ref([]);

const fetchData = async () => {
  try {
    const [roomsRes, eventsRes] = await Promise.all([
      client.get('/rooms?limit=3'),
      client.get('/events?limit=3')
    ]);
    recentRooms.value = roomsRes.data;
    recentEvents.value = eventsRes.data;
    stats.value.rooms = roomsRes.data.length;
    stats.value.events = eventsRes.data.length;
  } catch (e) {
    console.error(e);
  }
};

const formatDate = (dateStr) => {
  return new Date(dateStr).toLocaleDateString('en-US', { 
    month: 'short', 
    day: 'numeric', 
    hour: '2-digit', 
    minute: '2-digit' 
  });
};

onMounted(fetchData);
</script>