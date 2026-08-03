#!/usr/bin/env python3
"""Generate clean SVG keyboard layer diagrams for keyhack-kanata README."""

import os

OUTDIR = os.path.dirname(os.path.abspath(__file__)) + "/assets"
os.makedirs(OUTDIR, exist_ok=True)

# Dark theme colors matching GitHub dark mode
COLORS = {
    "bg": "#0d1117",
    "key_bg": "#161b22",
    "key_border": "#30363d",
    "key_border_active": "#58a6ff",
    "text_primary": "#c9d1d9",
    "text_secondary": "#8b949e",
    "text_hold": "#58a6ff",
    "text_tap": "#c9d1d9",
    "text_action": "#7ee787",
    "accent": "#58a6ff",
    "layer_label": "#f0883e",
}

KEY_W = 52
KEY_H = 52
KEY_GAP = 5
ROW_GAP = 8
MARGIN = 20

# Standard 60% row lengths
ROW_LENGTHS = [13, 14, 14, 13, 12, 7]

# Key width multipliers
SPECIAL_KEYS = {
    "bspc": 1.5,
    "tab": 1.5,
    "\\": 1.5,
    "caps": 1.75,
    "ret": 2.0,
    "lsft": 2.25,
    "rsft": 2.75,
    "lctl": 1.25,
    "lmet": 1.25,
    "lalt": 1.25,
    "spc": 6.25,
    "ralt": 1.25,
    "rmet": 1.25,
    "rctl": 1.25,
}

# Calculate SVG dimensions
def calc_keyboard_width():
    """Calculate total keyboard width from row 2 (widest row with 14 keys)."""
    total = MARGIN
    for i in range(14):
        # Approximate key names for width calc - use max possible
        w_mult = 1.0
        if i == 0:
            w_mult = SPECIAL_KEYS.get("tab", 1.0)
        elif i == 13:
            w_mult = SPECIAL_KEYS.get("\\", 1.0)
        w = KEY_W * w_mult + (w_mult - 1) * KEY_GAP
        total += w + KEY_GAP
    return total + MARGIN

SVG_WIDTH = int(calc_keyboard_width()) + 20  # extra padding
SVG_HEIGHT = 65 + 6 * (KEY_H + ROW_GAP) + MARGIN + 10  # title + 6 rows + padding


def escape_xml(text):
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def draw_key(x, y, w_mult, tap, hold=None, action=None, active=False):
    w = KEY_W * w_mult + (w_mult - 1) * KEY_GAP
    border = COLORS["key_border_active"] if active else COLORS["key_border"]

    svg = f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{KEY_H}" rx="5" '
    svg += f'fill="{COLORS["key_bg"]}" stroke="{border}" stroke-width="1.5"/>\n'

    # Tap label (top)
    if tap:
        svg += f'<text x="{x + w/2:.1f}" y="{y + 16:.1f}" text-anchor="middle" '
        svg += f'fill="{COLORS["text_tap"]}" font-family="Segoe UI,system-ui,-apple-system,sans-serif" '
        svg += f'font-size="12" font-weight="600">{escape_xml(tap)}</text>\n'

    # Hold label (middle)
    if hold:
        svg += f'<text x="{x + w/2:.1f}" y="{y + 30:.1f}" text-anchor="middle" '
        svg += f'fill="{COLORS["text_hold"]}" font-family="Segoe UI,system-ui,-apple-system,sans-serif" '
        svg += f'font-size="10" font-weight="500">{escape_xml(hold)}</text>\n'

    # Action description (bottom, smaller)
    if action:
        svg += f'<text x="{x + w/2:.1f}" y="{y + 42:.1f}" text-anchor="middle" '
        svg += f'fill="{COLORS["text_action"]}" font-family="Segoe UI,system-ui,-apple-system,sans-serif" '
        svg += f'font-size="8">{escape_xml(action)}</text>\n'

    return svg, w + KEY_GAP


