@echo off
echo Creating Virtual Environment
py -3.10 -m venv venv
echo Activating Venv
call venv\Scripts\activate.bat
echo Installing requirements
pip install -r requirements.txt
echo Setup Complete