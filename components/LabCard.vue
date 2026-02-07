<script setup lang="ts">
defineProps<{
  step: string
  title: string
  image: string
  description: string
}>()
</script>

<template>
  <div class="bg-slate-50 rounded-xl p-4 border border-slate-200 hover:shadow-md transition-shadow group">
    <div class="flex items-center gap-2 mb-3">
      <span class="bg-emerald-600 text-white w-8 h-8 rounded-full flex items-center justify-center font-bold text-sm shadow-sm">
        {{ step }}
      </span>
      <h3 class="font-bold text-lg text-slate-800">{{ title }}</h3>
    </div>
    
    <div class="relative overflow-hidden rounded-lg mb-3 aspect-video">
      <img 
        :src="image" 
        :alt="title" 
        class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-110"
      />
      <div class="absolute inset-0 bg-gradient-to-t from-black/20 to-transparent"></div>
    </div>
    
    <p class="text-slate-600 text-sm leading-relaxed">
      {{ description }}
    </p>
  </div>
</template>
