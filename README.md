# Rasperry Pi Pico Scripts

Repository of scripts (in MicroPython) to be run on the Rasperry Pi Pico
micro-controller board.

Installed version is the "Pimoroni" MicroPython  including libraries for their
add-on boards (using the v0.0.5 Alpha release currently).

Using Thonny IDE to write/flash the Pico. Using MicroPython the Pico will
launch `main.py` when powered up, so write code to that file on the Pico if
the intention is to use it away from a development environment.  

* `keypad_timer.py`: hit any key on the (Pimoroni) Pico Keypad to start a timer;
  each button will flash for a minute to show a visual countdown
