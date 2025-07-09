@echo off
echo Installing required packages...
pip install -r requirements.txt

echo.
echo Starting Business Idea Generator...
echo.

python main.py

pause