def draw_keyboard(keys_data, layer_title, subtitle, active_keys=None):
    if active_keys is None:
        active_keys = set()

    # Recalculate actual width for this specific key layout
    y = 55
    max_x = 0
    key_idx = 0
    for row_idx, row_len in enumerate(ROW_LENGTHS):
        x = MARGIN
        for _ in range(row_len):
            if key_idx >= len(keys_data):
                break
            key_info = keys_data[key_idx]
            key_name = key_info.get("key", "")
            w_mult = SPECIAL_KEYS.get(key_name, 1.0)
            w = KEY_W * w_mult + (w_mult - 1) * KEY_GAP
            x += w + KEY_GAP
            max_x = max(max_x, x)
            key_idx += 1
        y += KEY_H + ROW_GAP

    actual_width = max(max_x + MARGIN, SVG_WIDTH)
    actual_height = y + MARGIN

    svg_parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {actual_width:.0f} {actual_height:.0f}" width="{actual_width:.0f}" height="{actual_height:.0f}">',
        f'<rect width="100%" height="100%" fill="{COLORS["bg"]}" rx="8"/>',
        f'<text x="{actual_width/2:.0f}" y="24" text-anchor="middle" fill="{COLORS["layer_label"]}" '
        f'font-family="Segoe UI,system-ui,-apple-system,sans-serif" font-size="16" font-weight="700">'
        f'{escape_xml(layer_title)}</text>',
        f'<text x="{actual_width/2:.0f}" y="42" text-anchor="middle" fill="{COLORS["text_secondary"]}" '
        f'font-family="Segoe UI,system-ui,-apple-system,sans-serif" font-size="11">'
        f'{escape_xml(subtitle)}</text>',
    ]

    y = 55
    key_idx = 0
    for row_idx, row_len in enumerate(ROW_LENGTHS):
        x = MARGIN
        for _ in range(row_len):
            if key_idx >= len(keys_data):
                break
            key_info = keys_data[key_idx]
            key_name = key_info.get("key", "")
            w_mult = SPECIAL_KEYS.get(key_name, 1.0)

            is_active = key_name in active_keys or key_info.get("active", False)

            key_svg, advance = draw_key(
                x, y, w_mult,
                key_info.get("tap", ""),
                key_info.get("hold"),
                key_info.get("action"),
                active=is_active
            )
            svg_parts.append(key_svg)
            x += advance
            key_idx += 1
        y += KEY_H + ROW_GAP

    svg_parts.append('</svg>')
    return "\n".join(svg_parts)


