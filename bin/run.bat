@echo off
REM
cd /d %~dp0..
cd src
python interface.py
pause