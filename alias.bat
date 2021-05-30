::toolz::
@echo off

::--------------------------------------------------------------------
::
::	ALAIS.BAT	ver 1.01
::
::	A tool for quickly writing aliases under Windows
::
::	(c) Paul Mann 2017 (20170909)
::
::
::--------------------------------------------------------------------

title Alias v1.01
prompt Alias-$$$G
color 0a
echo.
cd


:: we need to read the config file from anywhere

set home=%cd%

set file=%~dp0\alias.config
if "%1"=="-f" (
  set file=%2
  shift
  shift
)

if "%1"=="-h" goto usage


if "%1"=="-a" goto _add
if "%1"=="-i" goto _interactive
if "%1"=="-l" goto _list

if "%1"=="--wipe" goto _wipe


goto _config

:_list


  echo.
  echo Alias		: Function
  echo.

  for /f "tokens=1,3 delims=#" %%a in (%file%) do (
    echo %%a		: %%b



)
goto end

:_wipe 

::This needs work to wipe alias cache

  echo.
  echo Alias		: Function
  echo.

  for /f "tokens=1,3 delims=#" %%a in (%file%) do (
    echo %%a		: %%b



)
goto end



:_interactive

  echo.
  echo alias INTERACTIVE mode
  echo.
  set /p alias=Name of Alais: 

  echo.
  echo Use: command [args] where [args] is either exact arguments (eg dir /b /w)
  echo or variables in the form of $1 ... $9 for %%1 ... %%9 or $n for all arguments
  echo.
  set /p cmd=Command: 
  set /p desc=description:

  echo %alias%#%cmd%#%desc% >> %file%

  call alias.bat
  
  set /p opt=Do you wish to add another Alias to %file%? [y/N]
  if "%opt%"=="y" goto _interactive


  goto end





echo args = %args%


:_add

  if "%4"=="" set args=$* goto _write
  if "%5"=="-n" set args="" & goto _write
  set args=%4
  call alias.bat
  call alias -l


:_write

  echo %2#%3#%args% >> %file%
  goto end

:_config

  for /f "tokens=1,2delims=#" %%a in (%file%) do (
    doskey %%a=%%b $*
)

:: Edit 20200920 - Give feedback at start

  if "%1"=="" goto _init

goto end

:_init

    echo.
    echo 	Aliases  LOADED

:: End EDIT

goto end
:usage

  if "%~2"=="" echo. & call :_GenHlp & goto end

  for /f "tokens=1-3 delims=#" %%a in (%file% ^| findstr "%2") do (

      echo.
      echo %%a		: %%b
      echo.
    if "%%c"=="" goto end
      echo %%c
    goto end
)
:_GenHlp


echo.
echo Quick and dirty ALIAS command written in Batch for windows
echo.
echo USAGE:
echo.
echo ALIAS [-A ^<alias^> ^<command^>][-I][-L][-F ^<file^>][-h [^<alias^>]]
echo.
echo ALIAS	: Processes the alias.config file and sets up aliases
echo.
echo -A	: Create a simple alias with a simple command (eg. ALIAS -A clear cls)
echo.
echo -I	: Interactive mode for creating more complex aliases
echo.
echo -L	: Lists all aliases and commands in ALIAS.CONFIG file
echo.
echo -F	: For using a file other than the default (alias.config)
echo.
echo -H	: Displays this page or the description of the named alias
echo.
echo NOTE: if invoking -F ^<file^> with other options it must be done first
)
:end

exit /b