# Layer 1 — Base
layer1_keys = [
    {"key": "esc", "tap": "Esc"}, {"key": "f1", "tap": "F1", "hold": "Mute"}, {"key": "f2", "tap": "F2", "hold": "P/P"},
    {"key": "f3", "tap": "F3", "hold": "Bri-"}, {"key": "f4", "tap": "F4", "hold": "Bri+"},
    {"key": "f5", "tap": "F5", "hold": "Mic"}, {"key": "f6", "tap": "F6", "hold": "Vol-"},
    {"key": "f7", "tap": "F7", "hold": "Vol+"}, {"key": "f8", "tap": "F8", "hold": "MicT"},
    {"key": "f9", "tap": "F9", "hold": "Shot"}, {"key": "f10", "tap": "F10", "hold": "Lock"},
    {"key": "f11", "tap": "F11"}, {"key": "f12", "tap": "F12"},

    {"key": "grv", "tap": "`", "hold": "~"}, {"key": "1", "tap": "1", "hold": "!"}, {"key": "2", "tap": "2", "hold": "@"},
    {"key": "3", "tap": "3", "hold": "#"}, {"key": "4", "tap": "4", "hold": "$"},
    {"key": "5", "tap": "5", "hold": "%"}, {"key": "6", "tap": "6", "hold": "^"},
    {"key": "7", "tap": "7", "hold": "&"}, {"key": "8", "tap": "8", "hold": "*"},
    {"key": "9", "tap": "9", "hold": "("}, {"key": "0", "tap": "0", "hold": ")"},
    {"key": "-", "tap": "-", "hold": "_"}, {"key": "=", "tap": "=", "hold": "+"},
    {"key": "bspc", "tap": "Bksp", "hold": "Del"},

    {"key": "tab", "tap": "Tab"}, {"key": "q", "tap": "Q", "hold": "C-Q"}, {"key": "w", "tap": "W", "hold": "C-W"},
    {"key": "e", "tap": "E"}, {"key": "r", "tap": "R", "hold": "C-R"}, {"key": "t", "tap": "T", "hold": "C-T"},
    {"key": "y", "tap": "Y", "hold": "Home"}, {"key": "u", "tap": "U", "hold": "PgDn"},
    {"key": "i", "tap": "I", "hold": "PgUp"}, {"key": "o", "tap": "O", "hold": "End"}, {"key": "p", "tap": "P"},
    {"key": "[", "tap": "[", "hold": "{"}, {"key": "]", "tap": "]", "hold": "}"}, {"key": "\\", "tap": "\\", "hold": "|"},

    {"key": "caps", "tap": "Esc"}, {"key": "a", "tap": "A", "hold": "C-A"}, {"key": "s", "tap": "S", "hold": "LMet"},
    {"key": "d", "tap": "D", "hold": "LAlt"}, {"key": "f", "tap": "F", "hold": "LCtrl"}, {"key": "g", "tap": "G"},
    {"key": "h", "tap": "H", "hold": "S-`"}, {"key": "j", "tap": "J", "hold": "RCtrl"},
    {"key": "k", "tap": "K", "hold": "RAlt"}, {"key": "l", "tap": "L", "hold": "RMet"},
    {"key": ";", "tap": ";", "hold": ":"}, {"key": "'", "tap": "'", "hold": '"'}, {"key": "ret", "tap": "Enter", "hold": "RAlt"},

    {"key": "lsft", "tap": "Shift"}, {"key": "z", "tap": "Z", "hold": "C-Z"}, {"key": "x", "tap": "X", "hold": "C-X"},
    {"key": "c", "tap": "C", "hold": "C-C"}, {"key": "v", "tap": "V", "hold": "C-V"}, {"key": "b", "tap": "B"},
    {"key": "n", "tap": "N"}, {"key": "m", "tap": "M"},
    {"key": ",", "tap": ",", "hold": "<"}, {"key": ".", "tap": ".", "hold": ">"}, {"key": "/", "tap": "/", "hold": "?"},
    {"key": "rsft", "tap": "Shift"},

    {"key": "lctl", "tap": "LCtrl", "hold": "Layer 4", "active": True}, {"key": "lmet", "tap": "LMeta", "hold": "Layer 2", "active": True},
    {"key": "lalt", "tap": "LAlt"}, {"key": "spc", "tap": "Space", "hold": "Layer 3", "active": True},
    {"key": "ralt", "tap": "RAlt"}, {"key": "rmet", "tap": "RMeta"}, {"key": "rctl", "tap": "RCtrl", "hold": "Layer 5", "active": True},
]

# Layer 2 — Window/Workspace (trigger: hold LMeta)
layer2_keys = [
    {"key": "esc", "tap": "Esc"}, {"key": "f1", "tap": ""}, {"key": "f2", "tap": ""},
    {"key": "f3", "tap": ""}, {"key": "f4", "tap": ""}, {"key": "f5", "tap": ""},
    {"key": "f6", "tap": ""}, {"key": "f7", "tap": ""}, {"key": "f8", "tap": ""},
    {"key": "f9", "tap": ""}, {"key": "f10", "tap": ""}, {"key": "f11", "tap": ""}, {"key": "f12", "tap": "Reload"},

    {"key": "grv", "tap": ""}, {"key": "1", "tap": ""}, {"key": "2", "tap": ""},
    {"key": "3", "tap": ""}, {"key": "4", "tap": ""}, {"key": "5", "tap": ""},
    {"key": "6", "tap": ""}, {"key": "7", "tap": ""}, {"key": "8", "tap": ""},
    {"key": "9", "tap": ""}, {"key": "0", "tap": ""}, {"key": "-", "tap": ""}, {"key": "=", "tap": ""},
    {"key": "bspc", "tap": "Bksp"},

    {"key": "tab", "tap": "Tab"}, {"key": "q", "tap": ""}, {"key": "w", "tap": ""},
    {"key": "e", "tap": ""}, {"key": "r", "tap": ""}, {"key": "t", "tap": ""},
    {"key": "y", "tap": "Tile L", "action": "Win snap"}, {"key": "u", "tap": "Disp L", "action": "Display"},
    {"key": "i", "tap": "Disp R", "action": "Display"}, {"key": "o", "tap": "Tile R", "action": "Win snap"},
    {"key": "p", "tap": "Close", "action": "kitty tab"}, {"key": "[", "tap": "Prev T", "action": "kitty tab"},
    {"key": "]", "tap": "Next T", "action": "kitty tab"}, {"key": "\\", "tap": ""},

    {"key": "caps", "tap": "Esc"}, {"key": "a", "tap": ""}, {"key": "s", "tap": ""},
    {"key": "d", "tap": ""}, {"key": "f", "tap": ""}, {"key": "g", "tap": ""},
    {"key": "h", "tap": "WS ←", "action": "Workspace"}, {"key": "j", "tap": "WS ↓", "action": "Workspace"},
    {"key": "k", "tap": "WS ↑", "action": "Workspace"}, {"key": "l", "tap": "WS →", "action": "Workspace"},
    {"key": ";", "tap": "Scrl L", "action": "kitty"}, {"key": "'", "tap": "Scrl R", "action": "kitty"},
    {"key": "ret", "tap": "Enter"},

    {"key": "lsft", "tap": "Shift"}, {"key": "z", "tap": ""}, {"key": "x", "tap": ""},
    {"key": "c", "tap": ""}, {"key": "v", "tap": ""}, {"key": "b", "tap": ""},
    {"key": "n", "tap": "WS 1", "action": "Workspace"}, {"key": "m", "tap": "WS 2", "action": "Workspace"},
    {"key": ",", "tap": "WS 3", "action": "Workspace"}, {"key": ".", "tap": "WS 4", "action": "Workspace"},
    {"key": "/", "tap": ""}, {"key": "rsft", "tap": "Shift"},

    {"key": "lctl", "tap": ""}, {"key": "lmet", "tap": ""}, {"key": "lalt", "tap": ""},
    {"key": "spc", "tap": ""}, {"key": "ralt", "tap": ""}, {"key": "rmet", "tap": ""}, {"key": "rctl", "tap": ""},
]

