---
theme: seriph
background: https://source.unsplash.com/collection/94734566/1920x1080
class: text-center
highlighter: shiki
lineNumbers: false
info: |
  ## Project S.C.O.P.E. - Mitosis
  Science Classroom Observation & Performance Engine
drawings:
  persist: false
transition: slide-left
title: 체세포 분열 탐험
---

# V. 생식과 유전
## 1. 세포 분열과 염색체

<div class="pt-12">
  <span @click="$slidev.nav.next" class="px-6 py-3 rounded-full cursor-pointer transition-colors hover:bg-emerald-500 hover:text-white border border-emerald-500 text-emerald-600 font-bold">
    탐험 시작하기 <div class="inline-block i-carbon-arrow-right" />
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

# 학습 목표

<div class="flex flex-col h-full justify-center items-center">
  <div class="bg-white p-10 rounded-2xl shadow-xl border-l-8 border-emerald-500 max-w-2xl">
    <ul class="space-y-6 text-2xl list-none">
      <li class="flex items-center gap-4">
        <div class="i-carbon-checkmark-filled text-emerald-500" />
        <span>염색체와 유전자의 관계를 설명할 수 있다.</span>
      </li>
      <li class="flex items-center gap-4">
        <div class="i-carbon-checkmark-filled text-emerald-500" />
        <span>체세포 분열의 특징을 염색체의 행동으로 설명할 수 있다.</span>
      </li>
    </ul>
  </div>
</div>

---
layout: center
class: text-center
---

# 생각 열기

<p class="text-4xl font-bold text-slate-700 leading-tight">
  분열 전인 세포와 분열 중인 세포의<br>
  <span class="text-emerald-600 underline decoration-wavy">차이점</span>은 무엇일까?
</p>

---
layout: two-cols
---

# 염색체 (Chromosome)

<div class="pr-4">
  <div class="bg-emerald-50 p-6 rounded-xl border-l-4 border-emerald-500 mb-6">
    <h3 class="font-bold text-xl mb-2 text-emerald-800">정의</h3>
    <p class="text-lg">분열 중인 세포에서 유전 물질이 꼬이고 뭉쳐서 만들어진 막대 모양의 구조물입니다.</p>
  </div>

  <div class="bg-blue-50 p-6 rounded-xl border-l-4 border-blue-500">
    <h3 class="font-bold text-xl mb-2 text-blue-800">구조</h3>
    <p class="text-lg">두 개의 <b>염색 분체</b>가 중앙의 <b>동원체</b>에 의해 연결된 구조입니다.</p>
  </div>
</div>

::right::

<div class="flex flex-col items-center justify-center h-full pl-4">
  <div class="bg-white p-4 rounded-2xl shadow-lg">
    <img src="/images/DNA_animation.gif" class="rounded-xl w-64 h-64 object-cover" />
    <p class="text-center mt-2 text-slate-500 text-sm">DNA 이중 나선 구조</p>
  </div>
</div>

---

# DNA와 유전자

<div class="grid grid-cols-2 gap-8 mt-4">
  <div class="bg-white p-6 rounded-xl shadow-md border-t-4 border-emerald-400">
    <h3 class="font-bold text-xl text-emerald-700 mb-3 flex items-center gap-2">
      <div class="i-carbon-dna" /> DNA (디옥시리보핵산)
    </h3>
    <p class="leading-relaxed">
      생명의 모든 유전 정보를 담고 있는 설계도입니다. 두 가닥이 서로 꼬여있는 <b>이중 나선 구조</b>를 하고 있습니다.
    </p>
  </div>

  <div class="bg-white p-6 rounded-xl shadow-md border-t-4 border-amber-400">
    <h3 class="font-bold text-xl text-amber-700 mb-3 flex items-center gap-2">
      <div class="i-carbon-tree-view" /> 유전자 (Gene)
    </h3>
    <p class="leading-relaxed">
      DNA의 특정 구간으로, 눈 색깔 등 특정 형질을 결정하는 <b>하나의 정보 단위</b>입니다.
    </p>
  </div>
</div>

