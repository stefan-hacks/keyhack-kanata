# Kanata Keyboard Configuration

This repository contains my custom keyboard layout configuration for [Kanata](https://github.com/jtroo/kanata), a software that allows advanced keyboard remapping and layer-based functionality.

## Overview

This configuration transforms a standard QWERTY keyboard into a highly efficient, layer-based input system with extensive tap-hold functionality, workspace management, and text editing capabilities.

## Layout Structure

### Base Layer (Layer One)
The main typing layer with extensive tap-hold modifications:

**Function Row:**
- F1-F10: Application shortcuts with tap-hold functionality
- F11-F12: Standard function keys

**Alphanumeric Zone:**
- Most keys have dual functionality:
  - **Tap**: Standard character
  - **Hold**: Modified character or shortcut
- Home row keys (`ASDF` and `JKL;`) transform into modifier keys when held

**Modifiers:**
- Left Windows: Layer 2 access (tap for Win, hold for layer)
- Space: Layer 3 access (tap for space, hold for layer)
- Backspace/Enter: Additional modifiers when held

### Layer 2 - Workspace & Window Management
Activated by holding the left Windows key:

- **Workspace navigation**: Switch between workspaces 1-4
- **Window management**: Move windows between workspaces, tile left/right
- **Pane control**: Split panes and navigate between them
- **Media controls**: Playback and volume controls

### Layer 3 - Editing & Navigation
Activated by holding the spacebar:

- **Mouse emulation**: Wheel scrolling in all directions
- **Text navigation**: Word-wise movement and selection
- **Editing commands**: Delete by word, line manipulation
- **Terminal control**: Pane navigation and management

## Key Features

### Tap-Hold System
Most keys implement tap-hold behavior with 200ms timing:
- **Short press**: Primary function (character typing)
- **Long press**: Secondary function (modifiers, shortcuts)

### Home Row Modifiers
The home row becomes modifier keys when held:
- `S` → Left Meta (Windows/Command)
- `D` → Left Alt
- `F` → Left Control
- `H` → Shift + Grave
- `J` → Right Control
- `K` → Right Alt
- `L` → Right Meta

### Efficient Modifier Access
- Eliminates uncomfortable pinky stretching for common modifiers
- Maintains traditional touch typing flow
- Reduces hand movement and strain

### Application Shortcuts
Dedicated function keys for common applications:
- Quick terminal access
- Password manager integration
- Volume and media control
- Workspace management

## Configuration Details

- **Tap Time**: 200ms
- **Hold Time**: 200ms
- **Process Unmapped Keys**: Enabled
- **Layer Change Logging**: Disabled

## Usage

1. Install Kanata
2. Place `kanata.kbd` in the appropriate configuration directory
3. Start Kanata with this configuration file
4. The layout will be active immediately

## Customization

The configuration uses Kanata's domain-specific language with:
- Layer definitions (`deflayer`)
- Key aliases (`defalias`)
- Variables for timing configuration
- Tap-hold combinations for dual-function keys

Modify the timing variables or key mappings in the `defvar` and `defalias` sections to suit personal preferences.

## Requirements

- [Kanata](https://github.com/jtroo/kanata) keyboard remapping software
- Compatible with Windows, Linux, and macOS

This configuration prioritizes ergonomics and efficiency, reducing finger travel and making common shortcuts more accessible while maintaining a familiar base layout for typing.
