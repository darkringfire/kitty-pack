@echo off

set KITTY_PATH=%~dp0

setx KITTY_PATH %KITTY_PATH%
setx PLINK %KITTY_PATH%plink.exe
setx SCP %KITTY_PATH%kscp.exe

reg import "%KITTY_PATH%kitty_setup.reg"

copy /y "%KITTY_PATH%klink.exe" "%KITTY_PATH%plink.exe"

::pause