<div class="mt-12 text-center bg-slate-100 p-6 rounded-2xl">
  <p class="text-xl">
    사람의 체세포에는 <span class="text-emerald-600 font-bold">23쌍(총 46개)</span>의 염색체가 있습니다. (2n=46)
  </p>
</div>

---
layout: center
---

# 핵 분열 과정 영상 탐구

<VideoSegmentPlayer 
  videoId="LM-0RdQbSUs" 
  :phaseData="{
    prophase: { title: '전기', text: '핵막이 사라지고 염색체가 응축되며 방추사가 형성됩니다.', start: 4, end: 9 },
    metaphase: { title: '중기', text: '염색체들이 세포 중앙에 배열됩니다.', start: 11, end: 16 },
    anaphase: { title: '후기', text: '염색분체들이 분리되어 양 극으로 이동합니다.', start: 21, end: 24 },
    telophase: { title: '말기', text: '두 개의 새로운 핵이 형성되고 세포질 분열이 시작됩니다.', start: 26, end: 30 }
  }"
/>

---

# 세포질 분열 (Cytokinesis)

<div class="grid grid-cols-2 gap-8 h-full items-center">
  <div class="space-y-6">
    <div class="bg-white p-6 rounded-xl shadow-md border-l-4 border-emerald-500">
      <h3 class="font-bold text-xl mb-2 text-emerald-800">동물 세포</h3>
      <p>세포막이 바깥에서 안으로 오므라들며 나뉩니다. (세포질 만입)</p>
      <img src="/images/cell_division.png" class="mt-4 h-32 w-full object-contain mx-auto" />
    </div>
    
    <div class="bg-white p-6 rounded-xl shadow-md border-l-4 border-amber-500">
      <h3 class="font-bold text-xl mb-2 text-amber-800">식물 세포</h3>
      <p>중앙에서 <b>세포판</b>이 만들어져 바깥으로 자라며 나뉩니다.</p>
      <img src="/images/cell_division_2.png" class="mt-4 h-32 w-full object-contain mx-auto" />
    </div>
  </div>

  <div class="bg-slate-50 p-6 rounded-2xl border border-slate-200">
    <h3 class="font-bold text-xl mb-4 text-center">체세포 분열의 의의</h3>
    <ul class="space-y-4 text-lg">
      <li class="flex items-start gap-3">
        <div class="i-carbon-growth text-emerald-600 mt-1" />
        <span><b>생장:</b> 세포 수가 늘어나 몸이 자람</span>
      </li>
      <li class="flex items-start gap-3">
        <div class="i-carbon-pedestrian-family text-emerald-600 mt-1" />
        <span><b>재생:</b> 상처 난 부위의 세포를 보충</span>
      </li>
      <li class="flex items-start gap-3">
        <div class="i-carbon-copy text-emerald-600 mt-1" />
        <span><b>유지:</b> 염색체 수를 동일하게 유지 (2n &rarr; 2n)</span>
      </li>
    </ul>
  </div>
</div>

---

# 관찰 실험: 양파 뿌리 끝 세포

<div class="grid grid-cols-4 gap-4 mt-4">
  <LabCard 
    step="1" 
    title="고정" 
    image="/images/1-fixation.jpg" 
    description="살아있을 때의 모습을 유지시킵니다." 
  />
  <LabCard 
    step="2" 
    title="해리" 
    image="/images/2-maceration.png" 
    description="세포벽을 연하게 만들어 잘 분리되게 합니다." 
  />
  <LabCard 
    step="3" 
    title="염색" 
    image="/images/3-staining.jpg" 
    description="핵과 염색체를 붉게 염색합니다." 
  />
  <LabCard 
    step="4" 
    title="분찰" 
    image="/images/4-separation.jpg" 
    description="세포를 한 겹으로 펴서 관찰합니다." 
  />
</div>

---
layout: center
---

# 💡 실력 확인 퀴즈

<div class="bg-white p-8 rounded-2xl shadow-lg border-2 border-emerald-500 max-w-2xl mx-auto">

::: quiz {id: "mitosis-01", type: "multiple-choice", difficulty: "mid"}
체세포 분열 결과 만들어진 딸세포의 염색체 수 변화로 옳은 것은?

