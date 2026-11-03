# EVE burst error R — English Translation Patch for PS Vita & Vita3K

**Title ID:** `PCSG00817`  
**Platform:** PlayStation Vita / Vita3K (Windows, Android, Linux, macOS, Steam Deck)  
**Patch Version:** 1.5 (City Map Screen & In-Game System Navigation Bar Localization)

---

## Changelog

### v1.5
- **City Map Screen (`25_uq/map_name.png`):** Localized all 24 location card headers when Kojiro or Marina moves across Tokyo (`Amagi Detective Agency`, `Headquarters Building`, `Inside Headquarters`, `Central Avenue`, `Princess Hotel`, `Sun Mansion`, `Room 402`, `Room 403`, `Katsuragi Det. Agency`, `Inside Katsuragi Agency`, `Ko's House`, `Inside Ko's House`, `Eldia Embassy`, `Inside Embassy`, `International School`, `Inside School`, `Pool`, `Girls' Dorm`, `Kyoko's Room`, `Library`, `Mayako's Room`, `Warehouse District`). Styled with 1:1 bold white typography and original red stroke outline.
- **In-Game Navigation Bar (`13_sys/System01.png`):** Localized all controller shortcut prompts:
  - `[L] Prev Page` / `[R] Next Page`
  - `[Circle] Play Voice`
  - `[Triangle] Quick Load`
  - `[Cross] Back`
- **Master Archive Update:** Rebuilt `data.psarc` with 128 replaced assets.

### v1.4
- **Parent Action Command Bar (`cmd1.png` + `cmd1.gxt`):** Fully localized all 110 command rows across both Left and Right columns. Parent investigation and situation verbs such as `Act Wildly` (Row 47, unlocking `Dance wildly` & `Fire at random`), `Shoot`, `Punch`, `Kiss`, `Touch`, `Hide`, `Escape`, `Sit`, `Change Clothes`, `Surrender`, `Climb`, etc. are now 100% in English with preserved cyan indicators and question mark hexagon badges.
- **System Dialog & Prompts (`dialog.png`):**
  - Localized confirmation buttons (`YES` / `NO`) across both Normal (dark teal) and Active/Hover states (bright cyan glow with arrow indicators).
  - Localized the persistent reminder checkbox (`Don't show again`) for both Unchecked and Checked states, preserving the PS Vita `(△)` triangle prompt and checkbox icons.
- **Archive Injection & Distribution:** Rebuilt master archive with 126 replaced assets.

### v1.3
- **Comprehensive Command Button Localization (All 525 Buttons):** 100% of all in-game investigation choices, sub-actions, targets, and inquiry options across all 8 command texture sheets (`cmd2_1`, `cmd2_2`, `cmd2_3`, `cmd2_4`, `cmd2_5`, `cmd2_6a`, `cmd2_6b`, and `cmd3`) are now fully localized into English.
- **Root Cause Resolution for Investigation Menus:** Decoded the engine's 2-column button layout architecture and Gojūon alphabetical indexing. Fixed missing sub-action buttons (e.g. `Go outside` on Move, `About the case`, `Amagi Detective Offices`, `About the Chief`).
- **Official PC-98 English Parity:** Sourced 504 out of 522 buttons (96.6%) directly from the official PC-98 translation memory, with the remaining remaster/console-exclusive buttons translated and styled with 1:1 drop-shadowed typography.
- **Pixel-Perfect Wiping:** Clean-tiled button interiors preserving the top-left green/gold indicator tabs and angled right bevels across both Normal and Hover states.

### v1.2
- **1:1 Settings & Slider Alignment:** Fixed master configuration sheets (`config00.png` + `config00.gxt`) across all 90 control clusters. Restored Window Opacity and RGB window color customization sliders (`Red (R)`, `Green (G)`, `Blue (B)`), separating them from the `Change Color for Read Text` toggle.
- **Confirmation Buttons Fix:** Stamped correct cell coordinates in active highlight sheet (`config01.png`), resolving the bug where confirmation dialog buttons displayed "Kojiro" instead of "Confirm". Stamped `Don't Confirm` and clean style selectors.
- **Button Interior Clean Sweep:** Re-engineered the 144px button slot wipe (`384..528`, `544..688`, `704..848`) to eliminate all leftover Japanese character strokes while preserving original borders.
- **Controller Shortcut Footer Localization:** Localized the controller shortcut footer in `config03.png` (`[L]/[R] Switch Tab`, `[START] Reset Defaults`, `[Triangle] Voice Test`, `[Cross] Back`) with clean spacing and transparent backgrounds.

### v1.1
- **Word-Boundary Dialogue Wrapping:** Re-wrapped all 102 scenario scripts (`44,565` lines) with word-level line boundaries, preventing mid-word hyphenation/splitting (e.g. `cha / nge`).
- **Full Settings/Config Menu Localization:** Localized remaster HD setting sheets (`config00.png` + `config00.gxt`, `config01.png`), translating Message Window, Screen Effects, Save Settings, Confirmation Prompts, Master/BGM/Voice volume sliders, and all individual character voice selectors.
- **Pill Toggle Buttons:** Localized all toggle pills (`ON`/`OFF`, `Enable`/`Disable`, `Hold Only`/`Toggle`, `Read Only`/`All Text`, `Gothic`/`Mincho`, `Custom`, `Normal`/`Fast`, `Reset Defaults`, `Voice Test`).
- **Command Menu Polish:** Cleaned `LOOK / EXAMINE` command texture (`cmd1.png` + `cmd1.gxt`), eliminating stray glyph boundary artifacts.
- **Decision Sub-Menu Localization:** Localized common decision sub-buttons on `cmd2_1.png` + `cmd2_1.gxt` (`Surroundings`, `Go Outside`, `Akane`, `Camera`, `Table`, `Desk`, `Desk Lamp`).

### v1.0
- Initial full English translation release for PS Vita & Vita3K.

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
