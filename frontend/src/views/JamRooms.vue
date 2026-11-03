<template>
  <div class="max-w-6xl mx-auto">
    <div class="flex justify-between items-center mb-8">
      <div>
        <h1 class="text-3xl font-bold text-slate-800">Jam Rooms</h1>
        <p class="text-slate-500">Jump into a live session or host your own.</p>
      </div>
      <button @click="showCreateModal = true" class="bg-primary text-white px-6 py-3 rounded-xl font-bold flex items-center gap-2 hover:bg-indigo-700 transition">
        <Plus class="w-5 h-5" />
        Go Live
      </button>
    </div>

    <div v-if="loading" class="text-center py-20">
      <div class="animate-spin rounded-full h-12 w-12 border-b-2 border-primary mx-auto"></div>
    </div>

    <div v-else-if="rooms.length === 0" class="bg-white rounded-3xl p-20 text-center border border-slate-100">
      <Radio class="w-16 h-16 text-slate-200 mx-auto mb-6" />
      <h3 class="text-xl font-bold text-slate-800 mb-2">No active rooms</h3>
      <p class="text-slate-500">Be the first to start a jam session!</p>
    </div>

    <div v-else class="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
      <div v-for="room in rooms" :key="room.id" class="bg-white rounded-2xl shadow-sm border border-slate-100 overflow-hidden hover:shadow-md transition group">
        <div class="p-6">
          <div class="flex justify-between items-start mb-4">
            <span class="bg-indigo-50 text-primary px-3 py-1 rounded-full text-xs font-bold uppercase tracking-wider">{{ room.genre }}</span>
            <div class="flex items-center gap-1 text-rose-500 text-xs font-bold">
              <span class="w-2 h-2 bg-rose-500 rounded-full"></span>
              {{ room.listener_count }} LIVE
            </div>
          </div>
          <h3 class="text-xl font-bold text-slate-800 mb-2 group-hover:text-primary transition">{{ room.title }}</h3>
          <p class="text-slate-500 text-sm mb-6 line-clamp-2">{{ room.description }}</p>
          <div class="flex items-center justify-between">
            <div class="flex items-center gap-2">
              <div class="w-8 h-8 bg-slate-100 rounded-full flex items-center justify-center text-slate-500">
                <User class="w-4 h-4" />
              </div>
              <span class="text-sm font-semibold text-slate-700">{{ room.host.username }}</span>
            </div>
            <button class="text-primary font-bold text-sm flex items-center gap-1">
              Join Jam <ChevronRight class="w-4 h-4" />
            </button>
          </div>
        </div>
      </div>
    </div>

    <!-- Create Modal -->
    <div v-if="showCreateModal" class="fixed inset-0 bg-slate-900/50 backdrop-blur-sm z-[100] flex items-center justify-center p-6">
      <div class="bg-white w-full max-w-lg rounded-3xl p-8">
        <h2 class="text-2xl font-bold mb-6">Start a New Jam</h2>
        <form @submit.prevent="handleCreateRoom" class="space-y-4">
          <div>
            <label class="block text-sm font-semibold mb-1">Room Title</label>
            <input v-model="newRoom.title" required class="w-full px-4 py-2 rounded-lg border border-slate-200 outline-none focus:ring-2 focus:ring-primary">
          </div>
          <div>
            <label class="block text-sm font-semibold mb-1">Genre</label>
            <select v-model="newRoom.genre" class="w-full px-4 py-2 rounded-lg border border-slate-200 outline-none focus:ring-2 focus:ring-primary">
              <option>Rock</option>
              <option>Jazz</option>
              <option>Electronic</option>
              <option>Acoustic</option>
              <option>Hip Hop</option>
            </select>
          </div>
          <div>
            <label class="block text-sm font-semibold mb-1">Description</label>
            <textarea v-model="newRoom.description" rows="3" class="w-full px-4 py-2 rounded-lg border border-slate-200 outline-none focus:ring-2 focus:ring-primary"></textarea>
          </div>
          <div class="flex gap-3 pt-4">
            <button type="button" @click="showCreateModal = false" class="flex-1 py-3 rounded-xl border border-slate-200 font-bold hover:bg-slate-50">Cancel</button>
            <button type="submit" class="flex-1 py-3 rounded-xl bg-primary text-white font-bold hover:bg-indigo-700">Go Live Now</button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, reactive } from 'vue';
import { Plus, Radio, User, ChevronRight } from 'lucide-vue-next';
import client from '../api/client';

const rooms = ref([]);
const loading = ref(true);
const showCreateModal = ref(false);
const newRoom = reactive({ title: '', genre: 'Rock', description: '' });

const fetchRooms = async () => {
  loading.value = true;
  try {
    const res = await client.get('/rooms');
    rooms.value = res.data;
  } finally {
    loading.value = false;
  }
};

const handleCreateRoom = async () => {
  try {
    await client.post('/rooms', newRoom);
    showCreateModal.value = false;
    fetchRooms();
    newRoom.title = '';
    newRoom.description = '';
  } catch (e) {
    alert('Failed to create room');
  }
};

onMounted(fetchRooms);
</script>