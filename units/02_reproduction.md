---
theme: seriph
background: https://source.unsplash.com/collection/94734566/1920x1080
class: text-center
highlighter: shiki
lineNumbers: false
info: |
  ## V. 생식과 유전
  3. 수정과 발생
drawings:
  persist: false
transition: slide-left
title: V. 생식과 유전
---

# V. 생식과 유전
## 3. 수정과 발생

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
  <div class="bg-white p-10 rounded-2xl shadow-xl border-l-8 border-amber-500 max-w-2xl">
    <ul class="space-y-6 text-2xl list-none">
      
      <li class="flex items-center gap-4">
        <div class="i-carbon-checkmark-filled text-amber-500" />
        <span>수정란으로부터 개체가 발생하는 과정을 설명할 수 있다.</span>
      </li>
      
      <li class="flex items-center gap-4">
        <div class="i-carbon-checkmark-filled text-amber-500" />
        <span>정자와 난자의 특징을 비교하고 수정 과정에서의 역할을 이해한다.</span>
      </li>
      
      <li class="flex items-center gap-4">
        <div class="i-carbon-checkmark-filled text-amber-500" />
        <span>난할과 일반적인 체세포 분열의 차이점을 비교하여 설명할 수 있다.</span>
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
  달걀이 병아리가 되기까지<br>어떤 과정을 거칠까? 🐣
</p>


<div class="mt-8 max-w-2xl mx-auto">
  <img src="/images/Schematic-drawings-of-chronological-chick-embryo-development.png" class="rounded-lg shadow-lg max-h-80 mx-auto" />
  
  <p class="text-sm text-slate-500 mt-2">하나의 수정란 세포가 복잡한 병아리가 되는 과정</p>
  
</div>




---

---

# 생식세포 - 정자와 난자




<div class="grid grid-cols-2 gap-8">
  
  <div class="bg-white p-6 rounded-2xl shadow-lg border-t-4 border-amber-500">
    
    <h3 class="text-2xl font-bold mb-4 text-amber-700">
      정자 (Sperm)
    </h3>
    
    
    
    <ul class="list-disc list-inside space-y-2 text-lg">
      
      <li>머리(핵)와 꼬리로 구성</li>
      
      <li>꼬리를 이용해 스스로 움직임</li>
      
      <li>아버지의 유전 물질(n) 전달</li>
      
    </ul>
    
    
  </div>
  
  <div class="bg-white p-6 rounded-2xl shadow-lg border-t-4 border-amber-500">
    
    <h3 class="text-2xl font-bold mb-4 text-amber-700">
      난자 (Ovum)
    </h3>
    
    
    
    <ul class="list-disc list-inside space-y-2 text-lg">
      
      <li>정자보다 훨씬 큼 (많은 양분 저장)</li>
      
      <li>스스로 움직이지 못함</li>
      
      <li>어머니의 유전 물질(n) 전달</li>
      
    </ul>
    
    
  </div>
  
</div>







---

---

# 정자와 난자의 구조


<div class="flex justify-center">
  <img src="/images/gametes1_med.jpeg" class="rounded-xl shadow-lg max-w-2xl w-full" />
</div>
<p class="text-center mt-4 text-slate-500">각자의 역할(이동 vs 양분)에 최적화된 구조</p>










---

layout: two-cols

---

# 수정 (Fertilization)


<div class="bg-white p-6 rounded-xl border-l-4 border-amber-500">
  <h3 class="font-bold text-xl mb-2 text-amber-800">정의</h3>
  <p class="text-lg mb-4">정자와 난자가 결합하여 <b>수정란</b>이 되는 과정</p>
  <ul class="list-disc list-inside text-lg">
    <li>장소: <b>수란관</b> 상단부</li>
    <li>결과: 체세포와 같은 염색체 수 회복 (n + n = 2n)</li>
  </ul>
</div>




<div class="grid grid-cols-1 gap-8">
  
  <div class="bg-white p-6 rounded-2xl shadow-lg border-t-4 border-amber-500">
    
    
    <div class="mb-4 text-lg">
        하나의 정자가 난자와 결합하는 순간
    </div>
    
    
    
    <img src="/images/Staged-penetration-and-fusion-of-the-sperm-nucleus-and-the-centriole-in-the-egg-in-the.png" class="rounded-lg w-full object-cover mt-4" />
    
  </div>
  
</div>







---

layout: two-cols

---

# 발생 ① - 난할 (Cleavage)


<div class="bg-indigo-50 p-6 rounded-xl">
  <h3 class="font-bold text-xl mb-2 text-indigo-800">특징</h3>
  <ul class="space-y-2 text-lg">
    <li><b>빠른 분열:</b> 세포 생장기(간기)가 거의 없음</li>
    <li><b>세포 크기:</b> 분열할수록 작아짐 (할구)</li>
    <li><b>전체 크기:</b> 수정란과 거의 동일하게 유지</li>
  </ul>
</div>




<div class="grid grid-cols-1 gap-8">
  
  <div class="bg-white p-6 rounded-2xl shadow-lg border-t-4 border-amber-500">
    
    
    <div class="mb-4 text-lg">
        2세포기 → 4세포기 → 8세포기 ...
    </div>
    
    
    
    <img src="/images/Cell_Cleavage.png" class="rounded-lg w-full object-cover mt-4" />
    
  </div>
  
</div>







---

---

# 난할 vs 체세포 분열