- [ ] 모세포의 절반으로 줄어든다.
- [x] 모세포와 동일하게 유지된다.
- [ ] 모세포의 두 배로 늘어난다.
- [ ] 시기에 따라 불규칙하게 변한다.
:::

</div>

<div class="mt-8 text-sm text-slate-400">
* 이 문항 데이터는 자동으로 추출되어 평가 시스템으로 전송됩니다.
</div>

---
layout: center
---

# V. 생식과 유전
## 2. 생식세포 형성 과정 (감수 분열)

<div class="pt-12">
  <span @click="$slidev.nav.next" class="px-6 py-3 rounded-full cursor-pointer transition-colors hover:bg-indigo-500 hover:text-white border border-indigo-500 text-indigo-600 font-bold">
    감수 분열 탐구하기 <div class="inline-block i-carbon-arrow-right" />
  </span>
</div>

---

# 생식과 생식세포

<div class="grid grid-cols-2 gap-8">
  <div class="bg-white p-6 rounded-2xl shadow-lg border-t-4 border-indigo-500">
    <h3 class="text-2xl font-bold mb-4 text-indigo-700 flex items-center gap-2">
      <div class="i-carbon-replicate" /> 생식 (Reproduction)
    </h3>
    <p class="mb-4">자신과 닮은 자손을 만드는 생명 현상</p>
    <img src="/images/Plant-Life-Cycle-for-Kids-Stages-Diagram.jpg" class="rounded-lg w-full h-48 object-cover" />
  </div>
  
  <div class="bg-white p-6 rounded-2xl shadow-lg border-t-4 border-blue-500">
    <h3 class="text-2xl font-bold mb-4 text-blue-700 flex items-center gap-2">
      <div class="i-carbon-user-identification" /> 생식세포 (Germ Cell)
    </h3>
    <p class="mb-4">자손에게 유전 물질을 전달하는 특수한 세포 (정자, 난자)</p>
    <img src="/images/gametes1_med.jpeg" class="rounded-lg w-full h-48 object-cover" />
  </div>
</div>

---

# 감수 분열 (Meiosis) 과정

<VideoSegmentPlayer 
  videoId="EPBSsGqTC8I" 
  :playbackRate="1.5"
  :columns="2"
  :phaseData="{
    prophase1: { title: '전기 I', text: '상동 염색체끼리 접합하여 2가 염색체를 형성합니다.', start: 1, end: 17 },
    metaphase1: { title: '중기 I', text: '2가 염색체가 세포 중앙에 배열됩니다.', start: 18, end: 38 },
    anaphase1: { title: '후기 I', text: '상동 염색체가 분리되어 양 극으로 이동합니다.', start: 47, end: 51 },
    telophase1: { title: '말기 I', text: '세포질이 나뉘어 2개의 딸세포(n)가 됩니다.', start: 60, end: 69 },
    prophase2: { title: '전기 II', text: '염색체가 다시 응축되고 방추사가 나타납니다.', start: 80, end: 83 },
    metaphase2: { title: '중기 II', text: '염색체가 세포 중앙에 배열됩니다.', start: 85, end: 89 },
    anaphase2: { title: '후기 II', text: '염색 분체가 분리되어 양 극으로 이동합니다.', start: 90, end: 97 },
    telophase2: { title: '말기 II', text: '총 4개의 딸세포(n)가 완성됩니다.', start: 99, end: 105 }
  }"
/>

---
layout: two-cols
---

# 감수 분열의 결과

<div class="pr-4">
  <div class="bg-indigo-50 p-6 rounded-xl border-l-4 border-indigo-500 mb-6">
    <h3 class="font-bold text-xl mb-2 text-indigo-800">세포 수</h3>
    <p class="text-lg">1개의 모세포 &rarr; <b>4개의 딸세포</b></p>
  </div>

  <div class="bg-red-50 p-6 rounded-xl border-l-4 border-red-500">
    <h3 class="font-bold text-xl mb-2 text-red-800">염색체 수</h3>
    <p class="text-lg">모세포의 <b>절반</b>으로 감소<br>(2n &rarr; n)</p>
  </div>
