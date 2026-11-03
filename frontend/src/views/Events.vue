<template>
  <div class="max-w-6xl mx-auto">
    <div class="flex justify-between items-center mb-8">
      <div>
        <h1 class="text-3xl font-bold text-slate-800">Virtual Concerts</h1>
        <p class="text-slate-500">Micro-events and pop-up shows from your favorite artists.</p>
      </div>
      <button @click="showCreateModal = true" class="bg-primary text-white px-6 py-3 rounded-xl font-bold flex items-center gap-2 hover:bg-indigo-700 transition">
        <CalendarPlus class="w-5 h-5" />
        Schedule Event
      </button>
    </div>

    <div v-if="loading" class="text-center py-20">
      <div class="animate-spin rounded-full h-12 w-12 border-b-2 border-primary mx-auto"></div>
    </div>

    <div v-else-if="events.length === 0" class="bg-white rounded-3xl p-20 text-center border border-slate-100">
      <Calendar class="w-16 h-16 text-slate-200 mx-auto mb-6" />
      <h3 class="text-xl font-bold text-slate-800 mb-2">No upcoming events</h3>
      <p class="text-slate-500">Check back later for new concert announcements.</p>
    </div>

    <div v-else class="grid md:grid-cols-2 gap-8">
      <div v-for="event in events" :key="event.id" class="bg-white rounded-3xl border border-slate-100 overflow-hidden flex flex-col md:flex-row">
        <div class="w-full md:w-48 bg-indigo-600 flex flex-col items-center justify-center text-white p-6">
          <span class="text-sm font-bold uppercase opacity-80">{{ getMonth(event.start_time) }}</span>
          <span class="text-5xl font-black">{{ getDay(event.start_time) }}</span>
          <span class="text-sm font-bold mt-2">{{ getTime(event.start_time) }}</span>
        </div>
        <div class="p-8 flex-1 flex flex-col justify-between">
          <div>
            <div class="flex justify-between items-start mb-2">
              <h3 class="text-2xl font-bold text-slate-800">{{ event.title }}</h3>
              <span class="bg-emerald-50 text-emerald-600 px-3 py-1 rounded-full text-sm font-bold">${{ event.ticket_price }}</span>
            </div>
            <p class="text-slate-600 mb-4">{{ event.description }}</p>
            <p class="text-sm text-slate-500 mb-6">Hosted by <span class="font-bold">{{ event.artist.username }}</span></p>
          </div>
          <button class="w-full bg-slate-900 text-white py-3 rounded-xl font-bold hover:bg-slate-800 transition">Get Ticket</button>
        </div>
      </div>
    </div>

    <!-- Create Modal -->
    <div v-if="showCreateModal" class="fixed inset-0 bg-slate-900/50 backdrop-blur-sm z-[100] flex items-center justify-center p-6">
      <div class="bg-white w-full max-w-lg rounded-3xl p-8">
        <h2 class="text-2xl font-bold mb-6">Schedule an Event</h2>
        <form @submit.prevent="handleCreateEvent" class="space-y-4">
          <div>
            <label class="block text-sm font-semibold mb-1">Event Title</label>
            <input v-model="newEvent.title" required class="w-full px-4 py-2 rounded-lg border border-slate-200 outline-none focus:ring-2 focus:ring-primary">
          </div>
          <div class="grid grid-cols-2 gap-4">
            <div>
              <label class="block text-sm font-semibold mb-1">Start Time</label>
              <input v-model="newEvent.start_time" type="datetime-local" required class="w-full px-4 py-2 rounded-lg border border-slate-200 outline-none focus:ring-2 focus:ring-primary">
            </div>
            <div>
              <label class="block text-sm font-semibold mb-1">Ticket Price ($)</label>
              <input v-model="newEvent.ticket_price" type="number" step="0.01" required class="w-full px-4 py-2 rounded-lg border border-slate-200 outline-none focus:ring-2 focus:ring-primary">
            </div>
          </div>
          <div>
            <label class="block text-sm font-semibold mb-1">Description</label>
            <textarea v-model="newEvent.description" rows="3" class="w-full px-4 py-2 rounded-lg border border-slate-200 outline-none focus:ring-2 focus:ring-primary"></textarea>
          </div>
          <div class="flex gap-3 pt-4">
            <button type="button" @click="showCreateModal = false" class="flex-1 py-3 rounded-xl border border-slate-200 font-bold hover:bg-slate-50">Cancel</button>
            <button type="submit" class="flex-1 py-3 rounded-xl bg-primary text-white font-bold hover:bg-indigo-700">Schedule Now</button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, reactive } from 'vue';
import { Calendar, CalendarPlus } from 'lucide-vue-next';
import client from '../api/client';

const events = ref([]);
const loading = ref(true);
const showCreateModal = ref(false);
const newEvent = reactive({ title: '', start_time: '', ticket_price: 0, description: '' });

const fetchEvents = async () => {
  loading.value = true;
  try {
    const res = await client.get('/events');
    events.value = res.data;
  } finally {
    loading.value = false;
  }
};

const handleCreateEvent = async () => {
  try {
    await client.post('/events', newEvent);
    showCreateModal.value = false;
    fetchEvents();
  } catch (e) {
    alert('Failed to create event');
  }
};

const getMonth = (d) => new Date(d).toLocaleString('default', { month: 'short' });
const getDay = (d) => new Date(d).getDate();
const getTime = (d) => new Date(d).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });

onMounted(fetchEvents);
</script>