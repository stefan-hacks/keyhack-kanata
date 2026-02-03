# ⌨️ Kanata v1.10 — Kitty + GNOME Power-User Layout

> **Hardware:** SteelSeries Apex 3 TKL · **OS:** Debian 13 Trixie · **DE:** GNOME 48 · **Wayland**  
> **Terminal:** kitty (Catppuccin Mocha · splits · scrollback-nvim)  
> **Kanata:** v1.10.0 · **Config:** `kanata.kbd`

A single-file kanata config that gives kitty full keyboard sovereignty: every active keybinding in your `kitty.conf` is mapped, plus GNOME desktop control, vi-style editing, git macros via a leader key, one-shot modifiers, chords for instant pane-splits, and dynamic macro recording — all without touching kitty's own keybinding system.

---

## Table of Contents

1. [What changed vs your previous config](#1-what-changed-vs-your-previous-config)
2. [Quick Start](#2-quick-start)
3. [Emergency Exit](#3-emergency-exit)
4. [Layer Map](#4-layer-map)
5. [Timing Tuning](#5-timing-tuning)
6. [Base Layer](#6-base-layer)
7. [Home-Row Mods](#7-home-row-mods)
8. [Number-Row Symbols](#8-number-row-symbols)
9. [Edit Layer (hold Space)](#9-edit-layer-hold-space)
10. [Win Layer (hold Left Meta)](#10-win-layer-hold-left-meta)
11. [Kitty Layer (Caps ×2)](#11-kitty-layer-caps-2) ← **new**
12. [Kitty-Tab Layer (Caps ×3)](#12-kitty-tab-layer-caps-3) ← **new**
13. [Fn Layer (Caps ×1)](#13-fn-layer-caps-1) ← **new**
14. [Caps Lock Tap-Dance](#14-caps-lock-tap-dance)
15. [Chords — Instant Pane Splits](#15-chords--instant-pane-splits) ← **new**
16. [Leader Key — Git & Kitty Macros](#16-leader-key--git--kitty-macros) ← **new**
17. [One-Shot Modifiers](#17-one-shot-modifiers) ← **new**
18. [Dynamic Macro Record & Play](#18-dynamic-macro-record--play) ← **new**
19. [Complete Kitty Keybinding Coverage](#19-complete-kitty-keybinding-coverage)
20. [Troubleshooting](#20-troubleshooting)
21. [Tuning & Customisation](#21-tuning--customisation)

---

## 1. What changed vs your previous config

These are every concrete fix and addition, in plain language. Nothing was removed without a replacement.

| # | Problem in old config | What we did |
|---|---|---|
| 1 | `layer-toggle` — layers **stayed on** after you released the key | Switched to `layer-while-held` — layers pop the instant you let go |
| 2 | Every single key used plain `tap-hold` with 200 ms timeouts — **every keypress had noticeable input lag** | Switched all keys to `tap-hold-press` — hold resolves the instant you press a *second* key. Zero perceived lag. |
| 3 | `Esc` was remapped to `CapsLock` — **breaks vim, breaks shell cancellation** | `Esc` stays `Esc`. CapsLock is now a tap-dance (see §14) |
| 4 | Several aliases had **identical tap and hold** (e.g. `@pp`, `@mpp`) — dead code | Removed all redundant aliases; every key does something different on tap vs hold |
| 5 | **Zero kitty bindings** — no pane nav, no splits, no scrollback, no tabs | New `kitty` and `kittytab` layers cover every active line in your `kitty.conf` |
| 6 | No way to trigger git commands without typing them character by character | Leader-key sequences: `[Ldr] g s t` → `git status↵` etc. |
| 7 | No sticky/one-shot modifiers — capitalising a single letter required holding Shift | One-shot mods on the `fn` layer |
| 8 | No chords — splitting a pane required typing `Ctrl+Alt+-` manually | `j+k` chord = hsplit, `k+l` chord = vsplit |
| 9 | No dynamic macro — can't record & replay a key sequence | Dynamic macro record/play on the `fn` layer |

Everything from your original that *worked well* is kept at the **same physical key positions**: number-row symbols, QWERTY-row Ctrl shortcuts, home-row mods, the editing layer arrow/delete layout, the workspace-snap layer, the F-row system shortcuts.

---

## 2. Quick Start

```bash
# Install kanata (Debian 13 has it in repos)
sudo apt install kanata

# Copy config
mkdir -p ~/.config/kanata
cp kanata.kbd ~/.config/kanata/kanata.kbd

# Test run (Ctrl+C to stop)
sudo kanata --cfg ~/.config/kanata/kanata.kbd

# Persistent: systemd user service
mkdir -p ~/.config/systemd/user
cat > ~/.config/systemd/user/kanata.service <<EOF
[Unit]
Description=Kanata keyboard remapper

[Service]
ExecStart=/usr/bin/kanata --cfg %h/.config/kanata/kanata.kbd
Restart=on-failure

[Install]
WantedBy=default.target
EOF
systemctl --user enable --now kanata
```

> **`danger-enable-cmd`** is enabled so the leader-key macros can type text via shell. The official kanata binary supports this. If your distro package does not, build from source with `cargo build --features cmd`.

---

## 3. Emergency Exit

```
Hold simultaneously:   Left Ctrl  +  Space  +  Escape
```

This fires at the raw scan-code level, before kanata processes anything. Works on any layer.

---

## 4. Layer Map

```
  ╔═══════════════════════════════════════════════════════════════════╗
  ║  LAYER STACK  (top = highest priority)                           ║
  ║                                                                  ║
  ║   fn          ← Caps Lock × 1 then hold   (one-shots, dyn-mac) ║
  ║   kitty       ← Caps Lock × 2 then hold   (pane/split/scroll)  ║
  ║   kittytab    ← Caps Lock × 3 then hold   (alt+1..9 tabs)      ║
  ║   win         ← hold Left Meta            (GNOME windows/WS)   ║
  ║   edit        ← hold Space                (arrows, word-del)   ║
  ║   base        ← always active                                  ║
  ║                                                                  ║
  ║  Transparent keys ( _ ) fall through to the layer below.        ║
  ╚═══════════════════════════════════════════════════════════════════╝
```

---

## 5. Timing Tuning

Four numbers control everything. Edit the `defvar` block at the top of `kanata.kbd`:

| Variable | Default | Controls |
|----------|---------|----------|
| `$tt` | 170 ms | Tap timeout — release faster than this = tap |
| `$ht` | 220 ms | Hold timeout — only matters if you hold a key *alone* with nothing else pressed |
| `$td` | 240 ms | Tap-dance gap — max time between successive Caps taps |
| `$os` | 900 ms | One-shot lifetime — sticky mod auto-cancels after this |

**Fast typer?** Drop `$tt` to 130. **Mis-triggering holds?** Raise to 200. Live-reload (`[Ldr] r l`) lets you test changes without restarting.

---

## 6. Base Layer

```
  BASE LAYER  (always active)
  ═══════════════════════════════════════════════════════════════════════

  [Esc] [F1↕] [F2↕] [F3↕] [F4↕] [F5↕] [F6↕] [F7↕] [F8↕] [F9↕] [F10↕] [F11] [F12]
         ↕ = tap F-key / hold = your original system shortcut (see §8 below)

  [`↕]  [1↕]  [2↕]  [3↕]  [4↕]  [5↕]  [6↕]  [7↕]  [8↕]  [9↕]  [0↕]  [-↕]  [=↕]  [Bsp↕]
         ↕ = tap digit / hold shifted symbol                          Bsp/Del

  [Tab] [q↕]  [w↕]  [e]   [r↕]  [t↕]  [y↕]  [u↕]  [i↕]  [o↕]  [p]   [[↕]  []↕]  [\↕]
         C-q   C-w         C-r   C-t   Home  PgDn  PgUp  End         {     }     |

  [CL↕] [a↕]  [s↕]  [d↕]  [f↕]  [g]   [h↕]  [j↕]  [k↕]  [l↕]  [;↕]  ['↕]  [Ret↕]
   ↕tap-dance  C-A   Meta  Alt   Ctrl         ~    RCtl  RAlt  RMet  :     "    Ret/RAlt
   fn/kitty/
   kittytab

  [LSft][z↕]  [x↕]  [c↕]  [v↕]  [b]   [n]   [m]   [,↕]  [.↕]  [/↕]  [RSft]
         C-z   C-x   C-c   C-v                       <     >     ?

  [LCtl][Win↕][LAlt]        [Edit↕]        [RAlt][Ldr] [RCtl]
         ↕=win layer  ↕=edit layer          leader key

  ═══════════════════════════════════════════════════════════════════════
```

---

## 7. Home-Row Mods

Every home-row key is a `tap-hold-press`: **tap** = the letter, **hold + press another key** = the modifier. The hold fires the instant you press the next key — no waiting.

```
         LEFT HAND                           RIGHT HAND
  ┌────┬────┬────┬────┐            ┌────┬────┬────┬────┐
  │  a │  s │  d │  f │            │  h │  j │  k │  l │
  │    │    │    │    │            │    │    │    │    │
  │ tap│ tap│ tap│ tap│            │ tap│ tap│ tap│ tap│
  │  a │  s │  d │  f │            │  h │  j │  k │  l │
  │    │    │    │    │            │    │    │    │    │
  │ hld│ hld│ hld│ hld│            │ hld│ hld│ hld│ hld│
  │ C-A│ Met│ Alt│ Ctl│            │  ~ │RCtl│RAlt│RMet│
  └────┴────┴────┴────┘            └────┴────┴────┴────┘
```

| Key | Tap | Hold | Why |
|:---:|:---:|:---:|---|
| A | `a` | Ctrl+A | Select-all — your original, kept |
| S | `s` | Meta (Super) | GNOME's primary WM modifier |
| D | `d` | Alt | Second most common modifier |
| F | `f` | Ctrl | Most frequent: Ctrl+C, Ctrl+V, Ctrl+W … |
| H | `h` | `~` (tilde) | Your original `hh` alias — shell home dir |
| J | `j` | Right Ctrl | Mirror of left Ctrl |
| K | `k` | Right Alt | Mirror of left Alt |
| L | `l` | Right Meta | Mirror of left Meta |

---

## 8. Number-Row Symbols

Tap = digit. Hold = the shifted symbol on that key. Exactly your original layout, now with zero-lag `tap-hold-press`.

```
  [`/~] [1/!] [2/@] [3/#] [4/$] [5/%] [6/^] [7/&] [8/*] [9/(] [0/)] [-/_] [=/+]
```

---

## 9. Edit Layer (hold Space)

Hold **Space** to enter the editing layer. Release Space to return to base. (Your original used `layer-toggle` which stayed on — this is now fixed.)

```
  EDIT LAYER  (hold Space)
  ═══════════════════════════════════════════════════════════════════════

  [ _ ] [ _ ] [ _ ] [ _ ] [ _ ] [ _ ] [ _ ] [ _ ] [ _ ] [ _ ] [ _ ] [ _ ] [ _ ]

  [ _ ] [ _ ] [ _ ] [ _ ] [ _ ] [ _ ] [ _ ] [ _ ] [ _ ] [ _ ] [ _ ] [ _ ] [ _ ] [ _ ]

  [ _ ] [ _ ] [ _ ] [ _ ] [ _ ] [ _ ] [←whl][↓whl][↑whl][→whl][ _ ] [C-U] [C-K] [ _ ]
                                       mouse wheel               del-to  del-to
                                                                 line-start line-end

  [ _ ] [ _ ] [ _ ] [ _ ] [ _ ] [ _ ] [ ← ] [ ↓ ] [ ↑ ] [ → ] [Bsp] [Del] [Ret]
                                       ── arrow keys (vi hjkl) ──

  [ _ ] [ _ ] [ _ ] [ _ ] [ _ ] [ _ ] [C-Bs][C-Dl][C-W] [A-D] [ _ ] [ _ ]
                                       ── word delete ──────────

  ═══════════════════════════════════════════════════════════════════════
```

| Position | Action | Description |
|:---:|---|---|
| H J K L | ← ↓ ↑ → | Arrow keys in vi positions |
| Y U I O | Mouse wheel ← ↓ ↑ → | Scroll without leaving keyboard |
| [ ] | Ctrl+U / Ctrl+K | Delete to line start / end |
| ; ' | Backspace / Delete | Character delete |
| N M | Ctrl+Bsp / Ctrl+Del | Word delete backward / forward |
| , . | Ctrl+W / Alt+D | Word delete (alternate) |

---

## 10. Win Layer (hold Left Meta)

Hold **Left Meta** (the physical Windows key) to enter the GNOME workspace/window layer. Same physical positions as your original layer "two".

```
  WIN LAYER  (hold Left Meta)
  ═══════════════════════════════════════════════════════════════════════

  [ _ ] [ _ ] [ _ ] [ _ ] [ _ ] [ _ ] [ _ ] [ _ ] [ _ ] [ _ ] [ _ ] [ _ ] [LRLD]
                                                                            live-reload

  [ _ ] [ _ ] [ _ ] [ _ ] [ _ ] [ _ ] [ _ ] [ _ ] [ _ ] [ _ ] [ _ ] [ _ ] [ _ ] [ _ ]

  [ _ ] [ _ ] [ _ ] [ _ ] [ _ ] [ _ ] [DSL] [DSR] [ _ ] [ _ ] [DSW] [TAB←][TAB→][ _ ]
                                       desktop slide        desktop  tab reorder
                                       left  right          switch

  [ _ ] [ _ ] [ _ ] [ _ ] [ _ ] [ _ ] [←  ] [↓  ] [↑  ] [→  ] [M←L] [M→R][Ret]
                                       ── window snap ──    move to monitor

  [ _ ] [ _ ] [ _ ] [ _ ] [ _ ] [ _ ] [WS1] [WS2] [WS3] [WS4] [ _ ] [ _ ]
                                       ── switch workspace ──

  ═══════════════════════════════════════════════════════════════════════
```

| Action | Physical key | Shortcut sent |
|---|:---:|:---:|
| Snap window left/down/up/right | H J K L | Super + arrow |
| Move to left/right monitor | ; ' | Shift+Super+H / Shift+Super+L |
| Switch workspace 1–4 | N M , . | Super + 1…4 |
| Desktop slide left/right | Y U | Alt+F11 / Alt+F12 |
| Desktop switch | P | Ctrl+Meta+/ |
| Reorder tabs | [ ] | Shift+Ctrl+PgUp / PgDn |
| Live-reload kanata | F12 | `lrld` |

---

## 11. Kitty Layer (Caps ×2)

**This is the big new addition.** Double-tap Caps Lock then hold to activate. Every active keybinding from your `kitty.conf` lives here, organised so the right hand does the same directional thing across three rows:

```
  KITTY LAYER  (Caps Lock × 2 then hold)
  ═══════════════════════════════════════════════════════════════════════

  [ _ ] [ _ ] [ _ ] [ _ ] [ _ ] [ _ ] [ _ ] [ _ ] [ _ ] [ _ ] [ _ ] [ _ ] [ _ ]
  [ _ ] [ _ ] [ _ ] [ _ ] [ _ ] [ _ ] [ _ ] [ _ ] [ _ ] [ _ ] [ _ ] [ _ ] [ _ ] [ _ ]

  [ _ ] [HSP] [VSP] [SB ] [SBL] [BCS] [RW ] [RS ] [RT ] [RN ] [URL] [NW ] [NT ] [CT ]
         hsplit vspl scrollback   broadcast  ─── pane RESIZE ───  URL  new   new  close
                     full  last                   wider shor tall narr hints win   tab  tab

  [ _ ] [KRC] [LR ] [F+ ] [F- ] [ _ ] [ ← ] [ ↓ ] [ ↑ ] [ → ] [FLT] [PIN] [ _ ]
         kitty layout font  font        ──── pane NAVIGATE ────   float pin
         reload rotate size  size

  [ _ ] [ _ ] [ _ ] [ _ ] [ _ ] [ _ ] [ ← ] [ ↓ ] [ ↑ ] [ → ] [ _ ] [ _ ]
                                       ──── pane MOVE ─────────

  ═══════════════════════════════════════════════════════════════════════

  Right-hand vertical stacking:
    QWERTY row  →  RESIZE   (Alt+Shift+hjkl)
    Home row    →  NAVIGATE (Alt+hjkl)
    Bottom row  →  MOVE     (Ctrl+Shift+Alt+hjkl)
```

### Full kitty binding map on this layer

| Physical key | Kitty action | Shortcut sent |
|:---:|---|:---:|
| Q | Horizontal split | Ctrl+Alt+− |
| W | Vertical split | Ctrl+Alt+\\ |
| E | Scrollback → nvim (full) | Ctrl+Shift+H |
| R | Scrollback → nvim (last cmd) | Ctrl+Shift+G |
| T | Broadcast to all panes | Ctrl+Shift+B |
| P | Open URL with hints | Ctrl+Shift+U |
| [ | New window (same directory) | Ctrl+Shift+Enter |
| ] | New tab (same directory) | Ctrl+Shift+N |
| \\ | Close current tab | Ctrl+Shift+W |
| A | Reload kitty config | Ctrl+Alt+R |
| S | Rotate pane layout | Ctrl+Alt+Space |
| D | Font size bigger | Ctrl+= |
| F | Font size smaller | Ctrl+− |
| H / J / K / L | Navigate pane ← ↓ ↑ → | Alt + H/J/K/L |
| Y / U / I / O | Resize pane wider/shorter/taller/narrower | Alt+Shift + H/J/K/L |
| N / M / , / . | Move pane ← ↓ ↑ → | Ctrl+Shift+Alt + H/J/K/L |
| ; | Toggle pane float | Ctrl+Shift+Alt+F |
| ' | Toggle pane pin | Ctrl+Shift+Alt+P |

---

## 12. Kitty-Tab Layer (Caps ×3)

Triple-tap Caps Lock then hold. The number row maps directly to `alt+1` through `alt+0` (tabs 1–10). Tab prev/next sit on `−` and `=`.

```
  KITTY-TAB LAYER  (Caps Lock × 3 then hold)
  ═══════════════════════════════════════════════════════════════════════

  [ _ ] [ _ ] [ _ ] [ _ ] [ _ ] [ _ ] [ _ ] [ _ ] [ _ ] [ _ ] [ _ ] [ _ ] [ _ ]

  [ _ ] [T1 ] [T2 ] [T3 ] [T4 ] [T5 ] [T6 ] [T7 ] [T8 ] [T9 ] [T10] [T←] [T→] [ _ ]
         ─────────── goto tab 1 through 10 ───────────────────────   prev  next

  ═══════════════════════════════════════════════════════════════════════
```

| Key | Kitty action | Shortcut sent |
|:---:|---|:---:|
| 1–9 | Goto tab 1–9 | Alt + 1…9 |
| 0 | Goto tab 10 | Alt + 0 |
| − | Previous tab | Ctrl+Shift+Tab |
| = | Next tab | Ctrl+Tab |

---

## 13. Fn Layer (Caps ×1)

Single-tap Caps Lock then hold. One-shot modifiers on the left home row, dynamic macro on the right, live-reload on F12.

```
  FN LAYER  (Caps Lock × 1 then hold)
  ═══════════════════════════════════════════════════════════════════════

  [ _ ] [ _ ] [ _ ] [ _ ] [ _ ] [ _ ] [ _ ] [ _ ] [ _ ] [ _ ] [ _ ] [ _ ] [LRLD]
                                                                            live-reload

  [ _ ] [ _ ] [ _ ] [ _ ] [ _ ] [ _ ] [ _ ] [ _ ] [ _ ] [ _ ] [ _ ] [ _ ] [ _ ] [ _ ]
  [ _ ] [ _ ] [ _ ] [ _ ] [ _ ] [ _ ] [ _ ] [ _ ] [ _ ] [ _ ] [ _ ] [ _ ] [ _ ] [ _ ]

  [ _ ] [OS-S][OS-C][OS-A][OS-M][ _ ] [ _ ] [ _ ] [ _ ] [ _ ] [REC] [PLY] [ _ ]
         sticky  sticky sticky sticky                            dyn-  dyn-
         Shift   Ctrl   Alt   Meta                               macro macro
                                                                 rec   play

  ═══════════════════════════════════════════════════════════════════════
```

---

## 14. Caps Lock Tap-Dance

Caps Lock is never sent to the OS. It is a three-way tap-dance — each option stays active while you hold after the final tap:

```
  ┌─────────────────────────────────────────────────────┐
  │             CAPS LOCK TAP-DANCE                      │
  │                                                     │
  │   1 tap  then hold  →  fn layer       (one-shots)  │
  │   2 taps then hold  →  kitty layer    (panes)      │
  │   3 taps then hold  →  kittytab layer (tab goto)   │
  │                                                     │
  │   Inter-tap window: 240 ms                          │
  │   Release Caps  →  back to base immediately         │
  └─────────────────────────────────────────────────────┘
```

**Muscle memory tip:** Single-tap-hold is the fastest path to fn (one-shots). Double-tap-hold for the kitty layer you'll use most. Triple-tap only when you need to jump to a specific tab number.

---

## 15. Chords — Instant Pane Splits

Press two keys simultaneously (within 180 ms). The action fires on the first key release. If the keys don't match a chord, they act normally.

```
  ┌───────────────────────────────────────────────┐
  │            INPUT CHORDS                       │
  │                                               │
  │   [ j ] + [ k ]   →   hsplit  (Ctrl+Alt+−)   │
  │   [ k ] + [ l ]   →   vsplit  (Ctrl+Alt+\)   │
  │                                               │
  │   [ c ] + [ v ]   →   undo    (Ctrl+Z)        │
  │   [ v ] + [ b ]   →   save    (Ctrl+S)        │
  │   [ n ] + [ m ]   →   close tab (Ctrl+Shift+W)│
  └───────────────────────────────────────────────┘
```

The split chords (`j+k` and `k+l`) are the most important ones for kitty workflow. They sit on adjacent home-row keys so you can trigger a split with a single hand, instantly, without activating any layer.

---

## 16. Leader Key — Git & Kitty Macros

Press **Right Meta** (the physical key, bottom-right). Kanata enters sequence mode — keys you type after it are **not** sent to the terminal. They accumulate until they match a sequence, or 450 ms of silence causes the raw keys to be typed instead.

```
  LEADER KEY SEQUENCES
  ═══════════════════════════════════════════

  [Ldr] → g → s → t       ⟹   git status↵
  [Ldr] → g → a → d       ⟹   git add -·          (cursor after space)
  [Ldr] → g → c → m       ⟹   git commit -m ·     (cursor after space)
  [Ldr] → g → p → s       ⟹   git push↵
  [Ldr] → g → l           ⟹   git log --oneline -20↵
  [Ldr] → k → r           ⟹   Ctrl+Alt+R          (reload kitty config)
  [Ldr] → r → l           ⟹   live-reload kanata

  Timeout: 450 ms of no input → raw keys are typed
  ═══════════════════════════════════════════
```

---

## 17. One-Shot Modifiers

On the **fn layer** (Caps ×1 hold), the left home row becomes sticky modifiers:

```
  Caps ×1 hold, then:

  ┌────┬────┬────┬────┐
  │  a │  s │  d │  f │
  │    │    │    │    │
  │ OS-│ OS-│ OS-│ OS-│
  │ Sft│ Ctl│ Alt│ Met│
  └────┴────┴────┴────┘
```

**How it works:**

1. Tap Caps once, hold → fn layer is active
2. Tap `a` → Shift becomes "sticky"
3. Release Caps → back to base
4. Tap any key (e.g. `h`) → outputs **Shift+H** (capital H)
5. Shift auto-releases — next key is normal

Lifetime: 900 ms. If you don't press a second key within 900 ms, the sticky mod cancels silently.

---

## 18. Dynamic Macro Record & Play

Record an arbitrary key sequence at runtime, replay it later. Useful for repetitive tasks that change from day to day.

```
  1.  Tap Caps once, hold  →  fn layer active
  2.  Tap  ;  (semicolon)  →  recording starts
  3.  Release Caps         →  back to base
  4.  Type whatever you need  (e.g. a file path, a repeated command)
  5.  Tap Caps once, hold  →  fn layer again
  6.  Tap  ;  again        →  recording stops
  7.  To replay:
      Tap Caps once, hold  →  fn layer
      Tap  '  (apostrophe) →  recorded sequence plays back
```

---

## 19. Complete Kitty Keybinding Coverage

Every **active** (non-commented) `map` line in your `kitty.conf` is covered. This table shows where each one lives in the kanata layout.

| kitty.conf binding | What it does | Where in kanata |
|---|---|---|
| `alt+1` … `alt+0` | Goto tab 1–10 | **kittytab** layer, number row |
| `ctrl+tab` | Next tab | **kittytab** layer, `=` key |
| `ctrl+shift+tab` | Previous tab | **kittytab** layer, `-` key |
| `ctrl+t` | New tab | **base** layer, hold `t` (Ctrl+T) |
| `ctrl+shift+w` | Close tab | **kitty** layer, `\` key; also **chord** `n+m` |
| `ctrl+shift+n` | New tab with cwd | **kitty** layer, `]` key |
| `ctrl+shift+enter` | New window with cwd | **kitty** layer, `[` key |
| `ctrl+alt+-` | Horizontal split | **kitty** layer, `q` key; also **chord** `j+k` |
| `ctrl+alt+\` | Vertical split | **kitty** layer, `w` key; also **chord** `k+l` |
| `alt+h/j/k/l` | Navigate panes | **kitty** layer, home row H J K L |
| `alt+shift+h/j/k/l` | Resize panes | **kitty** layer, QWERTY row Y U I O |
| `ctrl+shift+alt+h/j/k/l` | Move panes | **kitty** layer, bottom row N M , . |
| `ctrl+alt+space` | Rotate layout | **kitty** layer, `s` key |
| `ctrl+shift+alt+f` | Float toggle | **kitty** layer, `;` key |
| `ctrl+shift+alt+p` | Pin toggle | **kitty** layer, `'` key |
| `ctrl+shift+h` | Scrollback → nvim | **kitty** layer, `e` key |
| `ctrl+shift+g` | Last cmd → nvim | **kitty** layer, `r` key |
| `ctrl+shift+b` | Broadcast | **kitty** layer, `t` key |
| `ctrl+shift+u` | URL hints | **kitty** layer, `p` key |
| `ctrl+alt+r` | Reload kitty config | **kitty** layer, `a` key; also **leader** `k r` |
| `ctrl+=` / `ctrl+-` | Font size ±2 | **kitty** layer, `d` / `f` keys |

---

## 20. Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| Layer stays on after releasing key | Old `layer-toggle` behaviour | This config uses `layer-while-held` — if you see this, you're still running the old file |
| Typing feels sluggish / delayed | `$tt` or `$ht` too high | Lower `$tt` to 130–150 in `defvar` |
| Home-row mod fires when you just want the letter | Typed too slowly, or `$tt` too low | Raise `$tt` to 180–200 |
| Caps tap-dance picks wrong layer | Tapping too slowly between taps | Lower `$td` to 180, or tap faster |
| Leader sequence types raw keys | Sequence didn't match | Check spelling; increase `sequence-timeout` if you're slow |
| Chord fires when you just want two letters | Typed two keys within 180 ms | Raise chord window to 120 ms, or retype more deliberately |
| `cmd`-based macros do nothing | Binary lacks cmd support | Use official kanata binary, or build with `--features cmd` |
| Kitty bindings don't fire | Wrong layer active | Check `log-layer-changes yes` output; make sure Caps tap-dance completed |

---

## 21. Tuning & Customisation

**Add a kitty binding you missed:** Add an alias in §14 with the exact chord kitty expects, then place it on an empty `_` slot in the `kitty` deflayer.

**Change a chord:** Edit the `defchordsv2` block. Format is `(key1 key2) action timeout release-mode (non-chord-layer)`.

**Add a leader sequence:** Add a line to `deffakekeys` with a label and its macro, then add a matching line in `defseq` with the key sequence.

**Swap home-row mod positions:** Change the modifier names in the `defalias` block (§6). Everything else follows automatically.

**Live-reload while editing:** Press `[Ldr] r l` — kanata reloads without restarting. If there's a parse error it keeps the previous config and logs the error.

---

*Built for kanata v1.10.0 · Debian 13 Trixie · GNOME 48 · Wayland · kitty (scrollback-nvim, splits)*
