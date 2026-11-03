# EVE burst error R — English Translation Patch for PS Vita & Vita3K

**Title ID:** `PCSG00817`  
**Platform:** PlayStation Vita / Vita3K (Windows, Android, Linux, macOS, Steam Deck)  
**Patch Version:** 1.0 (Full Game)

---

## Overview

This is a complete, 100% playable English localization patch for **EVE burst error R** on the PlayStation Vita. 

It combines the official PC-98 English translation for all original dialogue with bespoke localization for console-exclusive remaster scenes and menus, running seamlessly in full HD with complete voice acting and soundtrack preservation.

---

## Features

- **100% Scenario Translation:** All 102 scenario scripts (`01_script/*.bin`) translated (44,565 dialogue lines).
- **Localized Action / Decision Menus:** Look / Examine, Talk, Move, Think, etc. localized while preserving engine internal opcode lookup tables.
- **Localized Title Screen:** Start Investigation (New Game), Resume Investigation (Load), Settings, Case Files (Extra), CG/Movie Gallery, Sound Test, Kojiro & Marina route selectors, and Date tabs.
- **Localized System Settings:** Complete translation of the in-game settings screen (Message Window, Screen Effects, Save Settings, Confirmation Dialogs, Touch/Stick Controls, Volume Sliders & Ducking).
- **Zero Loss:** 1080p remaster art, animated movies, full voice acting, and background music are 100% preserved.

---

## Requirements

1. A legal, decrypted copy of **EVE burst error R** (`PCSG00817`).
2. Python 3 (installed by default on Linux/macOS; available from python.org or Microsoft Store for Windows).

---

## Installation Guide

### Method A: Vita3K (Windows / Android / Steam Deck)

1. Copy `data.psarc` from your decrypted game folder (`.../PCSG00817/data/data.psarc`) into this patch folder.
2. Run the patcher:
   - **Windows:** Double-click `Apply_Patch.bat`
   - **Linux / macOS / Steam Deck:** Run `./apply_patch.sh` or `python3 patcher.py data.psarc data_patched.psarc`
3. In ~2 seconds, `data_patched.psarc` will be created.
4. Rename `data_patched.psarc` to `data.psarc` and replace the original in your game's `data/` folder:
   - **Vita3K (PC):** `<Vita3K-directory>/ux0/app/PCSG00817/data/data.psarc`
   - **Vita3K (Android):** `/sdcard/Android/data/org.vita3k.emulator/files/vita/ux0/app/PCSG00817/data/data.psarc`

---

### Method B: Real PS Vita Hardware (via rePatch)

1. Make sure your Vita has CFW (HENkaku / Enso) with the `rePatch` plugin installed.
2. Follow steps 1–3 above to produce `data_patched.psarc`.
3. Copy `data_patched.psarc` over USB or FTP to your Vita at:
   `ux0:rePatch/PCSG00817/data/data.psarc`
4. Launch the game from LiveArea. The `rePatch` plugin will automatically load the patched English assets without altering your base game.

---

## File Contents

```text
├── Apply_Patch.bat            # 1-click Windows installer
├── apply_patch.sh             # Linux / macOS / Steam Deck installer
├── patcher.py                 # Standalone Python patch injection engine
├── patch_files/
│   ├── 01_script/             # 102 translated scenario bytecode scripts
│   └── 13_sys/                # Localized UI textures (title_01, config1, cmd1)
└── README.md
```

---

## Disclaimer & Credits

- This patch contains **only fan-made script translations and localized interface graphics**.
- **No copyrighted game code, video footage, voice audio, or music is distributed with this patch.** You must dump your own legally purchased copy of *EVE burst error R* (`PCSG00817`).
- EVE burst error is copyright © C's ware / El Dia / RED FLAGSHIP. All rights reserved by their respective owners.
