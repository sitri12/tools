::toolz::
@echo off

:: help switches here

if "%1"=="-h" goto _help
if "%1"=="" goto _help


:_main

for /f "eol=; tokens=1,2" %%a in (%1) do (
  call :_tokens %%a %%b
)

:_tokens

  if "%1"=="-" (cd..)
  if "%1"=="+" (mcd "%2")
  if "%1"=="." (md "%2")
  if "%1"=="@" (pushd "%2")

exit /b

:_help

cls

echo.
echo BMD.BAT (ver 1.0 : (c) Paul Mann 2020)                                     MAN PAGE
echo =============================================================================================================
echo.
echo Synopsis:
echo =========
echo.
echo     Init is a very simple scripting language for creating complex directory structures from a source file.
echo.
echo Usage:
echo ======
echo.
echo     INIT [-h][source_file.dat]
echo.
echo Arguments:
echo ==========
echo.
echo     -h        :  Show this page
echo.
echo Language:
echo =========
echo.
echo      INIT is a very simple scripting language with only 3 commands
echo.
echo     Command          :  Meaning                       :  Equivalent
echo     ----------------------------------------------------------------------------------------
echo       -              :  Go up 1 directory             : cd..
echo       + [directory]  :  Create directory, cd into it  : mcd.bat [directory]
echo       . [directory]  :  Create directory              : md [directory]
echo       @ [directory]  :  Goto directory                : pushd [directory]
echo       ;              :  Comment                       :
echo.
echo Notes:
echo ======
echo.
echo   + Indents are allowed and recommended
echo   + TO DO
echo       - '@' operator to signify starting directory.  Can be used multiple times in a script as a PUSHD call 

goto _end

:_end

exit /b
