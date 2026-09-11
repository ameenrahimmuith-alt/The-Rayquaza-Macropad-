# Firmware

This hackpad runs on **KMK** (CircuitPython). The sources live in [`KMK/`](KMK/):

- [`KMK/main.py`](KMK/main.py) — 4×3 matrix + EC11 encoder + OLED setup, 3 keymap layers
- [`KMK/code.py`](KMK/code.py) — CircuitPython entry point (imports `main`)
- [`KMK/boot.py`](KMK/boot.py) — disables CIRCUITPY auto-reload while plugged in

## Flashing

1. Download **CircuitPython for Seeed XIAO RP2040** from
   <https://circuitpython.org/board/seeeduino_xiao_rp2040/> (the `.uf2`).
2. Double-tap the XIAO BOOT button to enter bootloader mode (a `RPI-RP2`
   drive mounts). Drag the `.uf2` onto it. The XIAO reboots into
   CircuitPython and a `CIRCUITPY` drive appears.
3. Download the latest [KMK firmware](https://github.com/KMKfw/kmk_firmware)
   release zip. Copy the `kmk/` folder from the zip onto `CIRCUITPY`.
4. Copy `main.py`, `code.py`, and `boot.py` from this folder onto
   `CIRCUITPY`.
5. Done. The macropad starts working immediately.

## Default keymap (3 layers, 12 keys per layer)

Layer layout (matrix index = row × 4 + col):

| Row | Col 0 | Col 1 | Col 2 | Col 3 |
|---|---|---|---|---|
| 0 (top)    | SW1  | SW2  | SW3  | SW4  |
| 1 (middle) | SW5  | SW6  | SW7  | SW8  |
| 2 (bottom) | SW9  | SW10 | SW11 | SW12 |

### Layer 0 — Default (letters)

| | | | |
|---|---|---|---|
| A | B | C | D |
| E | F | G | H |
| I | J | K | **MO(1)** (hold for L1) |

Encoder: turn = volume +/−, push: unwired.

### Layer 1 — Media

| | | | |
|---|---|---|---|
| Mute | Play/Pause | Next | Prev |
| Vol+ | Vol−  | — | — |
| — | — | **MO(2)** (hold for L2) | — (passthrough) |

Encoder: turn = next/prev track.

### Layer 2 — Numpad

| | | | |
|---|---|---|---|
| 7 | 8 | 9 | + |
| 4 | 5 | 6 | − |
| 1 | 2 | 3 | — (passthrough) |

Encoder: turn = numpad + / −.

Edit `keyboard.keymap` and `encoder_handler.map` in [`KMK/main.py`](KMK/main.py)
to change.
