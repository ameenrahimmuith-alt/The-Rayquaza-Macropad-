"""boot.py for XIAO RP2040 - runs once at power-up before main.py.

Disables the auto-reload-on-write feature so that touching files on the CIRCUITPY
drive while the macropad is plugged in doesn't immediately reset the keyboard.
"""
import supervisor
supervisor.disable_autoreload()
