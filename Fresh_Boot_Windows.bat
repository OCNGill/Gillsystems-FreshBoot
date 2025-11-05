@echo off
:: ============================================================
::  Fresh_Boot_Windows v1.0
::  Purpose: Safe, non-destructive fresh boot cleanup
::  Author: Stephen Gill with Copilot assistance
:: ============================================================

:: --- Elevation check ---
net session >nul 2>&1
if %errorlevel% neq 0 (
    echo Requesting admin privileges...
    powershell -Command "Start-Process '%~f0' -Verb RunAs"
    exit /b
)

:: --- Clear user temp files ---
del /q /s "%TEMP%\*" >nul 2>&1
del /q /s "C:\Windows\Temp\*" >nul 2>&1

:: --- Clear Windows Event Logs ---
for /F "tokens=*" %%G in ('wevtutil el') DO (
    wevtutil cl "%%G" >nul 2>&1
)

:: --- Clear browser caches (Chrome/Edge/Firefox) ---
:: Chrome
del /q /s "%LocalAppData%\Google\Chrome\User Data\Default\Cache\*" >nul 2>&1
:: Edge
del /q /s "%LocalAppData%\Microsoft\Edge\User Data\Default\Cache\*" >nul 2>&1
:: Firefox
del /q /s "%AppData%\Mozilla\Firefox\Profiles\*\cache2\entries\*" >nul 2>&1

:: --- Clear clipboard ---
echo off | clip

:: --- Flush DNS + ARP ---
ipconfig /flushdns
arp -d *

:: --- Stop any active network traces ---
netsh trace stop >nul 2>&1

:: --- Clear crash dumps ---
del /q /s "%SystemRoot%\Minidump\*" >nul 2>&1
del /q /s "%SystemRoot%\MEMORY.DMP" >nul 2>&1

:: --- Clear recent files list ---
del /q /s "%AppData%\Microsoft\Windows\Recent\*" >nul 2>&1

:: --- Force reboot (fresh boot) ---
shutdown /r /f /t 0