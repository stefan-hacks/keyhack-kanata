# keyhack-kanata

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Platform](https://img.shields.io/badge/platform-Linux-blue.svg)
![Desktop](https://img.shields.io/badge/desktop-GNOME-orange.svg)

> A battle-tested Kanata keyboard configuration for **HP EliteBook 840 G8** running **Debian Linux** with **GNOME desktop** and **kitty terminal**.

This configuration transforms a standard laptop keyboard into a productivity powerhouse using [Kanata](https://github.com/jtroo/kanata) — a cross-platform keyboard remapping tool that brings QMK-like functionality to any keyboard.

---

## 📑 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Installation](#-installation)
- [Configuration Breakdown](#-configuration-breakdown)
- [Layer Reference](#-layer-reference)
- [Hardware Context](#-hardware-context)
- [Customization](#-customization)
- [Troubleshooting](#-troubleshooting)
- [Resources](#-resources)

---

## 🎯 Overview

This configuration is optimized for:

| Component | Details |
|-----------|---------|
| **Hardware** | HP EliteBook 840 G8 (business laptop) |
| **OS** | Debian Linux (stable/testing) |
| **Desktop** | GNOME Shell |
| **Terminal** | kitty |
| **Keyboard** | Built-in laptop keyboard with F1-F12 media row |

### Philosophy

The layout follows a **minimal-layer** approach with **tap-hold** as the primary mechanism:

1. **Layer 1 (Base)**: Normal typing with tap-hold modifiers
2. **Layer 2 (Windows)**: Hold Left Meta for window/workspace management
3. **Layer 3 (Editing)**: Hold Space for text editing and navigation

```
┌─────────────────────────────────────────────────────────────┐
│                    LAYER ARCHITECTURE                       │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   F1-F12 Row    →  System controls (media, workspaces)       │
│   Number Row    →  Shift symbols on hold (!@#$%^&*())      │
│   Home Row      →  Modifiers on hold (Meta/Alt/Ctrl)         │
│   Left Meta     →  Layer 2: Window/Workspace management      │
│   Spacebar      →  Layer 3: Text editing + mouse wheel       │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## ✨ Features

### 🎹 Tap-Hold Modifiers (Home Row)

Transform the home row into modifiers when held:

| Key | Tap | Hold |
|-----|-----|------|
| `S` | `s` | Left Meta (Super/Windows) |
| `D` | `d` | Left Alt |
| `F` | `f` | Left Ctrl |
| `H` | `h` | Shift+\` (GNOME activity overview) |
| `J` | `j` | Right Ctrl |
| `K` | `k` | Right Alt |
| `L` | `l` | Right Meta |
| `Backspace` | `backspace` | `delete` |
| `Enter` | `enter` | Right Alt |

### 🔢 Smart Number Row

Numbers output symbols when held — no more reaching for Shift:

| Key | Tap | Hold |
|-----|-----|------|
| `` ` `` | \` | `~` |
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

### 🐱 kitty Terminal Integration

Special bindings for the kitty terminal:

| Alias | Function |
|-------|----------|
| `pt` / `nt` | Previous/Next tab |
| `mls` / `mrs` | Scroll left/right |
| `pp` | Close tab |

### 🐭 Mouse Wheel Layer

Hold Spacebar to access mouse wheel controls:

```
Layer 3 (Space held):
┌───┬───┬───┐
│ ← │ ↑ │ → │  Mouse wheel directions
│ J │ K │ L │  (hold Space + these keys)
└───┼───┼───┘
    │ ↓ │
    └───┘
```

---

## 🚀 Installation

### Prerequisites

```bash
# Install kanata
# Via Homebrew (Linuxbrew)
brew install kanata

# Via cargo
cargo install kanata

# Via GitHub releases
# Download from: https://github.com/jtroo/kanata/releases
```

### Setup udev Rules (Linux)

```bash
# Create uinput permissions
sudo groupadd -f uinput
sudo usermod -aG input $USER
sudo usermod -aG uinput $USER

# Create udev rule
echo 'KERNEL=="uinput", MODE="0660", GROUP="uinput", OPTIONS+="static_node=uinput"' | \
    sudo tee /etc/udev/rules.d/99-kanata.rules

# Reload udev
sudo udevadm control --reload-rules
sudo udevadm trigger
```

### Clone and Configure

```bash
# Clone this repository
git clone https://github.com/stefan-hacks/keyhack-kanata.git
cd keyhack-kanata

# Copy config to kanata location
mkdir -p ~/.config/kanata
cp kanata.kbd ~/.config/kanata/
```

### Systemd Service (Recommended)

Create `~/.config/systemd/user/kanata.service`:

```ini
[Unit]
Description=Kanata keyboard remapper
Documentation=https://github.com/jtroo/kanata
After=default.target

[Service]
Type=simple
Environment=PATH=/usr/local/bin:/usr/local/sbin:/usr/bin:/bin
Environment=DISPLAY=:0
ExecStart=/bin/sh -c 'exec kanata --cfg ~/.config/kanata/kanata.kbd'
Restart=on-failure
RestartSec=5

[Install]
WantedBy=default.target
```

Enable and start:

```bash
# Enable user service
systemctl --user daemon-reload
systemctl --user enable kanata.service
systemctl --user start kanata.service
systemctl --user status kanata.service
```

Or use the provided helper script:

```bash
chmod +x kanata_load.sh
./kanata_load.sh
```

---

## 🔧 Configuration Breakdown

### Global Settings

```lisp
(defcfg
  process-unmapped-keys yes   ; Process all keys
  log-layer-changes no        ; Disable noisy layer logging
)
```

### Variable Definitions

```lisp
(defvar
  tap-time 200    ; 200ms for tap detection
  hold-time 200   ; 200ms for hold detection
)
```

> **Note:** These values are tuned for laptop use. Increase if you experience accidental holds.

### Key Aliases Explained

#### Navigation Keys

| Alias | Description |
|-------|-------------|
| `yy` | `home` — beginning of line |
| `uu` | `pgdn` — page down |
| `ii` | `pgup` — page up |
| `oo` | `end` — end of line |

#### Text Deletion

| Alias | Description |
|-------|-------------|
| `tbd` | `Ctrl+w` — delete word backward (terminal style) |
| `tfd` | `Alt+d` — delete word forward |
| `dwb` | `Ctrl+backspace` — delete word backward |
| `dwf` | `Ctrl+delete` — delete word forward |
| `bdl` | `Ctrl+backspace` — beginning delete line |
| `fdl` | `Shift+Ctrl+delete` — forward delete line |

#### Bracket Modifiers

| Alias | Tap | Hold |
|-------|-----|------|
| `so` | `[` | `{` |
| `sc` | `]` | `}` |
| `pi` | `\` | `\|` |
| `se` | `;` | `:` |
| `ap` | `'` | `"` |
| `co` | `,` | `<` |
| `fu` | `.` | `>` |
| `fs` | `/` | `?` |
| `gm` | `` ` `` | `~` |

---

## 📚 Layer Reference

### Layer 1 — Base Layer

Standard QWERTY with tap-hold modifiers on almost every key.

```
┌────┬────┬────┬────┬────┬────┬────┬────┬────┬────┬────┬────┬────┐
│Esc │@qtd│@pum│@dsb│@isb│@mut│@vdn│@vup│@mic│@psc│@lts│F11 │F12 │
└────┴────┴────┴────┴────┴────┴────┴────┴────┴────┴────┴────┴────┘

┌────┬────┬────┬────┬────┬────┬────┬────┬────┬────┬────┬────┬────┬────┐
│@gm │@1m │@2m │@3m │@4m │@5m │@6m │@7m │@8m │@9m │@0m │@mi │@pl │bspc│
└────┴────┴────┴────┴────┴────┴────┴────┴────┴────┴────┴────┴────┴────┘

┌────┬────┬────┬────┬────┬────┬────┬────┬────┬────┬────┬────┬────┬────┐
│tab │@qq │@ww │ e  │@rr │@tt │@yy │@uu │@ii │@oo │ p  │@so │@sc │@pi │
└────┴────┴────┴────┴────┴────┴────┴────┴────┴────┴────┴────┴────┴────┘

┌────┬────┬────┬────┬────┬────┬────┬────┬────┬────┬────┬────┬────┐
│esc │@aa │@ss │@dd │@ff │ g  │@hh │@jj │@kk │@ll │@se │@ap │ret │
└────┴────┴────┴────┴────┴────┴────┴────┴────┴────┴────┴────┴────┘

┌────┬────┬────┬────┬────┬────┬────┬────┬────┬────┬────┬────┐
│lsft│@zz │@xx │@cc │@vv │ b  │ n  │ m  │@co │@fu │@fs │rsft│
└────┴────┴────┴────┴────┴────┴────┴────┴────┴────┴────┴────┘

┌────┬────┬────┬─────────────────┬────┬────┐
│lctl│@l2 │@la │      @l3        │@ra │ _  │ _  │
└────┴────┴────┴─────────────────┴────┴────┘
        (hold for layer 2) (hold for layer 3)
```

### Layer 2 — Window/Workspace Layer

Hold **Left Meta** to access GNOME window management:

```
┌────┬────┬────┬────┬────┬────┬────┬────┬────┬────┬────┬────┬────┐
│Esc │ _  │ _  │ _  │ _  │ _  │ _  │ _  │ _  │ _  │ _  │ _  │lrld│
└────┴────┴────┴────┴────┴────┴────┴────┴────┴────┴────┴────┴────┘
              (reload config)

┌────┬────┬────┬────┬────┬────┬────┬────┬────┬────┬────┬────┬────┬────┐
│ `  │ _  │ _  │ _  │ _  │ _  │ 6  │ 7  │ 8  │ 9  │ 0  │ _  │ _  │bspc│
└────┴────┴────┴────┴────┴────┴────┴────┴────┴────┴────┴────┴────┴────┘

┌────┬────┬────┬────┬────┬────┬────────┬────────┬────────┬────────┬───┬───┬───┬───┐
│tab │ _  │ _  │ _  │ _  │ _  │@wtl    │@dsl    │@dsr    │@wtr    │@pp│@pt│@nt│ \ │
└────┴────┴────┴────┴────┴────┴────────┴────────┴────────┴────────┴───┴───┴───┴───┘
       (Window snap) (Display L/R)

┌────┬────┬────┬────┬────┬────┬──────┬──────┬──────┬──────┬────┬────┬────┐
│esc │ _  │ _  │ _  │ _  │ _  │@rpl  │@rpd  │@rpu  │@rpr  │@mls│@mrs│ret │
└────┴────┴────┴────┴────┴────┴──────┴──────┴──────┴──────┴────┴────┴────┘
       (Workspace navigation: ←↓↑→)

┌────┬────┬────┬────┬────┬────┬────┬────┬────┬────┬────┬────┐
│lsft│ _  │ _  │ _  │ _  │ _  │@w1 │@w2 │@w3 │@w4 │ _  │rsft│
└────┴────┴────┴────┴────┴────┴────┴────┴────┴────┴────┴────┘
       (Switch to workspace 1-4)
```

### Layer 3 — Editing Layer

Hold **Spacebar** to access text editing and mouse controls:

```
┌────┬────┬────┬────┬────┬────┬────┬────┬────┬────┬────┬────┬────┐
│Esc │@qtd│@pum│@dsb│@isb│@mut│@vdn│@vup│@mic│@psc│@lts│ _  │ _  │
└────┴────┴────┴────┴────┴────┴────┴────┴────┴────┴────┴────┴────┘

┌────┬────┬────┬────┬────┬────┬────┬────┬────┬────┬────┬────┬────┬────┐
│ `  │ _  │ _  │ _  │ _  │ _  │ _  │ _  │ _  │ _  │ _  │ _  │ _  │bspc│
└────┴────┴────┴────┴────┴────┴────┴────┴────┴────┴────┴────┴────┴────┘

┌────┬────┬────┬────┬────┬────┬────────┬────────┬────────┬────────┬───┬────┬────┬───┐
│tab │ _  │ _  │ _  │ _  │ _  │@mwl    │@mwd    │@mwu    │@mwr    │ p │@dtb│@dte│ _ │
└────┴────┴────┴────┴────┴────┴────────┴────────┴────────┴────────┴───┴────┴────┴───┘
       (Mouse wheel: ← ↓ ↑ →)

┌────┬────┬────┬────┬────┬────┬─────┬─────┬─────┬─────┬─────┬─────┬────┐
│esc │ _  │ _  │ _  │ _  │ _  │left │down │ up  │rght │bspc │del  │ret │
└────┴────┴────┴────┴────┴────┴─────┴─────┴─────┴─────┴─────┴─────┴────┘
       (Arrow keys)

┌────┬────┬────┬────┬────┬────┬─────┬─────┬─────┬─────┬────┬────┐
│lsft│ _  │ _  │ _  │ _  │ _  │@dwb │@dwf │@tbd │@tfd │ _  │rsft│
└────┴────┴────┴────┴────┴────┴─────┴─────┴─────┴─────┴────┴────┘
       (Delete word back/fwd, Tab back/fwd)
```

---

## 🖥️ Hardware Context

### HP EliteBook 840 G8 Layout

```
┌─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┐
│ Esc │ F1  │ F2  │ F3  │ F4  │ F5  │ F6  │ F7  │ F8  │ F9  │ F10 │ F11 │ F12 │
│     │ Mute│Vol- │Vol+ │Mic  │Brgt-│Brgt+│Airpl│ Pres│ Call│ Proj│ Bri-│ Bri+│
└─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┘

┌─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬───────┐
│  `  │  1  │  2  │  3  │  4  │  5  │  6  │  7  │  8  │  9  │  0  │  -  │  =  │ Bksp  │
└─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴───────┘

┌─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┐
│ Tab │  Q  │  W  │  E  │  R  │  T  │  Y  │  U  │  I  │  O  │  P  │  [  │  ]  │  \  │
└─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┘

┌─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┐
│Caps │  A  │  S  │  D  │  F  │  G  │  H  │  J  │  K  │  L  │  ;  │  '  │Enter│
└─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┘

┌───────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────────┐
│ Shift │  Z  │  X  │  C  │  V  │  B  │  N  │  M  │  ,  │  .  │  /  │ Shift   │
└───────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────────┘

┌─────┬─────┬─────┬───────────────────────────────┬─────┬─────┬─────┐
│Ctrl │ Win │ Alt │           Spacebar            │AltGr│ Win │Ctrl │
└─────┴─────┴─────┴───────────────────────────────┴─────┴─────┴─────┘
```

---

## 🎨 Customization

### Adjust Tap-Hold Timing

If you're getting accidental modifiers or missed modifiers:

```lisp
(defvar
  tap-time 300    ; Increase for slower typing
  hold-time 300
)
```

### Add More Layers

```lisp
;; In defalias section
sym (layer-toggle symbols)

;; In deflayer section
(deflayer symbols
  ...
)
```

### Change GNOME Shortcuts

Modify the workspace/workspace navigation aliases for your setup:

```lisp
;; Default GNOME shortcuts
rpl M-left    ; Previous workspace
rpr M-rght    ; Next workspace

;; Custom shortcuts (e.g., Ctrl+Alt+arrows)
rpl C-A-left
rpr C-A-rght
```

---

## 🔧 Troubleshooting

### Kanata Won't Start

```bash
# Check uinput group
groups $USER | grep uinput

# If not present, re-login or use:
newgrp uinput

# Check device permissions
ls -la /dev/uinput
# Should show: crw-rw---- 1 root uinput
```

### Service Fails to Start

```bash
# Check logs
journalctl --user -u kanata.service -f

# Run in debug mode
kanata --cfg ~/.config/kanata/kanata.kbd --debug
```

### Keys Not Responding

```bash
# Check if kanata is running
ps aux | grep kanata

# Kill kanata and restart
pkill kanata
kanata --cfg ~/.config/kanata/kanata.kbd
```

### Accidental Holds / Double Types

1. Increase `tap-time` in the config (try 250-300ms)
2. Adjust your typing style — lift fingers quickly between keys
3. Use `tap-hold-release` instead of `tap-hold`:

```lisp
;; Old:
ss (tap-hold $tap-time $hold-time s lmet)

;; New:
ss (tap-hold-release $tap-time $hold-time s lmet)
```

### kitty-specific Issues

If kitty shortcuts don't work, check your kitty.conf:

```bash
# In ~/.config/kitty/kitty.conf
map ctrl+shift+t new_tab
map ctrl+shift+w close_tab
map ctrl+shift+, previous_tab
map ctrl+shift+. next_tab
```

---

## 📖 Resources

- **[Kanata Repository](https://github.com/jtroo/kanata)** — Official documentation
- **[Kanata Config Guide](https://github.com/jtroo/kanata/blob/main/docs/config.adoc)** — Complete configuration reference
- **[Kanata Simulator](https://jtroo.github.io/)** — Test configs in browser
- **[HP EliteBook Support](https://support.hp.com)** — Hardware documentation

---

## 📄 License

MIT License — See [LICENSE](LICENSE) file

---

## 🙏 Acknowledgments

- [jtroo](https://github.com/jtroo) for creating Kanata
- The QMK firmware project for inspiration
- The GNOME community for their excellent desktop environment

---

**Maintained by:** @stefan-hacks  
**Last Updated:** 2026-05-11  
**Tested On:** HP EliteBook 840 G8 + Debian 12 + GNOME 43 + kitty 0.31
