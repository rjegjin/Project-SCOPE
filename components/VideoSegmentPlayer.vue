<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue'

const props = defineProps<{
  videoId: string
  phaseData: Record<string, { title: string, text: string, start: number, end: number }>
  playbackRate?: number
  columns?: number
}>()

const activePhase = ref('')
const player = ref<any>(null)
let intervalId: any = null

const selectPhase = (phase: string) => {
  activePhase.value = phase
  const segment = props.phaseData[phase]
  
  if (player.value && typeof player.value.seekTo === 'function') {
    if (intervalId) clearInterval(intervalId)
    
    if (props.playbackRate) {
      player.value.setPlaybackRate(props.playbackRate)
    }
    
    player.value.seekTo(segment.start, true)
    player.value.playVideo()
    
    intervalId = setInterval(() => {
      if (player.value.getCurrentTime() >= segment.end) {
        player.value.pauseVideo()
        clearInterval(intervalId)
      }
    }, 250)
  }
}

onMounted(() => {
  if (!(window as any).YT) {
    const tag = document.createElement('script')
    tag.src = "https://www.youtube.com/iframe_api"
    const firstScriptTag = document.getElementsByTagName('script')[0]
    firstScriptTag.parentNode?.insertBefore(tag, firstScriptTag)
  }

  const initPlayer = () => {
    player.value = new (window as any).YT.Player(`youtube-player-${props.videoId}`, {
      height: '100%',
      width: '100%',
      videoId: props.videoId,
      playerVars: { 'playsinline': 1, 'controls': 0, 'rel': 0 },
    })
  }

  if ((window as any).YT && (window as any).YT.Player) {
    initPlayer()
  } else {
    const oldCallback = (window as any).onYouTubeIframeAPIReady
    (window as any).onYouTubeIframeAPIReady = () => {
      if (oldCallback) oldCallback()
      initPlayer()
    }
  }
})

onUnmounted(() => {
  if (intervalId) clearInterval(intervalId)
})
</script>

<template>
  <div class="bg-white p-4 rounded-xl shadow-lg border border-slate-200">
    <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
      <div class="flex flex-col gap-2">
        <div :class="['grid gap-2', columns === 2 ? 'grid-cols-2' : 'grid-cols-1']">
          <button 
            v-for="(data, key) in phaseData" 
            :key="key"
            @click="selectPhase(key as string)"
            :class="[
              'p-2 rounded-lg text-sm transition-all duration-300 border-2',
              activePhase === key 
                ? 'bg-indigo-500 text-white border-indigo-600 font-bold scale-105 shadow-md' 
                : 'bg-slate-50 text-slate-700 border-slate-200 hover:border-indigo-300'
            ]"
          >
            {{ data.title }}
          </button>
        </div>
      </div>
      
      <div class="md:col-span-2 flex flex-col gap-4">
        <div class="aspect-video bg-slate-100 rounded-lg overflow-hidden border border-slate-200 shadow-inner">
          <div :id="`youtube-player-${videoId}`"></div>
        </div>
        
        <div class="p-3 bg-indigo-50 rounded-lg border-l-4 border-indigo-500 min-h-[70px]">
          <h4 class="text-lg font-bold text-indigo-800 mb-1">
            {{ activePhase ? phaseData[activePhase].title : '단계를 선택하세요' }}
          </h4>
          <p class="text-sm text-slate-700">
            {{ activePhase ? phaseData[activePhase].text : '버튼을 클릭하면 해당 단계의 영상이 재생됩니다.' }}
          </p>
        </div>
      </div>
    </div>
  </div>
</template>