# Layer 3 — Symbols (trigger: hold Space)
layer3_keys = [
    {"key": "esc", "tap": "Esc"}, {"key": "f1", "tap": "Mute"}, {"key": "f2", "tap": "P/P"},
    {"key": "f3", "tap": "Bri-"}, {"key": "f4", "tap": "Bri+"}, {"key": "f5", "tap": "Mic"},
    {"key": "f6", "tap": "Vol-"}, {"key": "f7", "tap": "Vol+"}, {"key": "f8", "tap": "MicT"},
    {"key": "f9", "tap": "Shot"}, {"key": "f10", "tap": "Lock"}, {"key": "f11", "tap": ""}, {"key": "f12", "tap": ""},

    {"key": "grv", "tap": ""}, {"key": "1", "tap": ""}, {"key": "2", "tap": ""},
    {"key": "3", "tap": ""}, {"key": "4", "tap": ""}, {"key": "5", "tap": ""},
    {"key": "6", "tap": ""}, {"key": "7", "tap": ""}, {"key": "8", "tap": ""},
    {"key": "9", "tap": ""}, {"key": "0", "tap": ""}, {"key": "-", "tap": ""}, {"key": "=", "tap": ""},
    {"key": "bspc", "tap": "Bksp"},

    {"key": "tab", "tap": "Tab"}, {"key": "q", "tap": "!"}, {"key": "w", "tap": "@"},
    {"key": "e", "tap": "#"}, {"key": "r", "tap": "$"}, {"key": "t", "tap": "%"},
    {"key": "y", "tap": ""}, {"key": "u", "tap": "("}, {"key": "i", "tap": ")"},
    {"key": "o", "tap": "["}, {"key": "p", "tap": "]"}, {"key": "[", "tap": "["}, {"key": "]", "tap": "]"},
    {"key": "\\", "tap": ""},

    {"key": "caps", "tap": "Esc"}, {"key": "a", "tap": "^"}, {"key": "s", "tap": "&"},
    {"key": "d", "tap": "*"}, {"key": "f", "tap": "/"}, {"key": "g", "tap": "`"},
    {"key": "h", "tap": "~"}, {"key": "j", "tap": "|"}, {"key": "k", "tap": ":"},
    {"key": "l", "tap": '"'}, {"key": ";", "tap": ""}, {"key": "'", "tap": ""}, {"key": "ret", "tap": "Enter"},

    {"key": "lsft", "tap": "Shift"}, {"key": "z", "tap": "-"}, {"key": "x", "tap": "_"},
    {"key": "c", "tap": "="}, {"key": "v", "tap": "="}, {"key": "b", "tap": "\\"},
    {"key": "n", "tap": "|"}, {"key": "m", "tap": "<"},
    {"key": ",", "tap": ","}, {"key": ".", "tap": "."}, {"key": "/", "tap": "?"},
    {"key": "rsft", "tap": "Shift"},

    {"key": "lctl", "tap": ""}, {"key": "lmet", "tap": ""}, {"key": "lalt", "tap": ""},
    {"key": "spc", "tap": ""}, {"key": "ralt", "tap": ""}, {"key": "rmet", "tap": ""}, {"key": "rctl", "tap": ""},
]

