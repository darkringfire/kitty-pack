@echo off

set KITTY_PATH=%~dp0.

copy /y "%KITTY_PATH%\klink.exe" "%KITTY_PATH%\plink.exe"

setx KITTY_PATH %KITTY_PATH%
setx PLINK %KITTY_PATH%\plink.exe
setx SCP %KITTY_PATH%\kscp.exe

set CS=HKEY_CURRENT_USER\Software\Classes
set KPPK=%CS%\KiTTY.ppk
set LOAD=%KPPK%\shell\load
set OPEN=%KPPK%\shell\open
set DIRKG=%CS%\Directory\shell\kittygen
set DIRBGKG=%CS%\Directory\Background\shell\kittygen

set ICO="""%%KITTY_PATH%%\keys.ico"""
set KITTY="""%%KITTY_PATH%%\kitty.exe"""
set KAG="""%%KITTY_PATH%%\kageant.exe"""

reg add "%CS%\.ppk"           /ve       /t REG_SZ         /d "KiTTY.ppk" /f
reg add "%KPPK%"              /ve       /t REG_SZ         /d "KiTTY Private Key File" /f
reg add "%KPPK%\DefaultIcon"  /ve       /t REG_EXPAND_SZ  /d "%ICO%" /f
reg add "%KPPK%\shell"        /ve       /t REG_SZ         /d "load" /f
reg add "%LOAD%"              /ve       /t REG_SZ         /d "Load to Authentication Agent" /f
reg add "%LOAD%"              /v "Icon" /t REG_EXPAND_SZ  /d "%ICO%" /f
reg add "%LOAD%\command"      /ve       /t REG_EXPAND_SZ  /d "%KAG% ""%%1""" /f
reg add "%OPEN%"              /ve       /t REG_SZ         /d "Open in Key Generator" /f
reg add "%OPEN%"              /v "Icon" /t REG_EXPAND_SZ  /d "%ICO%" /f
reg add "%OPEN%\command"      /ve       /t REG_EXPAND_SZ  /d "%KITTY% -keygen ""%%1""" /f
reg add "%DIRKG%"             /ve       /t REG_SZ         /d "KiTTY Gen" /f
reg add "%DIRKG%"             /v "Icon" /t REG_EXPAND_SZ  /d "%ICO%" /f
reg add "%DIRKG%\command"     /ve       /t REG_EXPAND_SZ  /d "%KITTY% -keygen" /f
reg add "%DIRBGKG%"           /ve       /t REG_SZ         /d "KiTTY Gen" /f
reg add "%DIRBGKG%"           /v "Icon" /t REG_EXPAND_SZ  /d "%ICO%" /f
reg add "%DIRBGKG%\command"   /ve       /t REG_EXPAND_SZ  /d "%KITTY% -keygen" /f




::pause
