# keyhack-kanata - Efficient Kanata Keyboard Configuration:

This is a highly customized Kanata keyboard configuration designed for efficient navigation, window management, and text editing. The layout features a base layer with extensive tap-hold functionality and two specialized layers activated via modifier keys.

## Key Features

- **Base Layer**: QWERTY layout with comprehensive tap-hold modifications
- **Layer 2**: Workspace/window management (activated by holding `left Meta`)
- **Layer 3**: Text editing and navigation (activated by holding `Space`)
- **Tap-Hold System**: All keys use 200ms tap/hold timing
- **Process Unmapped Keys**: Enabled for better compatibility

## Base Layer (one) - Main Modifications

### Function Keys Row
| Key | Tap Action | Hold Action |
|-----|------------|-------------|
| F1  | F1         | Ctrl+Alt+Q  |
| F2  | F2         | Alt+F2      |
| F3  | F3         | Ctrl+Alt+↓  |
| F4  | F4         | Ctrl+Alt+↑  |
| F5  | F5         | Alt+F5      |
| F6  | F6         | Alt+F6      |
| F7  | F7         | Alt+F7      |
| F8  | F8         | Alt+F8      |
| F9  | F9         | Alt+F9      |
| F10 | F10        | Ctrl+Alt+M+L |
| F11 | F11        | F11         |
| F12 | F12        | F12         |

### Alphanumeric Keys
| Key | Tap Action | Hold Action |
|-----|------------|-------------|
| ` | ` | Shift+` |
| 1-0 | Number | Shift+Number |
| - | - | Shift+- |
| = | = | Shift+= |
| Q | Q | Ctrl+Q |
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
| S | S | Meta |
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

### Special Keys
| Key | Tap Action | Hold Action |
|-----|------------|-------------|
| Left Meta | Tap: Meta | Hold: Toggle Layer 2 |
| Space | Tap: Space | Hold: Toggle Layer 3 |
| Backspace | Backspace | Delete |
| Enter | Enter | Right Alt |
| Caps Lock | Escape | N/A |

## Layer 2 (Workspace/Window Management)
*Activated by holding Left Meta*

### Navigation Controls
| Key | Function |
|-----|----------|
| Y | Shift+Meta+Page Up (Move window left) |
| U | Desktop Left |
| I | Desktop Down |
| O | Desktop Up |
| P | Desktop Right |
| H | Shift+Meta+Page Down (Move window right) |
| J | Window Left |
| K | Window Down |
| L | Window Up |
| ; | Window Right |

### Workspace Management
| Key | Function |
|-----|----------|
| B | Workspace 1 |
| N | Workspace 2 |
| M | Workspace 3 |
| , | Workspace 4 |
| P | Ctrl+M+/ |
| [ | Ctrl+M+, |
| ] | Ctrl+M+. |

## Layer 3 (Text Editing)
*Activated by holding Space*

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

2. **Special Features**:
   - F12 on Layer 2 reloads configuration
   - Mouse wheel emulation on Layer 3
   - Comprehensive window/workspace management
   - Text editing/navigation shortcuts

3. **Design Philosophy**:
   - Home row keys (HJKL) handle navigation
   - Modifier keys on home position (SDF = Meta/Alt/Ctrl)
   - Layer switching via frequently used keys (Space/Meta)

To use this configuration, load it with Kanata and ensure your OS keyboard layout matches the base layer (QWERTY).