# Layer 4 — Editing (trigger: hold LCtrl)
layer4_keys = [
    {"key": "esc", "tap": "Esc"}, {"key": "f1", "tap": "Mute"}, {"key": "f2", "tap": "P/P"},
    {"key": "f3", "tap": "Bri-"}, {"key": "f4", "tap": "Bri+"}, {"key": "f5", "tap": "Mic"},
    {"key": "f6", "tap": "Vol-"}, {"key": "f7", "tap": "Vol+"}, {"key": "f8", "tap": "MicT"},
    {"key": "f9", "tap": "Shot"}, {"key": "f10", "tap": "Lock"}, {"key": "f11", "tap": ""}, {"key": "f12", "tap": ""},

    {"key": "grv", "tap": ""}, {"key": "1", "tap": ""}, {"key": "2", "tap": ""},
    {"key": "3", "tap": ""}, {"key": "4", "tap": ""}, {"key": "5", "tap": ""},
    {"key": "6", "tap": ""}, {"key": "7", "tap": ""}, {"key": "8", "tap": ""},
    {"key": "9", "tap": ""}, {"key": "0", "tap": ""}, {"key": "-", "tap": ""}, {"key": "=", "tap": ""},
    {"key": "bspc", "tap": "Bksp"},

    {"key": "tab", "tap": "Tab"}, {"key": "q", "tap": ""}, {"key": "w", "tap": ""},
    {"key": "e", "tap": ""}, {"key": "r", "tap": ""}, {"key": "t", "tap": ""},
    {"key": "y", "tap": "MWhL", "action": "Mouse wheel"}, {"key": "u", "tap": "MWhD", "action": "Mouse wheel"},
    {"key": "i", "tap": "MWhU", "action": "Mouse wheel"}, {"key": "o", "tap": "MWhR", "action": "Mouse wheel"},
    {"key": "p", "tap": "DelBOL", "action": "C-u"}, {"key": "[", "tap": "DelEOL", "action": "C-k"},
    {"key": "]", "tap": ""}, {"key": "\\", "tap": ""},

    {"key": "caps", "tap": "Esc"}, {"key": "a", "tap": ""}, {"key": "s", "tap": ""},
    {"key": "d", "tap": ""}, {"key": "f", "tap": ""}, {"key": "g", "tap": ""},
    {"key": "h", "tap": "←", "action": "Arrow"}, {"key": "j", "tap": "↓", "action": "Arrow"},
    {"key": "k", "tap": "↑", "action": "Arrow"}, {"key": "l", "tap": "→", "action": "Arrow"},
    {"key": ";", "tap": "Bksp"}, {"key": "'", "tap": "Del"}, {"key": "ret", "tap": "Enter"},

    {"key": "lsft", "tap": "Shift"}, {"key": "z", "tap": ""}, {"key": "x", "tap": ""},
    {"key": "c", "tap": ""}, {"key": "v", "tap": ""}, {"key": "b", "tap": ""},
    {"key": "n", "tap": "DWB", "action": "C-Bspc"}, {"key": "m", "tap": "DWF", "action": "C-Del"},
    {"key": ",", "tap": "TWB", "action": "C-w"}, {"key": ".", "tap": "TWF", "action": "A-d"},
    {"key": "/", "tap": ""}, {"key": "rsft", "tap": "Shift"},

    {"key": "lctl", "tap": ""}, {"key": "lmet", "tap": ""}, {"key": "lalt", "tap": ""},
    {"key": "spc", "tap": ""}, {"key": "ralt", "tap": ""}, {"key": "rmet", "tap": ""}, {"key": "rctl", "tap": ""},
]

