# keyhack-kanata

This is a highly customized Kanata keyboard configuration designed for efficient navigation, window management, and text editing in a GNOME desktop environment. The layout features a base layer with extensive tap-hold functionality and two specialized layers activated via modifier keys, optimized to work with your specific GNOME setup.

## Key Features

- **Base Layer**: QWERTY layout with comprehensive tap-hold modifications
- **Layer 2**: Workspace/window management (activated by holding `left Meta`)
- **Layer 3**: Text editing and navigation (activated by holding `Space`)
- **Tap-Hold System**: All keys use 200ms tap/hold timing
- **GNOME Integration**: Optimized for your GNOME extensions and keybindings
- **Process Unmapped Keys**: Enabled for better compatibility

## GNOME Environment Integration
Your configuration is optimized for these GNOME settings:
- **Theme**: Adwaita-dark with Hack Nerd Font
- **Keybindings**: Custom workspace switching (Alt+Super+1-9) and window movement (Super+Shift+1-9)
- **Extensions**: Forge (tiling), ArcMenu, Dash-to-Dock, Quake Terminal, Blur My Shell
- **Quake Terminal**: Activated with Ctrl+Alt+Q (matches Kanata's F1 hold function)
- **Ulauncher**: Activated with Alt+Space (doesn't conflict with Kanata's space hold)

## Base Layer (one) - Main Modifications

### Function Keys Row (Aligned with GNOME Functions)
| Key | Tap Action | Hold Action (GNOME Function) |
|-----|------------|------------------------------|
| F1  | F1         | Ctrl+Alt+Q (Quake Terminal)  |
| F2  | F2         | Alt+F2                       |
| F3  | F3         | Ctrl+Alt+↓                   |
| F4  | F4         | Ctrl+Alt+↑                   |
| F5  | F5         | Alt+F5 (Mute)                |
| F6  | F6         | Alt+F6 (Volume Down)         |
| F7  | F7         | Alt+F7 (Volume Up)           |
| F8  | F8         | Alt+F8 (Mic Mute)            |
| F9  | F9         | Alt+F9                       |
| F10 | F10        | Ctrl+Alt+M+L                 |
| F11 | F11        | F11                          |
| F12 | F12        | F12                          |

### Alphanumeric Keys (Optimized for GNOME Workflow)
| Key | Tap Action | Hold Action |
|-----|------------|-------------|
| ` | ` | Shift+` |
| 1-0 | Number | Shift+Number |
| - | - | Shift+- |
| = | = | Shift+= |
| Q | Q | Ctrl+Q (Close Window) |
| W | W | Ctrl+W |
| E | E | Ctrl+E |
| R | R | Ctrl+R |
| T | T | Ctrl+T |
| Y | Y | Home |
| U | U | Page Down |
| I | I | Page Up |
| O | O | End |
| P | P | Ctrl+M+/ |
| [ | [ | Shift+[ |
| ] | ] | Shift+] |
| \ | \ | Shift+\ |
| A | A | Ctrl+A |
| S | S | Meta (Super) |
| D | D | Alt |
| F | F | Ctrl |
| H | H | Shift+` |
| J | J | Right Ctrl |
| K | K | Right Alt |
| L | L | Right Meta |
| ; | ; | Shift+; |
| ' | ' | Shift+' |
| Z | Z | Ctrl+Z |
| X | X | Ctrl+X |
| C | C | Ctrl+C |
| V | V | Ctrl+V |
| , | , | Shift+, |
| . | . | Shift+. |
| / | / | Shift+/ |

### Special Keys (GNOME Integration)
| Key | Tap Action | Hold Action |
|-----|------------|-------------|
| Left Meta | Tap: Meta | Hold: Toggle Layer 2 |
| Space | Tap: Space | Hold: Toggle Layer 3 |
| Backspace | Backspace | Delete |
| Enter | Enter | Right Alt |
| Caps Lock | Escape | N/A |

## Layer 2 (Workspace/Window Management)
*Activated by holding Left Meta - Aligned with GNOME workspace keybindings*

### Navigation Controls
| Key | Function (Matches GNOME Bindings) |
|-----|-----------------------------------|
| Y | Shift+Meta+Page Up (Move window left) |
| U | Alt+F11 (Switch workspace left) |
| I | Meta+Down (Window down) |
| O | Alt+F12 (Switch workspace right) |
| P | Meta+Up (Window up) |
| H | Shift+Meta+Page Down (Move window right) |
| J | Meta+Left (Window left) |
| K | Meta+Down (Window down) |
| L | Meta+Right (Window right) |
| ; | Meta+Up (Window up) |

### Workspace Management
| Key | Function (Matches GNOME Bindings) |
|-----|-----------------------------------|
| B | Alt+Super+1 (Workspace 1) |
| N | Alt+Super+2 (Workspace 2) |
| M | Alt+Super+3 (Workspace 3) |
| , | Alt+Super+4 (Workspace 4) |
| P | Ctrl+M+/ |
| [ | Ctrl+M+, |
| ] | Ctrl+M+. |

## Layer 3 (Text Editing)
*Activated by holding Space - Optimized for text navigation*

### Navigation & Editing
| Key | Tap Action | Hold Action |
|-----|------------|-------------|
| Y | Mouse Wheel Left | N/A |
| U | Mouse Wheel Down | N/A |
| I | Mouse Wheel Up | N/A |
| O | Mouse Wheel Right | N/A |
| H | Left Arrow | N/A |
| J | Down Arrow | N/A |
| K | Up Arrow | N/A |
| L | Right Arrow | N/A |
| [ | Ctrl+U | Ctrl+Backspace |
| ] | Ctrl+K | Shift+Ctrl+Delete |
| , | Ctrl+Backspace | Ctrl+W |
| . | Delete Word Forward | Alt+D |

### Special Functions
| Key | Function |
|-----|----------|
| Backspace | Backspace |
| Space | Space |
| Delete | Delete |

## Configuration Notes

1. **Tap-Hold Timing**: 
   - Tap time: 200ms
   - Hold time: 200ms
   - Consistent across all tap-hold keys

2. **GNOME-Specific Optimizations**:
   - Workspace switching matches GNOME's Alt+Super+[1-9] bindings
   - Window movement aligns with GNOME's Super+Arrow key navigation
   - Quake Terminal activation matches GNOME extension binding (Ctrl+Alt+Q)
   - Close window (Ctrl+Q) matches GNOME's default window closing

3. **Design Philosophy**:
   - Home row keys (HJKL) handle navigation
   - Modifier keys on home position (SDF = Meta/Alt/Ctrl)
   - Layer switching via frequently used keys (Space/Meta)
   - Integration with your GNOME extensions (Forge tiling, ArcMenu, etc.)

## Known Conflicts and Resolutions
1. **Ulauncher**: Uses Alt+Space - doesn't conflict with Space hold for Layer 3
2. **GNOME Screenshot**: Alt+F9 may conflict with other functions - consider rebinding in GNOME if needed
3. **Window Management**: Some Layer 2 functions require Forge tiling extension for full functionality

To use this configuration:
1. Load it with Kanata 
2. Ensure your GNOME keyboard layout matches the base layer (QWERTY)
3. Verify your GNOME extensions (especially Forge) are enabled
4. Customize any conflicting keybindings through GNOME Settings

This configuration is optimized for your current GNOME setup with Hack Nerd Font, Adwaita-dark theme, and your specific extension ecosystem.
