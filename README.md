# EVE burst error R — English Translation Patch for PS Vita & Vita3K

**Title ID:** `PCSG00817`  
**Platform:** PlayStation Vita / Vita3K (Windows, Android, Linux, macOS, Steam Deck)  
**Patch Version:** 1.9 (Empty-String Softlock Fix for Glen's Phone Call & Terminal Sequences)

---

## Changelog

### v1.9
- **Fixed Softlock During Glen's Phone Call (`a001.bin`):** Fixed a bug where line `953` (`《スピーカーから流れる音声と、直接受話器へ届く肉声では、》`) was saved wrapped in square brackets `[...]` and stripped down to an empty string `""`, causing the dialogue box to go blank and freeze until switching to Marina's side.
- **Zero Empty-String Regressions (`110` Fixed):** Updated `_strip_pc98_speaker_tags()` so `[...]` stripping can never leave a non-empty line blank, skipped empty `""` entries during translation-memory lookup, and preserved terminal typing animation strings (`a001_6.bin`, `b022_4.bin`) plus `a001_7.bin` line `1026`. Audited all `102` `.bin` scripts (`0` empty-string regressions remaining).

### v1.8
- **100% Scenario Dialogue Coverage:** Audited all 102 `.bin` scripts (`73,208` strings) and translated the 9 missed lines in Koujirou's opening (`a01.bin`), bringing translated dialogue to `44,574` lines (**0** untranslated non-menu, non-speaker dialogue lines remaining).
- **Native Engine Formatting (`[n]` & `[w][h]`):** Switched from raw `\n` (which the Vita engine ignored, causing mid-word wraps) to native `[n]` line breaks, stripped leftover PC-98 inline `[Kojiroh]`/`[Name]` tags, and added automatic `[w080][h080]` / `[w070][h070]` / `[w065][h065]` scaling for long lines so text never clips at the bottom of the 2-line dialogue box.
- **Clearer Installation Guide:** Separated **Update 1.03 (`data3.psarc`, recommended for almost all users)** from **Base Game v1.00 (`data.psarc`)**.

### v1.7
- **Official Update 1.03 Full Compatibility:** Resolves the issue where installing official Update 1.03 (default on PKGi / PKGj) overrode the English script with Japanese dialogue files.
- **Investigation Button Override (`90_update/cmd2_1`):** Injected localized English investigation sub-menu textures (`cmd2_1.png` + `cmd2_1.gxt` containing *Surroundings*, *Camera*, *Cash*, etc.) into the v1.03-exclusive `90_update/` directory so all buttons remain 100% in English on v1.03.
- **Lightweight `data3.psarc` rePatch Release:** Distributed as a standalone ~14.9 MB `data3.psarc` archive. Real PS Vita users (`rePatch`) and Vita3K users can simply drop this single file in place without ever needing to extract, patch, or transfer the 1.1 GB base archive.

### v1.6
- **Side Change Dialog Confirmation Header (`13_sys/dialog.png`):** Baked explicit English prompt header `[ SIDE CHANGE: SWITCH PROTAGONIST? ]` with glowing cyan accents directly onto the master dialog window. Resolves ambiguity during Kojiro $\leftrightarrow$ Marina route switches without requiring modifications to encrypted Sony executables.
- **Universal PSARC Compatibility:** 100% compatible with existing `Apply_Patch.bat` pipeline for PC, Android, and real PS Vita hardware.

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

## In-Game System Confirmation Dialogs (YES / NO Reference)

All dialogue, scenario text, menus, and choice buttons (`YES` / `NO`) are fully localized in English. The confirmation question sentences above the buttons are hardcoded in the game's executable engine. Use this reference to know exactly what the game is asking:

| Japanese Prompt | Triggered By | What YES Confirms | What NO Does |
| :--- | :--- | :--- | :--- |
| **サイトチェンジをします 【小次郎編→まりな編】 よろしいですか？**<br>*(or まりな編→小次郎編)* | **`S.CHANGE`** button<br>*(Right Menu / Screen)* | **YES:** Switches protagonist route (Kojiroh $\leftrightarrow$ Marina) and loads the other story. | **NO:** Cancels switch; stays with the current character. |
| **クイックセーブします。よろしいですか？** | **`Q.SAVE`** button<br>*(Right Menu)* | **YES:** Saves your exact current progress into the Quick Save slot. | **NO:** Cancels without saving. |
| **クイックロードします。よろしいですか？** | **`Q.LOAD`** button<br>*(Right Menu)* | **YES:** Discards unsaved progress and restores your Quick Save. | **NO:** Cancels; stays in the current game state. |
| **タイトルに戻ります。よろしいですか？** | **`TITLE`** button<br>*(Right Menu)* | **YES:** Quits to the Main Menu. Any unsaved progress will be lost. | **NO:** Cancels; resumes gameplay. |
| **セーブデータを上書きします。よろしいですか？** | Save Menu (Slot Selection) | **YES:** Overwrites the selected save slot with your current game. | **NO:** Cancels; lets you pick another slot. |
| **セーブデータをロードします。よろしいですか？** | Load Menu (Slot Selection) | **YES:** Loads the selected save file. | **NO:** Cancels; returns to menu. |

> [!NOTE]
> On the **Side Change** confirmation dialog, checking the bottom checkbox (**`Don't show again`** / `次回から表示しない`) tells the game to remember your preference and switch characters immediately without asking every time.

---

## Requirements

1. A legal, decrypted copy of **EVE burst error R** (`PCSG00817`).
2. Python 3 (installed by default on Linux/macOS; available from python.org or Microsoft Store for Windows).

---

## Installation Guide

> [!IMPORTANT]
> **Which method should you use?**
> Check your game's `ux0/app/PCSG00817/data/` folder (or Vita3K title version):
> - **Do you have Official Update `1.03` installed (or a `data3.psarc` file)?** → Use **Method A (`data3.psarc`)**. Do **not** only patch `data.psarc`, or Update `1.03` will override it with Japanese!
> - **Do you ONLY have Base Game `1.00` (no `data3.psarc`)?** → Use **Method B (`Apply_Patch.bat`)**.

---

### Method A: Update 1.03 Users — Vita3K & Real PS Vita (`data3.psarc` — Recommended)

> [!TIP]
> **No Python and no 1.1 GB file patching required!** Works on **Vita3K** and **Real PS Vita (`rePatch`)** with Official Update `1.03`.

1. Download `EVE_Burst_Error_R_Vita_English_Patch_v1.8_data3_rePatch.zip` (~15 MB) from the [Releases](https://github.com/fiksr/eve-burst-error-r-vita-english-patch/releases) page and extract it.
2. Copy the `data3.psarc` file (`PCSG00817/data/data3.psarc`):
   - **Vita3K (Windows / Linux / macOS / Steam Deck):** Copy `data3.psarc` into `<Vita3K-directory>/ux0/app/PCSG00817/data/data3.psarc` and **overwrite** the existing file.
   - **Vita3K (Android):** Copy `data3.psarc` into `/sdcard/Android/data/org.vita3k.emulator/files/vita/ux0/app/PCSG00817/data/data3.psarc` and **overwrite**.
   - **Real PS Vita (`rePatch`):** Ensure `rePatch.skprx` is enabled in `ur0:tai/config.txt`, then copy the extracted `PCSG00817` folder to `ux0:rePatch/PCSG00817/data/data3.psarc`.
3. Launch the game. `data3.psarc` overrides both the base game and Update `1.03` with all 102 English scripts and localized UI textures.

---

### Method B: Base Game v1.00 ONLY (No Update 1.03 Installed)

1. Download `EVE_Burst_Error_R_Vita_English_Patch_v1.8.zip` and extract it.
2. Copy `data.psarc` (1.1 GB) from your decrypted game folder (`.../PCSG00817/data/data.psarc`) into the extracted patch folder.
3. Run the patcher:
   - **Windows:** Double-click `Apply_Patch.bat`
   - **Linux / macOS / Steam Deck:** Run `./apply_patch.sh` or `python3 patcher.py data.psarc data_patched.psarc`
4. In ~2 seconds, `data_patched.psarc` will be created.
5. Rename `data_patched.psarc` to `data.psarc` and replace the original in your game's `data/` folder:
   - **Vita3K (PC):** `<Vita3K-directory>/ux0/app/PCSG00817/data/data.psarc`
   - **Vita3K (Android):** `/sdcard/Android/data/org.vita3k.emulator/files/vita/ux0/app/PCSG00817/data/data.psarc`
   - **Real PS Vita (`rePatch`):** `ux0:rePatch/PCSG00817/data/data.psarc`

*(Note: If you later install Official Update `1.03`, also copy `data3.psarc` from Method A so `1.03` stays in English.)*

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