</div>

::right::

<div class="flex flex-col items-center justify-center h-full pl-4">
  <div class="bg-white p-4 rounded-2xl shadow-lg">
    <img src="/images/Meiosis_main_steps.svg" class="rounded-xl w-full" />
  </div>
</div>

---

# 체세포 분열 vs 감수 분열

<div class="bg-white p-4 rounded-xl shadow-lg">
  <table class="w-full text-sm">
    <thead class="bg-slate-100">
      <tr>
        <th class="p-2">구분</th>
        <th class="p-2 text-indigo-600">감수 분열</th>
        <th class="p-2 text-emerald-600">체세포 분열</th>
      </tr>
    </thead>
    <tbody class="text-center">
      <tr class="border-b">
        <td class="p-2 font-bold">분열 횟수</td>
        <td class="p-2">2회 연속</td>
        <td class="p-2">1회</td>
      </tr>
      <tr class="border-b">
        <td class="p-2 font-bold">딸세포 수</td>
        <td class="p-2">4개</td>
        <td class="p-2">2개</td>
      </tr>
      <tr class="border-b">
        <td class="p-2 font-bold">염색체 수</td>
        <td class="p-2 text-red-600">절반 감소 (2n &rarr; n)</td>
        <td class="p-2">변화 없음 (2n &rarr; 2n)</td>
      </tr>
      <tr class="border-b">
        <td class="p-2 font-bold">목적</td>
        <td class="p-2">생식세포 형성</td>
        <td class="p-2">생장, 재생</td>
      </tr>
    </tbody>
  </table>
</div>

<div class="mt-4">
  <img src="/images/[비상교육] 중등_과학 3_5-1_세포 분열 비교(출).jpg" class="h-40 mx-auto rounded-lg shadow-md" />
</div>

---

# DNA 상대량의 변화

<div class="flex flex-col items-center">
  <img src="/images/[비상교육] 중등_과학 3_5-1_생식세포 형성 과정에서 DNA 상대량 변화(출).jpg" class="h-80 rounded-xl shadow-xl" />
  <div class="mt-4 grid grid-cols-2 gap-8">
    <div class="text-sm p-3 bg-blue-50 rounded-lg">
      <b>감수 1분열:</b> 상동 염색체 분리 &rarr; 핵상과 DNA양 모두 감소
    </div>
    <div class="text-sm p-3 bg-indigo-50 rounded-lg">
      <b>감수 2분열:</b> 염색 분체 분리 &rarr; DNA양만 다시 감소
    </div>
  </div>
</div>

---

# 💡 실력 확인 퀴즈 (감수 분열)

<div class="bg-white p-8 rounded-2xl shadow-lg border-2 border-indigo-500 max-w-2xl mx-auto">

::: quiz {id: "meiosis-01", type: "multiple-choice", difficulty: "mid"}
감수 분열의 특징으로 옳은 것을 모두 고르면? (2개)

- [x] 분열 결과 4개의 딸세포가 만들어진다.
- [ ] 분열 결과 염색체 수가 두 배로 늘어난다.
- [ ] 1분열과 2분열 사이에 DNA 복제가 일어난다.
- [x] 상동 염색체가 접합하여 2가 염색체를 형성한다.
:::

</div>

---
layout: center
class: text-center
---

# 핵심 정리

<div class="bg-indigo-600 text-white p-10 rounded-3xl shadow-2xl inline-block text-left">
  <ul class="space-y-4 text-xl list-none">
    <li class="flex items-center gap-4">
      <div class="i-carbon-checkmark" />
      <span>감수 분열은 <b>2회 연속</b> 분열한다.</span>
    </li>
    <li class="flex items-center gap-4">
      <div class="i-carbon-checkmark" />
      <span>딸세포는 <b>4개</b>, 염색체 수는 <b>절반</b>이 된다.</span>
    </li>
    <li class="flex items-center gap-4">
      <div class="i-carbon-checkmark" />
      <span>이를 통해 세대가 거듭되어도 염색체 수가 <b>일정하게 유지</b>된다.</span>
    </li>
  </ul>
</div>
