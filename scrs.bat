::toolz::
@echo off

if "%1" == "-h" goto _help
if "%1" == "-0" goto _off
if "%1" == "-1" goto _on
if "%1" == "-r" goto _report
if "%1" == "" goto _report

:_off
call :_report

echo.
echo Turning Screensaver OFF
echo.

Reg add "HKEY_CURRENT_USER\Control Panel\Desktop" /v ScreenSaveActive /t REG_SZ /d 0 /f




goto _end

:_on
call :_report

echo.
echo Turning Screensaver ON
echo.

Reg add "HKEY_CURRENT_USER\Control Panel\Desktop" /v ScreenSaveActive /t REG_SZ /d 1 /f


goto _end

:_report

:: Get reg key value

reg query "HKEY_CURRENT_USER\Control Panel\Desktop" /v ScreenSaveActive  > c:\cli_tools\dump.dmp

for /f "tokens=3" %%a in (c:\cli_tools\dump.dmp) do (
    call :_test %%a
)
del c:\cli_tools\dump.dmp


goto _end



:: Test value of reg key
:_test

    echo.

    if "%1" == "0" echo Screen saver is OFF 
    if "%1" == "1" echo Screen saver is ON 
::    exit /b
    goto _end


:_help

echo.
echo Turns Screensaver On or off
echo.
echo Usage:
echo.
echo     scrs [-0][-1][-r][-h]
echo.
echo         -0    -    Turn Screensaver OFF
echo         -1    -    Turn Screensaver ON
echo         -r    -    Report Screensaver Status
echo         -h    -    Help (This Page)
echo.


:_end

exit /b
