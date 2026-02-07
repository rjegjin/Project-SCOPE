<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue'

const props = defineProps<{
  videoId: string
}>()

const activePhase = ref('')
const player = ref<any>(null)
let intervalId: any = null

const phaseData = {
  prophase: { title: '전기', text: '핵막이 사라지고 염색체가 응축되며 방추사가 형성됩니다.', start: 4, end: 9 },
  metaphase: { title: '중기', text: '염색체들이 세포 중앙에 배열됩니다.', start: 11, end: 16 },
  anaphase: { title: '후기', text: '염색분체들이 분리되어 양 극으로 이동합니다.', start: 21, end: 24 },
  telophase: { title: '말기', text: '두 개의 새로운 핵이 형성되고 세포질 분열이 시작됩니다.', start: 26, end: 30 }
}

const selectPhase = (phase: string) => {
  activePhase.value = phase
  const segment = (phaseData as any)[phase]
  
  if (player.value && typeof player.value.seekTo === 'function') {
    if (intervalId) clearInterval(intervalId)
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
  // Load YouTube API if not already loaded
  if (!(window as any).YT) {
    const tag = document.createElement('script')
    tag.src = "https://www.youtube.com/iframe_api"
    const firstScriptTag = document.getElementsByTagName('script')[0]
    firstScriptTag.parentNode?.insertBefore(tag, firstScriptTag)
  }

  const initPlayer = () => {
    player.value = new (window as any).YT.Player('youtube-player', {
      height: '100%',
      width: '100%',
      videoId: props.videoId,
      playerVars: { 'playsinline': 1, 'controls': 0, 'rel': 0 },
    })
  }

  if ((window as any).YT && (window as any).YT.Player) {
    initPlayer()
  } else {
    (window as any).onYouTubeIframeAPIReady = initPlayer
  }
})

onUnmounted(() => {
  if (intervalId) clearInterval(intervalId)
})
</script>

<template>
  <div class="bg-white p-4 rounded-xl shadow-lg border border-slate-200">
    <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
      <div class="flex flex-col space-y-2">
        <button 
          v-for="(data, key) in phaseData" 
          :key="key"
          @click="selectPhase(key)"
          :class="[
            'p-3 rounded-lg text-lg transition-all duration-300 border-2',
            activePhase === key 
              ? 'bg-emerald-500 text-white border-emerald-600 font-bold scale-105 shadow-md' 
              : 'bg-slate-50 text-slate-700 border-slate-200 hover:border-emerald-300'
          ]"
        >
          {{ data.title }}
        </button>
      </div>
      
      <div class="md:col-span-2 flex flex-col gap-4">
        <div class="aspect-video bg-slate-100 rounded-lg overflow-hidden border border-slate-200 shadow-inner">
          <div id="youtube-player"></div>
        </div>
        
        <div class="p-4 bg-emerald-50 rounded-lg border-l-4 border-emerald-500 min-h-[80px]">
          <h4 class="text-xl font-bold text-emerald-800 mb-1">
            {{ activePhase ? (phaseData as any)[activePhase].title : '단계를 선택하세요' }}
          </h4>
          <p class="text-slate-700">
            {{ activePhase ? (phaseData as any)[activePhase].text : '버튼을 클릭하면 해당 단계의 영상이 재생됩니다.' }}
          </p>
        </div>
      </div>
    </div>
  </div>
</template>
