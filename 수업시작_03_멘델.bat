@echo off
cd /d "%~dp0"
echo [Project S.C.O.P.E.] 멘델의 유전 원리 수업을 시작합니다...
echo.
echo * 만약 처음 실행하신다면 잠시만 기다려주세요 (필요한 도구를 로드합니다)...
npx @slidev/cli units/03_mendel.md
if %errorlevel% neq 0 (
    echo.
    echo [오류] Sli.dev가 설치되지 않은 것 같습니다.
    echo 아래 명령어를 터미널에 입력하여 먼저 설치해 주세요:
    echo npm install @slidev/cli @slidev/theme-seriph
)
pause