# Layer 5 — Numbers (trigger: hold RCtrl)
layer5_keys = [
    {"key": "esc", "tap": "Esc"}, {"key": "f1", "tap": "Mute"}, {"key": "f2", "tap": "P/P"},
    {"key": "f3", "tap": "Bri-"}, {"key": "f4", "tap": "Bri+"}, {"key": "f5", "tap": "Mic"},
    {"key": "f6", "tap": "Vol-"}, {"key": "f7", "tap": "Vol+"}, {"key": "f8", "tap": "MicT"},
    {"key": "f9", "tap": "Shot"}, {"key": "f10", "tap": "Lock"}, {"key": "f11", "tap": ""}, {"key": "f12", "tap": ""},

    {"key": "grv", "tap": ""}, {"key": "1", "tap": ""}, {"key": "2", "tap": ""},
    {"key": "3", "tap": ""}, {"key": "4", "tap": ""}, {"key": "5", "tap": ""},
    {"key": "6", "tap": ""}, {"key": "7", "tap": ""}, {"key": "8", "tap": ""},
    {"key": "9", "tap": ""}, {"key": "0", "tap": ""}, {"key": "-", "tap": ""}, {"key": "=", "tap": ""},
    {"key": "bspc", "tap": "Bksp"},

    {"key": "tab", "tap": "Tab"}, {"key": "q", "tap": "+"}, {"key": "w", "tap": "9"},
    {"key": "e", "tap": "8"}, {"key": "r", "tap": "7"}, {"key": "t", "tap": "-"},
    {"key": "y", "tap": ""}, {"key": "u", "tap": ""}, {"key": "i", "tap": ""},
    {"key": "o", "tap": ""}, {"key": "p", "tap": ""}, {"key": "[", "tap": ""}, {"key": "]", "tap": ""},
    {"key": "\\", "tap": ""},

    {"key": "caps", "tap": "Esc"}, {"key": "a", "tap": "/"}, {"key": "s", "tap": "6"},
    {"key": "d", "tap": "5"}, {"key": "f", "tap": "4"}, {"key": "g", "tap": "0"},
    {"key": "h", "tap": ""}, {"key": "j", "tap": ""}, {"key": "k", "tap": ""},
    {"key": "l", "tap": ""}, {"key": ";", "tap": ""}, {"key": "'", "tap": ""}, {"key": "ret", "tap": "Enter"},

    {"key": "lsft", "tap": "Shift"}, {"key": "z", "tap": "="}, {"key": "x", "tap": "3"},
    {"key": "c", "tap": "2"}, {"key": "v", "tap": "1"}, {"key": "b", "tap": ""},
    {"key": "n", "tap": ""}, {"key": "m", "tap": ""},
    {"key": ",", "tap": ""}, {"key": ".", "tap": ""}, {"key": "/", "tap": ""},
    {"key": "rsft", "tap": "Shift"},

    {"key": "lctl", "tap": ""}, {"key": "lmet", "tap": ""}, {"key": "lalt", "tap": ""},
    {"key": "spc", "tap": ""}, {"key": "ralt", "tap": ""}, {"key": "rmet", "tap": ""}, {"key": "rctl", "tap": ""},
]


def generate_all():
    layers = [
        ("layer1_base.svg", "Layer 1 — Base", "Default typing with tap-hold modifiers", layer1_keys, {"lctl", "lmet", "spc", "rctl"}),
        ("layer2_window.svg", "Layer 2 — Window/Workspace", "Hold Left Meta (S key) to activate", layer2_keys, set()),
        ("layer3_symbols.svg", "Layer 3 — Symbols", "Hold Spacebar to activate", layer3_keys, set()),
        ("layer4_editing.svg", "Layer 4 — Editing", "Hold Left Ctrl to activate", layer4_keys, set()),
        ("layer5_numbers.svg", "Layer 5 — Numbers", "Hold Right Ctrl to activate", layer5_keys, set()),
    ]

    for filename, title, subtitle, keys, active in layers:
        svg = draw_keyboard(keys, title, subtitle, active)
        path = os.path.join(OUTDIR, filename)
        with open(path, "w") as f:
            f.write(svg)
        print(f"Generated: {path}")


if __name__ == "__main__":
    generate_all()
