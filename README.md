# Kanata Keyboard Configuration

> A keyboard-first workflow for GNOME and terminal work: dual-purpose keys, programming symbols, window and workspace controls, and text-editing shortcuts — without leaving the home row.

This README documents the supplied Kanata configuration. It describes the mappings as written in the config; shortcuts that invoke GNOME or application actions depend on those shortcuts being configured and supported by the active desktop or application.

---

## Contents

- [Design overview](#design-overview)
- [How tap-hold works](#how-tap-hold-works)
- [Layer map](#layer-map)
- [Layer 1 — Main](#layer-1--main)
- [Layer 2 — Symbols and programming](#layer-2--symbols-and-programming)
- [Layer 3 — Windows, workspaces, and media](#layer-3--windows-workspaces-and-media)
- [Layer 4 — Editing and mouse-wheel emulation](#layer-4--editing-and-mouse-wheel-emulation)
- [Function-row controls](#function-row-controls)
- [Configuration reference](#configuration-reference)
- [Learning the layout](#learning-the-layout)
- [Troubleshooting notes](#troubleshooting-notes)

---

## Design overview

The configuration keeps the familiar QWERTY layout for ordinary typing while assigning extra actions to keys based on whether they are **tapped** or **held**.

| Principle | How it is implemented |
|---|---|
| Keep normal typing familiar | Letters and common punctuation generally retain their tap output. |
| Reduce finger travel | Navigation, modifiers, editing, and window controls are placed around the home row. |
| Use the thumbs for layers | Hold **Space** for symbols, **Left Meta** for window/workspace controls, or **Left Ctrl** for editing tools. |
| Make common actions accessible | The function row and letter keys can trigger shortcuts when held. |
| Keep the config reloadable | Layer 3 maps the F12 position to Kanata's `lrld` action. |

### At a glance

- **Tap** a dual-purpose key to type its normal character or perform its tap action.
- **Hold** it to activate its secondary action.
- Hold **Space** to access programming symbols.
- Hold **Left Meta** to access window and workspace controls.
- Hold **Left Ctrl** to access editing and mouse-wheel controls.
- The configuration uses a shared **200 ms tap time** and **200 ms hold time**.

---

## How tap-hold works

The configuration defines two timing variables:

```lisp
(defvar
  tap-time 200
  hold-time 200
)
```

Many keys use these variables with Kanata's `tap-hold` action.

| Setting | Value | Meaning |
|---|---:|---|
| `tap-time` | `200` ms | Tap/hold decision timing parameter supplied to `tap-hold`. |
| `hold-time` | `200` ms | Hold timing parameter supplied to `tap-hold`. |

For example, the `s` key is defined as:

```lisp
ss (tap-hold $tap-time $hold-time s lmet)
```

- Tap `S` → types `s`.
- Hold `S` → acts as Left Meta / Super.

**Practical tip:** start by typing normally, then deliberately hold the dual-purpose keys when you want their secondary actions. If a key frequently produces the wrong action, adjust the timing only after identifying which tap-hold behavior is responsible.

---

## Layer map

| Layer | How to access it | Main purpose |
|---|---|---|
| **1 — Main** | Default layer | Everyday typing, home-row modifiers, symbols, and function-row actions |
| **2 — Symbols** | Hold **Space** | Programming punctuation and shifted symbols |
| **3 — Windows / Workspaces** | Hold **Left Meta** | Window snapping, workspace navigation, moving windows, media controls, reload |
| **4 — Editing** | Hold **Left Ctrl** | Cursor movement, deletion shortcuts, and mouse-wheel emulation |

The layer keys are defined as tap-hold actions, so tapping them retains their ordinary key output:

| Key | Tap | Hold |
|---|---|---|
| Space | Space | Layer 2 |
| Left Meta | Left Meta | Layer 3 |
| Left Ctrl | Left Ctrl | Layer 4 |

---

## Layer 1 — Main

Layer 1 is the everyday typing layer. It preserves the QWERTY letter layout but adds tap-hold actions to selected keys.

### Home-row modifiers

| Key | Tap | Hold |
|---|---|---|
| `S` | `s` | Left Meta / Super |
| `D` | `d` | Left Alt |
| `F` | `f` | Left Ctrl |
| `H` | `h` | `Shift + Backtick` |
| `J` | `j` | Right Ctrl |
| `K` | `k` | Right Alt |
| `L` | `l` | Right Meta |

The `H` hold sends `Shift + Backtick`, which the comments identify as the GNOME Activities overview shortcut. Whether that opens Activities depends on the desktop's shortcut settings.

### Number row: digits and shifted symbols

Tap a number key for the digit; hold it for the shifted symbol.

| Key | Tap | Hold |
|---|---:|---|
| Backtick | `` ` `` | `~` |
| `1` | `1` | `!` |
| `2` | `2` | `@` |
| `3` | `3` | `#` |
| `4` | `4` | `$` |
| `5` | `5` | `%` |
| `6` | `6` | `^` |
| `7` | `7` | `&` |
| `8` | `8` | `*` |
| `9` | `9` | `(` |
| `0` | `0` | `)` |
| `-` | `-` | `_` |
| `=` | `=` | `+` |

### Top row: application shortcuts

| Key | Tap | Hold |
|---|---|---|
| `Q` | `q` | `Ctrl + Q` — quit application |
| `W` | `w` | `Ctrl + W` — close tab/window |
| `E` | `e` | `Ctrl + E` — reserved / application-dependent |
| `R` | `r` | `Ctrl + R` — commonly reload or refresh |
| `T` | `t` | `Ctrl + T` — commonly open a new tab |

These are standard key combinations, so the exact action is determined by the focused application.

### Punctuation

| Key | Tap | Hold |
|---|---|---|
| `[` | `[` | `{` |
| `]` | `]` | `}` |
| `\` | `\` | `\|` |
| `;` | `;` | Right Shift modifier |
| `'` | `'` | `"` |
| `,` | `,` | `<` |
| `.` | `.` | `>` |
| `/` | `/` | `?` |

The `A` key is also dual-purpose: tap it for `a`; hold it for **Left Shift**. The bottom-row `Z`, `X`, `C`, and `V` keys send their usual letters when tapped and the common `Ctrl + Z`, `Ctrl + X`, `Ctrl + C`, and `Ctrl + V` shortcuts when held.

### Navigation on the right side

| Key | Tap | Hold |
|---|---|---|
| `Y` | `y` | Home — beginning of line |
| `U` | `u` | Page Down |
| `I` | `i` | Page Up |
| `O` | `o` | End — end of line |

### Media and horizontal scrolling

| Key | Action |
|---|---|
| `P` | Sends `Ctrl + Alt + /` on tap or hold — intended for play/pause |
| `[` | Sends `Ctrl + Alt + ,` on tap or hold — intended for previous track |
| `]` | Sends `Ctrl + Alt + .` on tap or hold — intended for next track |
| `;` | Sends `Shift + Meta + H` on tap or hold — intended to scroll left |
| `'` | Sends `Shift + Meta + L` on tap or hold — intended to scroll right |

These are shortcut emissions, not direct media APIs. Configure the corresponding desktop or application shortcuts if you want these actions to work.

### Caps Lock and Escape

The main layer swaps the usual positions:

- The physical **Caps Lock** position sends **Escape**.
- The physical **Escape** position sends **Caps Lock**.

This is useful if Escape is more valuable near the home row. The same positional swap is retained on the other layers.

---

## Layer 2 — Symbols and programming

**Access:** hold **Space**.

Layer 2 is intended to make common programming punctuation available without reaching as far across the number row. Keys not explicitly remapped generally fall through to their underlying behavior as permitted by the layer/configuration.

### Symbol layout

The table lists the outputs configured in Layer 2:

| Physical key | Output |
|---|---|
| `Q` | `!` |
| `W` | `@` |
| `E` | `#` |
| `R` | `$` |
| `T` | `%` |
| `Y` | `0` |
| `U` | `(` |
| `I` | `)` |
| `O` | `[` |
| `P` | `]` |
| `[` | `[` |
| `]` | `]` |
| `A` | `^` |
| `S` | `&` |
| `D` | `*` |
| `F` | `/` |
| `G` | Backtick |
| `H` | `~` |
| `J` | `\` |
| `K` | `;` |
| `L` | `'` |
| `Z` | `-` |
| `X` | `+` |
| `C` | `_` |
| `V` | `=` |
| `B` | `\` |
| `N` | `,` |
| `M` | `.` |
| `,` | `,` |
| `.` | `.` |
| `/` | `/` or shifted `/` according to the configured mapping |

**Important:** this is a symbol layer, not a complete alternate keyboard layout. For the exact output of any key, the `deflayer two` block in the Kanata config is authoritative.

---

## Layer 3 — Windows, workspaces, and media

**Access:** hold **Left Meta**.

Layer 3 groups desktop navigation and window-management actions on the right half of the keyboard. The emitted shortcuts use Meta/Super combinations and are intended for a GNOME workflow.

### Workspace navigation

| Key | Shortcut sent | Intended action |
|---|---|---|
| `Y` | `Meta + Home` | Switch to first workspace |
| `U` | `Meta + Page Up` | Switch to workspace on the left |
| `I` | `Meta + Page Down` | Switch to workspace on the right |
| `O` | `Meta + End` | Switch to last workspace |

### Window snapping and sizing

| Key | Shortcut sent | Intended action |
|---|---|---|
| `H` | `Meta + Left` | Snap window left |
| `J` | `Meta + Down` | Restore / unmaximize window |
| `K` | `Meta + Up` | Maximize window |
| `L` | `Meta + Right` | Snap window right |

### Move windows between monitors and workspaces

| Key | Shortcut sent | Intended action |
|---|---|---|
| `N` | `Shift + Meta + Left` | Move window to monitor on the left |
| `M` | `Shift + Meta + Page Up` | Move window to workspace on the left |
| `,` | `Shift + Meta + Page Down` | Move window to workspace on the right |
| `.` | `Shift + Meta + Right` | Move window to monitor on the right |

### Media and horizontal scrolling

Layer 3 also exposes the configured play/pause, previous-track, next-track, scroll-left, and scroll-right shortcuts on the `P`, `[`, `]`, `;`, and `'` positions respectively.

### Reload the configuration

The **F12 physical position** is mapped to `lrld` on Layer 3, which invokes Kanata's configuration reload action. To use it, hold Left Meta to activate Layer 3 and press the F12 position.

---

## Layer 4 — Editing and mouse-wheel emulation

**Access:** hold **Left Ctrl**.

Layer 4 is designed for text editing and terminal-oriented workflows.

### Cursor movement

| Key | Output |
|---|---|
| `H` | Left Arrow |
| `J` | Down Arrow |
| `K` | Up Arrow |
| `L` | Right Arrow |

### Deletion and line editing

| Key | Shortcut sent | Intended use |
|---|---|---|
| `,` | `Ctrl + Backspace` | Delete the previous word |
| `.` | `Ctrl + Delete` | Delete the next word |
| `[` | `Ctrl + U` | Delete to the beginning of the line in many terminals |
| `]` | `Ctrl + K` | Delete to the end of the line in many terminals |
| `,` (alternate alias) | `Ctrl + W` | Delete previous word in many terminals |
| `.` (alternate alias) | `Alt + D` | Delete next word in many shells/editors |

**Implementation note:** the supplied config defines several deletion aliases (`tbd`, `tfd`, `dtb`, `dte`, `dwb`, `dwf`), but Layer 4 actually maps the comma and period positions to `@dwb` and `@dwf` respectively. The `tbd`/`tfd` aliases are defined but not used in the displayed layer mapping. Therefore, the active comma/period outputs are `Ctrl + Backspace` and `Ctrl + Delete`.

### Mouse-wheel emulation

| Key | Action |
|---|---|
| `Y` | Wheel left |
| `U` | Wheel down |
| `I` | Wheel up |
| `O` | Wheel right |

The aliases use `mwheel-*` with parameters `50` and `120`, as defined in the configuration.

---

## Function-row controls

In the main layer, the function-row keys keep their ordinary F-key action when tapped and send a configured shortcut when held.

| Key | Tap | Hold sends | Intended action |
|---|---|---|---|
| `F1` | `F1` | `Ctrl + Alt + Q` | Quake-style dropdown terminal |
| `F2` | `F2` | `Alt + F2` | Run a command |
| `F3` | `F3` | `Ctrl + Meta + Down` | Decrease display brightness (shortcut-dependent) |
| `F4` | `F4` | `Ctrl + Meta + Up` | Increase display brightness (shortcut-dependent) |
| `F5` | `F5` | `Alt + F5` | Intended to toggle audio mute |
| `F6` | `F6` | `Alt + F6` | Intended to lower volume |
| `F7` | `F7` | `Alt + F7` | Intended to raise volume |
| `F8` | `F8` | `Alt + F8` | Intended to toggle microphone |
| `F9` | `F9` | `Ctrl + Shift + Alt + R` | Intended screenshot action |
| `F10` | `F10` | `Meta + L` | Lock screen |
| `F11` | `F11` | `F11` | Unmodified |
| `F12` | `F12` on Layer 1 | Reload action on Layer 3 | Reload Kanata config while Layer 3 is active |

The shortcut comments describe the intended actions. The actual effect depends on GNOME, application bindings, and any custom shortcuts configured on the system.

---

## Configuration reference

### Global behavior

```lisp
(defcfg
  process-unmapped-keys yes
  log-layer-changes no
)
```

- `process-unmapped-keys yes` enables Kanata to process keys that are not explicitly remapped by a layer.
- `log-layer-changes no` disables layer-change logging.

### Layer aliases

```lisp
l2 (tap-hold $tap-time $hold-time spc (layer-toggle two))
l3 (tap-hold $tap-time $hold-time lmet (layer-toggle three))
l4 (tap-hold $tap-time $hold-time lctl (layer-toggle four))
```

These aliases connect the Space, Left Meta, and Left Ctrl keys to the three additional layers while preserving their tap behavior.

### Source layout

`defsrc` describes the physical QWERTY keyboard positions that Kanata receives. Each `deflayer` then assigns an output or alias to the corresponding position. When changing a mapping, keep the position order aligned with `defsrc`.

---

## Learning the layout

A practical order for learning this configuration:

1. **Get comfortable with tap-hold.** Practise the `S`, `D`, `F`, `J`, `K`, and `L` home-row modifiers.
2. **Learn one layer at a time.** Start with Space + symbol keys, then add Left Meta + window controls, then Left Ctrl + editing.
3. **Practise by task.** Type a short code snippet, navigate a document, move a window, and edit a command line.
4. **Keep a short cheat sheet nearby.** Focus first on the keys you use several times a day.
5. **Tune timing only after practice.** If taps are regularly interpreted as holds, or holds as taps, test a small timing adjustment and re-evaluate.

### Suggested daily drills

- **Symbols:** hold Space and type brackets, braces, operators, and quotes.
- **Navigation:** use the right-hand `Y U I O` keys for Home, Page Down, Page Up, and End.
- **Editing:** hold Left Ctrl and use `H J K L` for arrows.
- **Window management:** hold Left Meta and use `H J K L` to snap or resize windows.
- **Workspaces:** hold Left Meta and use `Y U I O` and the bracket positions to move between workspaces.

---

## Troubleshooting notes

- **A shortcut does nothing:** confirm that GNOME or the focused application has a matching shortcut configured. Kanata emits key combinations; it does not directly control every desktop feature.
- **A symbol is unexpected:** check the active keyboard layout and verify the corresponding mapping in `deflayer two`. Shifted punctuation can differ between keyboard layouts.
- **A key types a character when you expected a modifier:** practise the hold action and review the shared tap-hold timing.
- **A key behaves differently across layers:** that is expected when the active layer maps the same physical position differently.
- **Layer 3 reload does not work:** confirm Kanata is running with this configuration, then hold Left Meta and press the physical F12 position.

> **Source of truth:** the Kanata configuration file is authoritative. This README is a human-readable guide to the supplied file; update it whenever you change `defsrc`, aliases, or layer mappings.
