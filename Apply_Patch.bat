@echo off
setlocal
title EVE burst error R - English Patch Installer
echo ========================================================
echo   EVE burst error R (PS Vita) - English Patch Installer
echo   Title ID: PCSG00817
echo ========================================================
echo.

if not exist "data.psarc" (
    echo [!] "data.psarc" not found in this folder!
    echo.
    echo Please copy your original decrypted "data.psarc" from your
    echo PS Vita or Vita3K directory into this folder and run this batch again.
    echo.
    pause
    exit /b 1
)

echo [*] Found data.psarc!
echo [*] Checking for Python...

python --version >nul 2>&1
if %errorlevel% neq 0 (
    py --version >nul 2>&1
    if %errorlevel% neq 0 (
        echo [!] Python 3 was not detected on your system.
        echo Please install Python from https://www.python.org/ or the Microsoft Store.
        echo.
        pause
        exit /b 1
    ) else (
        set PYCMD=py
    )
) else (
    set PYCMD=python
)

echo [*] Running translation patcher...
%PYCMD% patcher.py "data.psarc" "data_patched.psarc"

if %errorlevel% equ 0 (
    echo.
    echo ========================================================
    echo   PATCH COMPLETE!
    echo ========================================================
    echo.
    echo Your translated archive is ready: "data_patched.psarc"
    echo.
    echo Next Steps:
    echo 1. Vita3K: Rename "data_patched.psarc" to "data.psarc" and replace the
    echo    original in your ux0/app/PCSG00817/data/ folder.
    echo 2. Real PS Vita: Copy "data_patched.psarc" as "data.psarc" into
    echo    ux0:rePatch/PCSG00817/data/data.psarc (requires rePatch plugin).
    echo.
) else (
    echo.
    echo [!] Patching encountered an error. Please review the output above.
    echo.
)

pause
