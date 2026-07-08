# Hardware Pinout Configuration

This document outlines the physical wiring connections between the Raspberry Pi Zero 2 W, the I2S Audio Amplifier (MAX98357A), and the I2S Microphone (INMP441).

note: some wires can be pluged in various pins and do same thing for example:
if you want a 5V u can go for pin2 or pin4 yet get the same output.

## Connection Table

| Component | Component Pin | Raspberry Pi Pin Name | Physical Pin Number |
| :--- | :--- | :--- | :--- |
| **MAX98357A Amp** | Vin | 5V Power | Pin 2 or 4 |
| **MAX98357A Amp** | GND | Ground | Pin 6 or 9 |
| **MAX98357A Amp** | BCLK | GPIO 18 (PCM_CLK) | Pin 12 |
| **MAX98357A Amp** | LRCK | GPIO 19 (PCM_FS) | Pin 35 |
| **MAX98357A Amp** | DIN | GPIO 21 (PCM_DOUT) | Pin 40 |
| | | | |
| **INMP441 Mic** | VDD | 3.3V Power | Pin 1 or 17 |
| **INMP441 Mic** | GND | Ground | Pin 14 |
| **INMP441 Mic** | SCK | GPIO 18 (PCM_CLK) | Pin 12 |
| **INMP441 Mic** | WS | GPIO 19 (PCM_FS) | Pin 35 |
| **INMP441 Mic** | DOUT | GPIO 20 (PCM_DIN) | Pin 38 |
| **INMP441 Mic** | L/R | Ground (Left Channel) | Connected to GND |

Note: you need a breadboard, for GPIO 19 (pin 35) and GPIO 18 (PIN 12).