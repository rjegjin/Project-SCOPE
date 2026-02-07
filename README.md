# Project S.C.O.P.E. 🔭
**Science Classroom Observation & Performance Engine**

> **"교사는 기획하고, 시스템은 구현한다."**
> 단 하나의 YAML 데이터로 웹 슬라이드, 시험지, PPT를 동시에 생성하는 수업 자동화 엔진입니다.

![Project Status](https://img.shields.io/badge/Status-Active-emerald)
![Tech Stack](https://img.shields.io/badge/Stack-Sli.dev%20%7C%20Python%20%7C%20YAML-blue)

## 🌟 핵심 기능 (Key Features)

1.  **Single Source of Truth (SSoT):**
    - `data/*.yaml` 파일 하나만 작성하면 모든 수업 자료가 자동으로 만들어집니다.
2.  **Multi-Format Output:**
    - 🖥️ **Web Slide:** Sli.dev 기반의 고품질 인터랙티브 슬라이드.
    - 📄 **Exam Sheet:** 출력 가능한 깔끔한 HWP/PDF 스타일의 시험지 (HTML).
    - 📊 **PowerPoint:** 편집 및 공유가 가능한 `.pptx` 파일.
3.  **Automation:**
    - 퀴즈 데이터 자동 추출 및 문제은행 구축.
    - 배치 파일(`.bat`)을 통한 원클릭 수업 시작.

## 🚀 설치 및 시작하기 (Getting Started)

### 사전 요구 사항
- **Node.js** (v18 이상)
- **Python** (v3.10 이상)

### 설치 (Installation)
```bash
# 1. 저장소 클론
git clone https://github.com/rjegjin/Project-SCOPE.git
cd Project-SCOPE

# 2. 필수 패키지 설치
npm install
pip install -r requirements.txt  # (필요 시) pip install pyyaml jinja2 python-pptx
```

### 사용 방법 (Usage)

1.  **새 단원 만들기:**
    - `data/` 폴더에 `04_electricity.yaml` 파일을 생성하고 내용을 입력합니다.
2.  **자료 생성 (Build):**
    - `전체업데이트.bat`를 실행하거나 터미널에서 `python build_all.py`를 실행합니다.
3.  **수업 시작:**
    - `수업시작_*.bat` 파일을 더블 클릭하거나 `npx slidev units/파일명.md`를 실행합니다.

## 📂 프로젝트 구조 (Structure)

```text
Project-SCOPE/
├── data/               # [입력] 수업 내용이 담긴 YAML 파일들
├── scripts/            # [엔진] 파이썬 자동화 스크립트 모음
│   ├── build_all.py    # 전체 빌드 마스터 스크립트
│   ├── legacy_to_yaml.py # 기존 HTML 자료 변환기
│   └── ...
├── templates/          # [틀] 슬라이드/시험지 디자인 템플릿 (Jinja2)
├── units/              # [출력 1] 생성된 마크다운 슬라이드
├── output/             # [출력 2] 생성된 시험지 및 PPTX
├── public/             # 이미지 자산 저장소
└── components/         # Vue.js 커스텀 컴포넌트 (VideoPlayer 등)
```

## 🛠️ Tech Stack
- **Frontend:** [Sli.dev](https://sli.dev/) (Vue 3, Vite, UnoCSS)
- **Engine:** Python (PyYAML, Jinja2, python-pptx)
- **Design:** Tailwind CSS (Emerald Theme)

---
**Project Lead:** The EdTech Master
**Last Updated:** 2026-02-07
