---
theme: seriph
background: https://source.unsplash.com/collection/94734566/1920x1080
class: text-center
highlighter: shiki
lineNumbers: false
info: |
  ## V. 생식과 유전
  멘델이 밝힌 유전 원리 - 완두콩 속에 숨겨진 비밀
drawings:
  persist: false
transition: slide-left
title: V. 생식과 유전
css: unocss
---

# V. 생식과 유전
## 멘델이 밝힌 유전 원리 - 완두콩 속에 숨겨진 비밀

<div class="pt-12">
  <span @click="$slidev.nav.next" class="px-6 py-3 rounded-full cursor-pointer transition-colors hover:bg-lime-500 hover:text-white border border-lime-500 text-lime-600 font-bold">
    학습 시작하기 <div class="inline-block i-carbon-arrow-right" />
  </span>
</div>

---
layout: default
---

# 학습 목표 🎯

<div class="bg-lime-50 p-8 rounded-2xl border-l-8 border-lime-500 mt-10">


- 유전의 뜻을 알고, 멘델의 실험 과정을 설명할 수 있다.

- 우성과 열성의 의미를 알고, 우열의 원리를 설명할 수 있다.

- 생식세포 형성 과정과 연관지어 분리의 법칙을 설명할 수 있다.


</div>


---
layout: center
class: text-center
---

# 생각 열기 🤔

<p class="text-3xl font-bold text-slate-700 leading-tight mb-8">
  우리는 왜 부모님을 닮았을까?
</p>





---
layout: default
---

# 핵심 용어 (1): 형질과 유전




<div class="grid grid-cols-3 gap-4">

<div class="bg-white p-4 rounded-xl shadow border border-slate-100 text-left">
  

<h3 class="font-bold text-lime-700 mb-1">형질 (Trait)</h3>
<p class="text-sm text-slate-600">생물이 가진 고유한 모양, 색깔, 성질 등.<br>(예: 완두 씨 모양, 사람의 눈동자 색)</p>


</div>

<div class="bg-white p-4 rounded-xl shadow border border-slate-100 text-left">
  

<h3 class="font-bold text-lime-700 mb-1">유전 (Heredity)</h3>
<p class="text-sm text-slate-600">부모의 형질이 자손에게 전달되는 현상.</p>


</div>

<div class="bg-white p-4 rounded-xl shadow border border-slate-100 text-left">
  

<h3 class="font-bold text-lime-700 mb-1">대립 형질</h3>
<p class="text-sm text-slate-600">하나의 형질에 대해 뚜렷이 대비되는 특징.<br>(예: '둥근 씨' vs '주름진 씨')</p>


</div>

</div>





---
layout: center
---

# 멘델 이전의 생각: 혼합설


<div class="text-lg leading-relaxed text-slate-700 mb-6">
과거 사람들은 **"부모의 형질이 자손에게 물감처럼 섞여 전달된다"**고 생각했습니다.<br>
하지만 멘델은 완두 실험을 통해 유전 인자가 입자처럼 행동한다는 사실을 밝혀냈습니다.

</div>







---
layout: default
---

# 멘델의 선택: 왜 완두였을까? 🌱




<div class="grid grid-cols-3 gap-4">

<div class="bg-white p-4 rounded-xl shadow border border-slate-100 text-left">
  

<h3 class="font-bold text-lime-700 mb-1">1. 기르기 쉽다</h3>
<p class="text-sm text-slate-600">세대가 짧고 자손의 수가 많아 통계 처리에 유리합니다.</p>


</div>

<div class="bg-white p-4 rounded-xl shadow border border-slate-100 text-left">
  

<h3 class="font-bold text-lime-700 mb-1">2. 대립 형질이 뚜렷하다</h3>
<p class="text-sm text-slate-600">씨의 모양, 색깔 등 구분이 명확하여 관찰하기 좋습니다.</p>


</div>

<div class="bg-white p-4 rounded-xl shadow border border-slate-100 text-left">
  

<h3 class="font-bold text-lime-700 mb-1">3. 자가 수분이 잘 된다</h3>
<p class="text-sm text-slate-600">순종을 얻기 쉽고, 인위적인 타가 수분(교배)도 가능합니다.</p>


</div>

</div>





---
layout: default
---

# 실험 준비: 순종 얻기


