import { defineConfig } from 'unocss'

export default defineConfig({
  // Tailwind 호환성을 위한 기본 프리셋은 Slidev 내부에 이미 포함되어 있습니다.
  // 여기서는 커스텀 단축 클래스(Shortcuts)나 테마 확장을 정의합니다.
  shortcuts: {
    'bg-main': 'bg-slate-50 text-slate-800',
    'btn-primary': 'px-4 py-2 rounded-lg bg-emerald-500 text-white hover:bg-emerald-600 transition-colors',
    'card': 'bg-white p-6 rounded-xl shadow-lg border border-slate-200',
  },
  theme: {
    fontFamily: {
      sans: ['Noto Sans KR', 'sans-serif'],
    },
  },
})
