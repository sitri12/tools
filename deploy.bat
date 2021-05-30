::Toolz::
@echo off
setlocal enabledelayedexpansion

if "%1" == "-h" goto _help 
if "%1" == "-m" goto _make
if "%1" == "-d" goto _deploy
if "%1" == "-a" goto _auto
if "%1" == "-s" goto _single 
::if "%1" == "" 

:_auto

    if "%2"=="" goto _error
    
    set dest=%2
    if exist %cd%\"deploy.cfg" del %cd%\deploy.cfg
    
    for /f "tokens=*" %%a in ('dir /b') do (
    
        call :_add_item %%a %dest% %%a
    
    )

 goto _end
 
:_single
    set /p sfile=File to Deploy: 
    if not exist %cd%\%sfile% call :_error -nofile
    if not exist %cd%\%sfile% exit /b
    
    set /p destdir=Destination Dir: 
    
    echo %sfile%#%destdir%#%sfile% > %cd%\deploy.cfg
    
    goto _end

 
 
:_error

    if "%1" == "-a" echo You need to specify the destination directory in auto mode
    if "%1" == "-nofile" echo %sfile% does not exist in %cd%
    
    
    goto _end

:_make
    set cfg=%2
    echo %cfg%
    
    if exist "deploy.cfg" call :_overwrite

    set /p dest=Destination directory: 

    for /f "tokens=*" %%a in ('dir /b') do (
    
    
        echo %%a
        echo.
    
        set /p fil = Destination file name:  
        
        if  "%fil%" == "" (call :_add_item  %%a %dest% %%a)
        if not "%fil%" == "" (call :_add_item %%a %dest% %fil)
    )
goto _end

:_add_item

    echo adding item %1 to Db
    
    echo %1#%2#%3 >> %cd%\deploy.cfg

goto _end

:_overwrite

    set /p opt=DEPLOY.CFG already exists. Overwrite? (Y^|n)
    if "opt"=="y" del deploy.cfg
    if "opt"=="Y" del deploy.cfg
    goto _end

:_deploy


    echo copying files ... 
    echo.

    for /f "tokens=1,2,3 delims=#" %%a in (deploy.cfg) do (
    
        if not exist %%b md %%b
        copy /v  %cd%\%%a %%b%%c >> nul

    )
goto _end

:_help

echo Depoloy.bat    -    ver 1.00               MAN Page                    20210426
echo ================================================================================
echo.
echo Synopsis
echo ======== 
echo.
echo Tool for deploying scripts and/or tools quickley and easily.
echo.
echo Usage
echo =====
echo.
echo    deploy [-h][-m][-d][-a ^<Destination_path^>]
echo.
echo        -h  -   Displays HELP (This Page)
echo        -m  -   MAKE a deploy.cfg file for directory 
echo        -d  -   Deploy's tools/scripts from deploy.cfg held in directory
echo        -a  -   Auto mode
echo        -s  -   Single file mode (WiP) 
echo.
echo.           
echo Notes
echo =====
echo.
echo      The MAKE option will ask you once for the destination directory and on each
echo      file in the directory you will be asked if another name when copied to the 
echo      destination directory will be needed.



:_end

    exit /b      