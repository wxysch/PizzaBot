@echo off 

call %~dp0pizza\venv\Scripts\activate

cd %~dp0pizza

set TOKEN=5963465941:AAGGLaCZJ2Axingv6r0OtaRjgCeQSEq0Ieg

python bot_telegram.py

pause