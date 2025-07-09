# Kanata Keyboard Configuration Documentation

## Summary
This Kanata configuration creates a highly customized keyboard layout with:
- **Tap-hold behavior** on most keys (200ms tap/hold time)
- **5 layers** for specialized functions
- **Modifier keys** remapped to home row positions
- **Navigation keys** on home row
- **Media controls**, **workspace management**, and **symbol layers**
- **Mouse emulation** on navigation layer

## Configuration Details

```lisp
(defcfg
  process-unmapped-keys yes  ; Pass unmapped keys to OS
  log-layer-changes no       ; Disable layer change logging
)

(defvar
  tap-time 200    ; Tap threshold in ms
  hold-time 200   ; Hold threshold in ms
)
```

## Layer Breakdown

### Layer One (Base Layer)
The main typing layer with tap-hold mods and navigation:

| Position             | Key     | Behavior                          |
|----------------------|---------|-----------------------------------|
| **Top Row**          | `caps`  | Toggle Caps Lock                 |
|                      | `F1-F12`| Standard function keys           |
| **Number Row**       | `1-0`   | Standard numbers                 |
|                      | `-/=`  | Minus/Equal                      |
|                      | `bspc` | Backspace                        |
| **Home Row (Left)**  | `a`     | Tap: `a`, Hold: `Shift`          |
|                      | `s`     | Tap: `s`, Hold: `Super`          |
|                      | `d`     | Tap: `d`, Hold: `Alt`            |
|                      | `f`     | Tap: `f`, Hold: `Ctrl`           |
| **Home Row (Right)** | `h`     | Tap: `h`, Hold: `~`              |
|                      | `j`     | Tap: `j`, Hold: `Ctrl`           |
|                      | `k`     | Tap: `k`, Hold: `Alt`            |
|                      | `l`     | Tap: `l`, Hold: `Super`          |
| **Nav Cluster**      | `y`     | Tap: `y`, Hold: `Home`           |
|                      | `u`     | Tap: `u`, Hold: `Page Down`      |
|                      | `i`     | Tap: `i`, Hold: `Page Up`        |
|                      | `o`     | Tap: `o`, Hold: `End`            |
| **Modifiers**        | `lmet`  | Tap: Super, Hold: Layer 2        |
|                      | `rmet`  | Tap: Super, Hold: Layer 3        |
|                      | `rctl`  | Tap: Ctrl, Hold: Layer 4/5 toggle|

### Layer Two (Workspace/Window Management)
Activated by holding left Super key:

| Position        | Key     | Function                         |
|-----------------|---------|----------------------------------|
| **Top Row**     | `F1`    | Quit app (`Ctrl-Alt-Q`)          |
|                 | `F2`    | App menu (`Alt-F2`)              |
|                 | `F3/F4` | Switch desktops                  |
|                 | `F5-F8` | Volume/mic controls              |
|                 | `F9`    | Screenshot                       |
|                 | `F10`   | Lock screen                      |
| **Navigation**  | `y`     | Move workspace left              |
|                 | `u`     | Move window left                 |
|                 | `i`     | Move window right                |
|                 | `o`     | Move workspace right             |
| **Media**       | `m`     | Media previous                   |
|                 | `,`     | Media next                       |
|                 | `.`     | Play/Pause                       |
| **Numpad**      | `n`     | `0`                              |
|                 | `m`     | `$` (Shift+4)                    |

### Layer Three (Navigation/Mouse)
Activated by holding right Super key:

| Position        | Key     | Function                         |
|-----------------|---------|----------------------------------|
| **Mouse**       | `y`     | Mouse left                       |
|                 | `u`     | Mouse down                       |
|                 | `i`     | Mouse up                         |
|                 | `o`     | Mouse right                      |
| **Arrow Keys**  | `h`     | Left arrow                       |
|                 | `j`     | Down arrow                       |
|                 | `k`     | Up arrow                         |
|                 | `l`     | Right arrow                      |
| **Editing**     | `[`     | Delete to line start (`Ctrl-U`)  |
|                 | `]`     | Delete to line end (`Ctrl-K`)    |
|                 | `,`     | Delete word left (`Ctrl-Backspace`)|
|                 | `.`     | Delete word right (`Ctrl-Delete`)|

### Layer Four (Symbols)
Activated by holding right Ctrl key:

| Position        | Key     | Symbol                           |
|-----------------|---------|----------------------------------|
| **Modified**    | `q`     | `!` (Shift+1)                    |
|                 | `w`     | `@` (Shift+2)                    |
|                 | `e`     | `#` (Shift+3)                    |
|                 | `r`     | `$` (Shift+4)                    |
|                 | `t`     | `%` (Shift+5)                    |
|                 | `a`     | `^` (Shift+6)                    |
|                 | `s`     | `&` (Shift+7)                    |
|                 | `d`     | `*` (Shift+8)                    |
| **F12 Key**     | `lrld`  | Reload Kanata config             |

### Layer Five (Brackets)
Alternate symbols layer:

| Position        | Key     | Symbol                           |
|-----------------|---------|----------------------------------|
| **Brackets**    | `q`     | `(` (Shift+9)                    |
|                 | `w`     | `)` (Shift+0)                    |
|                 | `e`     | `[`                              |
|                 | `r`     | `]`                              |
|                 | `t`     | `\|` (Shift+\\)                  |
| **Braces**      | `a`     | `{` (Shift+[)                    |
|                 | `s`     | `}` (Shift+])                    |
| **Quotes**      | `z`     | `'`                              |
|                 | `x`     | `"` (Shift+')                    |

## Key Aliases Reference
```lisp
;; Modifiers
al   = a + Shift      ss   = s + Super
dd   = d + Alt       ff   = f + Ctrl

;; Navigation
yy   = y + Home      uu   = u + Page Down
ii   = i + Page Up   oo   = o + End

;; Editing
aa   = a + Ctrl-A    zz   = z + Ctrl-Z
xx   = x + Ctrl-X    cc   = c + Ctrl-C
vv   = v + Ctrl-V

;; Special
l2   = Super (Layer 2)   l3   = Super (Layer 3)
l4   = Ctrl (Layer 4)    l5   = Ctrl (Layer 5)
```