<div class="bg-white p-6 rounded-xl shadow-lg overflow-x-auto">
  <table class="w-full text-sm">
    <thead class="bg-slate-100">
      <tr>
        <th class="p-3 text-left">구분</th>
        
        <th class="p-3 text-center text-amber-600">난할 (초기 발생)</th>
        
        <th class="p-3 text-center text-emerald-600">일반 체세포 분열</th>
        
      </tr>
    </thead>
    <tbody class="text-center">
      
      <tr class="border-b last:border-b-0">
        <td class="p-3 font-bold text-left bg-slate-50">분열 속도</td>
        
        <td class="p-3">매우 빠름</td>
        
        <td class="p-3">보통</td>
        
      </tr>
      
      <tr class="border-b last:border-b-0">
        <td class="p-3 font-bold text-left bg-slate-50">세포 생장(간기)</td>
        
        <td class="p-3">거의 없음 (생략)</td>
        
        <td class="p-3">있음 (세포가 커짐)</td>
        
      </tr>
      
      <tr class="border-b last:border-b-0">
        <td class="p-3 font-bold text-left bg-slate-50">딸세포 크기</td>
        
        <td class="p-3">점점 작아짐</td>
        
        <td class="p-3">모세포와 비슷함</td>
        
      </tr>
      
      <tr class="border-b last:border-b-0">
        <td class="p-3 font-bold text-left bg-slate-50">전체 크기</td>
        
        <td class="p-3">일정함</td>
        
        <td class="p-3">커짐 (생장)</td>
        
      </tr>
      
    </tbody>
  </table>
</div>



---

---

# 발생 ② - 착상과 태반




<div class="grid grid-cols-2 gap-8">
  
  <div class="bg-white p-6 rounded-2xl shadow-lg border-t-4 border-pink-500">
    
    <h3 class="text-2xl font-bold mb-4 text-pink-700">
      착상 (Implantation)
    </h3>
    
    
    <div class="mb-4 text-lg">
        수정 후 5~7일 뒤, 배아가 <b>자궁 내막</b>에 파고드는 현상. 이때부터 <b>임신</b>으로 간주함.
    </div>
    
    
    
    <img src="/images/uterus_implantation.jpg" class="rounded-lg w-full object-cover mt-4" />
    
  </div>
  
  <div class="bg-white p-6 rounded-2xl shadow-lg border-t-4 border-red-500">
    
    <h3 class="text-2xl font-bold mb-4 text-red-700">
      태반 (Placenta)
    </h3>
    
    
    <div class="mb-4 text-lg">
        모체와 태아 사이의 물질 교환 장소. (산소/영양소 공급, 노폐물 배출)
    </div>
    
    
    
  </div>
  
</div>







---

---

# 태아의 성장 과정


<div class="grid grid-cols-3 gap-4">
  <div class="bg-white p-4 rounded-xl shadow-md">
    <img src="/images/fetus_11_weeks.jpg" class="rounded-lg h-40 w-full object-cover mb-2"/>
    <h4 class="font-bold text-center">초기 (11주)</h4>
    <p class="text-sm text-center">주요 기관 형성, 사람 모습 갖춤</p>
  </div>
  <div class="bg-white p-4 rounded-xl shadow-md">
    <img src="/images/fetus_21_weeks.jpg" class="rounded-lg h-40 w-full object-cover mb-2"/>
    <h4 class="font-bold text-center">중기 (21주)</h4>
    <p class="text-sm text-center">활발한 태동, 급격한 성장</p>
  </div>
  <div class="bg-white p-4 rounded-xl shadow-md">
    <img src="/images/fetus_37_weeks.jpg" class="rounded-lg h-40 w-full object-cover mb-2"/>
    <h4 class="font-bold text-center">후기 (37주)</h4>
    <p class="text-sm text-center">출산 준비 완료 (약 266일 후 출산)</p>
  </div>
</div>












---
layout: center
---

# 💡 개념 확인 퀴즈

<div class="bg-white p-8 rounded-2xl shadow-lg border-2 border-amber-500 max-w-2xl mx-auto">

::: quiz {id: "fertilization-01", type: "multiple-choice", difficulty: "mid"}
수정란의 초기 세포 분열인 '난할'의 특징으로 옳은 것은?


- [ ] 세포 분열 후 세포의 크기가 커진다.

- [ ] 세포 분열 사이에 생장기가 길다.

- [x] 분열이 진행되어도 전체 배아의 크기는 일정하다.

- [ ] 염색체 수가 절반으로 줄어든다.

:::

</div>


---
layout: center
class: text-center
---

# 핵심 정리 📝

<div class="bg-amber-600 text-white p-10 rounded-3xl shadow-2xl inline-block text-left max-w-4xl">
  <ul class="space-y-4 text-xl list-none">
    
    <li class="flex items-start gap-4">
      <div class="i-carbon-checkmark mt-1 flex-shrink-0" />
      <span><b>수정</b>은 수란관에서 정자와 난자가 결합하는 것이다.</span>
    </li>
    
    <li class="flex items-start gap-4">
      <div class="i-carbon-checkmark mt-1 flex-shrink-0" />
      <span><b>난할</b>은 세포 생장 없이 빠르게 분열하여 전체 크기가 일정하다.</span>
    </li>
    
    <li class="flex items-start gap-4">
      <div class="i-carbon-checkmark mt-1 flex-shrink-0" />
      <span>배아가 자궁 내막에 <b>착상</b>하면 임신이 시작된다.</span>
    </li>
    
    <li class="flex items-start gap-4">
      <div class="i-carbon-checkmark mt-1 flex-shrink-0" />
      <span><b>태반</b>을 통해 모체로부터 영양소와 산소를 공급받는다.</span>
    </li>
    
  </ul>
</div>