#!/usr/bin/env bash
set -e

echo "========================================================"
echo "  EVE burst error R (PS Vita) - English Patch Installer"
echo "  Title ID: PCSG00817"
echo "========================================================"
echo ""

if [ ! -f "data.psarc" ]; then
    echo "[!] 'data.psarc' not found in current directory!"
    echo "Please copy your original decrypted data.psarc here and re-run."
    exit 1
fi

PYTHON_CMD=""
if command -v python3 &>/dev/null; then
    PYTHON_CMD="python3"
elif command -v python &>/dev/null; then
    PYTHON_CMD="python"
else
    echo "[!] Python 3 is required. Please install python3."
    exit 1
fi

$PYTHON_CMD patcher.py "data.psarc" "data_patched.psarc"

echo ""
echo "Patch complete! Replace data.psarc with data_patched.psarc in your Vita / Vita3K app folder."