<div class="text-lg leading-relaxed text-slate-700 mb-6">
**자가 수분(Self-pollination)**
수술의 꽃가루가 같은 꽃의 암술머리에 붙는 현상.
계속 반복하면 유전적으로 균일한 **순종(Purebred)**을 얻을 수 있습니다.

</div>







---
layout: default
---

# 실험 1단계: 어버이(P) 교배




<div class="grid grid-cols-1 gap-4">

<div class="bg-white p-4 rounded-xl shadow border border-slate-100 text-left">
  

<h3 class="font-bold text-lime-700 mb-1">부모 세대 (P)</h3>


<ul class="text-sm text-slate-700 mt-2 list-disc list-inside">

<li>순종의 둥근 완두 (RR)</li>

<li>순종의 주름진 완두 (rr)</li>

<li>이 둘을 **타가 수분**하여 교배합니다.</li>

</ul>


</div>

</div>





---
layout: center
---

# 실험 결과: 잡종 1대 (F1)


<div class="text-lg leading-relaxed text-slate-700 mb-6">
**결과:** 모든 자손이 **둥근 완두**만 나타났습니다!<br>
주름진 형질은 어디로 갔을까요? 사라진 걸까요?

</div>







---
layout: default
---

# 결론 1: 우열의 원리


<div class="text-lg leading-relaxed text-slate-700 mb-6">
대립 형질을 가진 순종끼리 교배했을 때, 잡종 1대에서 나타나는 형질을 **우성**, 나타나지 않는 형질을 **열성**이라고 합니다.

</div>





| 구분 | 우성 (Dominant) | 열성 (Recessive) | 
| --- |  --- |  --- | 

| **특징** | 잡종 1대에서 표현됨 | 잡종 1대에서 숨겨짐 | 

| **멘델 실험 예** | 둥근 모양, 노란 색깔 | 주름진 모양, 초록 색깔 | 




---
layout: default
---

# 실험 2단계: 잡종 2대 (F2) 얻기


<div class="text-lg leading-relaxed text-slate-700 mb-6">
잡종 1대(F1, 둥근 완두)를 **자가 수분**시켜 자손(F2)을 얻었습니다.<br>
숨겨졌던 주름진 형질이 다시 나타날까요?

</div>







---
layout: default
---

# 실험 결과: 분리의 법칙


<div class="text-lg leading-relaxed text-slate-700 mb-6">
**결과:** 둥근 완두와 주름진 완두가 **3 : 1**의 비율로 나타났습니다.

</div>



<div class="grid grid-cols-2 gap-4">

<div class="bg-white p-4 rounded-xl shadow border border-slate-100 text-left">
  

<h3 class="font-bold text-lime-700 mb-1">유전 인자의 분리</h3>
<p class="text-sm text-slate-600">생식세포가 만들어질 때, 쌍으로 존재하던 유전 인자가 나뉘어 서로 다른 생식세포로 들어갑니다.</p>


</div>

<div class="bg-white p-4 rounded-xl shadow border border-slate-100 text-left">
  

<h3 class="font-bold text-lime-700 mb-1">비율의 비밀</h3>
<p class="text-sm text-slate-600">RR : Rr : rr = 1 : 2 : 1 (유전자형)<br>둥근(우성) : 주름진(열성) = 3 : 1 (표현형)</p>


</div>

</div>







---
layout: center
---

# 개념 확인 퀴즈 💡

<div class="bg-white p-8 rounded-2xl shadow-xl border-2 border-lime-200 text-left">

잡종 1대(Rr)를 자가 수분했을 때, 자손(F2)에서 나타나는 표현형의 분리 비는?


- [ ] 모두 둥근 완두만 나온다.

- [ ] 둥근 완두 : 주름진 완두 = 1 : 1

- [ ] 둥근 완두 : 주름진 완두 = 3 : 1

- [ ] 둥근 완두 : 주름진 완두 = 9 : 3 : 3 : 1


</div>


---
layout: center
---

# 핵심 정리 📝

<div class="bg-lime-600 text-white p-10 rounded-3xl shadow-2xl text-left">


- **우열의 원리: 잡종 1대에서는 우성 형질만 나타난다.**

- **분리의 법칙: 생식세포 형성 시 유전 인자가 나뉘어 들어간다.**

- **멘델은 유전 인자가 입자처럼 보존된다는 것을 증명했다.**


</div>