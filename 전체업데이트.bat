@echo off
cd /d "%~dp0"
echo [Project S.C.O.P.E.] 모든 수업 자료(슬라이드, 시험지, PPT)를 업데이트합니다...
python scripts/build_all.py
echo.
echo 업데이트 완료! output 폴더와 units 폴더를 확인하세요.
pause
