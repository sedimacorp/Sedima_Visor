@echo off
cd /d "C:\Users\Martha Rubiano\Downloads\demo gas 2"
start "" http://localhost:8001/visor.html
python -m http.server 8001
pause
