::toolz::
@echo off

:========================================================
:
:       GODIR.BAT - recode v2.00
:
:       (c) Paul Mann 20190613
:
:========================================================

:vars

set file=%~dp0\godir.conf

if "%1"=="-f" (
  set file=%2
  shift
  shift
)

::Help Switches

if "%1"=="/h" goto usage
if "%1"=="/?" goto usage
if "%1"=="-h" goto usage
if "%1"=="-help" goto usage
if "%1"=="-man" goto usage

:Args

if "%1"=="" goto _interactive
if "%1"=="-a" goto _add
if "%1"=="-i" goto _interactive
if "%1"=="-l" goto _list
if "%1"=="-e" goto _explorer
if "%1"=="-this" goto _this
if "%1"=="-back" popd
if "%1"=="-edit" notepad.exe godir.conf
if "%1"=="-todo" goto _todo
:: goto _config

:main



  for /f "tokens=1-2 delims=#" %%a in (%file%) do (

    if %%a==%1 (
      echo %%b
      pushd "%%b"
    )
  )

goto end

:_list


  echo.
  echo Alias		: Location (dir)
  echo.

  for /f "tokens=1,2 delims=#" %%a in (%file%) do (
    echo %%a		: %%b
)
goto end

:_add

  call :_exist %2
  if %leave%==TRUE (exit /b)

  echo %2#%3 >> %file%
  echo %3 has been saved to %file% as %2
  echo.

goto end

:_this

call :_exist %2

if %leave%==TRUE (exit /b)

echo %2#%cd% >> %file%
echo %cd% has been saved to %file% as %2
echo.

goto end


:_interactive

  cls
  echo.
  echo Adding a new alias.
  echo.
  echo.
  set /p alias=Name of Alias :
  call :_exist %alias%

  if %leave%==TRUE (exit /b)

  echo.
  set /p loc=Full Path of Directory :
  echo.
  echo %alias%#%loc% >> %file%
  echo %loc% has been saved to %file% as %alias%
  set /p opt=Do you wish to add another Alias to %file%? [y/N]
  if "%opt%"=="y" goto _interactive

goto end

:_explorer

  for /f "tokens=1-2 delims=#" %%a in (%file%) do (
    if %%a==%2 (
      echo Opening %%b in Explorer:
      echo.
      explorer "%%b"
      )
    )

:_exist

   set leave=FALSE

  for /f "tokens=1-2 delims=#" %%a in (%file%) do (

    if %%a==%1 (
      echo.
      echo.
      echo Alias already exists
      echo.
      echo.
      echo %%a		: %%b
      echo.
      echo.
      set leave=TRUE
    )


  )


:end

exit /b


:usage

cls
echo.
echo GODIR  (v2.0)                                                                Man Page
echo======================================================================================
echo.
echo SYNOPSIS
echo.
echo The purpose of this BATCH file is to enable the user to quickly navigate
echo the directory structure when using the Command Line. This is achieved by
echo matching a named ALIAS with it's matching path.
echo.
echo USAGE
echo.
echo      GODIR [Args]
echo.
echo ARGS
echo.
echo      -h                   : This page (NOTE you can also use /h /? and -man)
echo      -a [ALIAS] [PATH]    : Add ALIAS and PATH to godir.conf
echo      -i                   : Interactive mode
echo      -l                   : List all entries in godir.conf
echo      -e [ALIAS]           : Opens ALIAS in explorer
echo      -this [ALIAS]        : Add current path to godir.conf
echo      -back                : Goes back one PATH in the stack
echo      -edit                : Opens godir.conf in NOTEPAD
echo.
echo OTHER CONSIDERATIONS
echo.
::pause
echo If an ALIAS is reused in -i -a or -this it will not be added to godir._conf
echo and the current ALIAS and its PATH will be displayed.

goto end

:_todo
echo.
echo TO DO
echo.
echo 1.  Add check to ensure a PATH only has one ALIAS
echo 2.  Will an init file be needed?
echo 3.  Expand Interactive mode to show basic help without exiting script
echo     and make it slightly prettier.
