@echo off

set KITTY_PATH=%~dp0

start /D "%KITTY_PATH%" kitty.exe -launcher
