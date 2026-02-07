---
theme: seriph
background: https://source.unsplash.com/collection/94734566/1920x1080
class: text-center
highlighter: shiki
lineNumbers: false
info: |
  ## V. 생식과 유전
  5. 멘델의 유전 원리
drawings:
  persist: false
transition: slide-left
title: V. 생식과 유전
---

# V. 생식과 유전
## 5. 멘델의 유전 원리

<div class="pt-12">
  <span @click="$slidev.nav.next" class="px-6 py-3 rounded-full cursor-pointer transition-colors hover:bg-emerald-500 hover:text-white border border-emerald-500 text-emerald-600 font-bold">
    학습 시작하기 <div class="inline-block i-carbon-arrow-right" />
  </span>
</div>

<div class="abs-b m-6 flex gap-2">
  <button @click="$slidev.nav.prev" class="text-xl icon-btn opacity-50 !border-none hover:opacity-100">
    <div class="i-carbon-caret-left" />
  </button>
  <button @click="$slidev.nav.next" class="text-xl icon-btn opacity-50 !border-none hover:opacity-100">
    <div class="i-carbon-caret-right" />
  </button>
</div>

---
layout: default
---

# 학습 목표 🎯

<div class="flex flex-col h-full justify-center items-center">
  <div class="bg-white p-10 rounded-2xl shadow-xl border-l-8 border-emerald-500 max-w-2xl">
    <ul class="space-y-6 text-2xl list-none">
      
      <li class="flex items-center gap-4">
        <div class="i-carbon-checkmark-filled text-emerald-500" />
        <span>멘델이 완두를 실험 재료로 선택한 이유를 설명할 수 있다.</span>
      </li>
      
      <li class="flex items-center gap-4">
        <div class="i-carbon-checkmark-filled text-emerald-500" />
        <span>우열의 원리와 분리의 법칙을 유전자 기호로 나타낼 수 있다.</span>
      </li>
      
      <li class="flex items-center gap-4">
        <div class="i-carbon-checkmark-filled text-emerald-500" />
        <span>독립의 법칙이 나타나는 원리를 확률로 이해한다.</span>
      </li>
      
    </ul>
  </div>
</div>


---
layout: center
class: text-center
---

# 생각 열기 🤔

<p class="text-4xl font-bold text-slate-700 leading-tight">
  부모님의 쌍꺼풀은 없는데,<br>왜 나에게는 쌍꺼풀이 있을까? 🧬
</p>


<div class="mt-8 max-w-2xl mx-auto">
  <img src="/images/mendel_intro.jpg" class="rounded-lg shadow-lg max-h-80 mx-auto" />
  
  <p class="text-sm text-slate-500 mt-2">유전 형질이 전달되는 신비로운 규칙을 찾아봅시다.</p>
  
</div>




---

---

# 멘델의 실험 재료 완두


<div class="grid grid-cols-2 gap-4">
  <div class="bg-emerald-50 p-4 rounded-lg border-l-4 border-emerald-500">
    <h4 class="font-bold mb-2">완두가 좋은 이유</h4>
    <ul class="list-disc list-inside">
      <li>재배하기 쉽고 한 세대가 짧다.</li>
      <li>자손의 수가 많아 통계 처리에 유리하다.</li>
      <li>대립 형질이 뚜렷하다.</li>
    </ul>
  </div>
  <img src="/images/mendel_pea_traits.jpg" class="rounded shadow h-40 object-cover" />
</div>










---

---

# 1. 우열의 원리 (Dominance)


잡종 1대(F1)에서 우성 형질만 나타나는 원리
<div class="p-4 bg-yellow-50 rounded mt-2 border border-yellow-200">
  YY (황색) x yy (녹색) → Yy (황색 100%)
</div>










---

---

# 2. 분리의 법칙 (Segregation)


생식세포 형성 시 대립 유전자가 분리되어 서로 다른 세포로 들어가는 법칙 (잡종 2대에서 3:1 분리)
<div class="mt-4 flex justify-center">
  <img src="/images/mendel_segregation.jpg" class="rounded shadow-lg h-48" />
</div>










---

---

# 3. 독립의 법칙 (Independent)


두 쌍 이상의 형질이 서로 영향을 주지 않고 독립적으로 유전되는 법칙 (9:3:3:1)
<div class="mt-4 flex justify-center">
  <img src="/images/mendel_independent.jpg" class="rounded shadow-lg h-48" />
</div>












---
layout: center
---

# 💡 개념 확인 퀴즈

<div class="bg-white p-8 rounded-2xl shadow-lg border-2 border-emerald-500 max-w-2xl mx-auto">

::: quiz {id: "mendel-01", type: "multiple-choice", difficulty: "high"}
유전자형이 RrYy인 완두를 자가 수분했을 때, 잡종 2대에서 '둥글고 녹색(R_yy)'인 완두가 나타날 확률은?


- [ ] 1/16

- [x] 3/16

- [ ] 9/16

- [ ] 4/16

:::

</div>


---
layout: center
class: text-center
---

# 핵심 정리 📝

<div class="bg-emerald-600 text-white p-10 rounded-3xl shadow-2xl inline-block text-left max-w-4xl">
  <ul class="space-y-4 text-xl list-none">
    
    <li class="flex items-start gap-4">
      <div class="i-carbon-checkmark mt-1 flex-shrink-0" />
      <span>우열의 원리: 잡종 1대에서는 우성만 표현됨</span>
    </li>
    
    <li class="flex items-start gap-4">
      <div class="i-carbon-checkmark mt-1 flex-shrink-0" />
      <span>분리의 법칙: 생식세포 형성 시 유전자가 분리됨 (3:1)</span>
    </li>
    
    <li class="flex items-start gap-4">
      <div class="i-carbon-checkmark mt-1 flex-shrink-0" />
      <span>독립의 법칙: 여러 형질은 독립적으로 유전됨 (9:3:3:1)</span>
    </li>
    
  </ul>
</div>