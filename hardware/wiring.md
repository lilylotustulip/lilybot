# Wiring

in this file i will be tracking the wiring process of my components, leaving some notes for a better understanding.

# System Foundation: Raspberry Pi Zero 2 W

**elements**: the elements needed to power on the raspberry pi zero are:
- 16 GB class 10 microSD card
- Samsung EP-TA200 Adaptive fast charger & Micro-USB Data & Power cable.

### steps:
- get the microSD card in the the microSD adapter to plug it in the device
- get the Rapberry Pi imager software on your device.
- follow the instructions (for the OS i used Rapberry Pi OS Lite (64-bit)), dont forget to enable SSH.
- plug the microSD in the raspberry Pi to make its first boot
- connect it, using the SSH command.

# Hardware interface & Protocols
- solder the components first.
- study the components and their pinouts.
- optional but i used a color code for the wires to keep things clear. for example: black for GND. (later the colors werent enough and i added more colors to the color code)
- plug the wires in the corresponding pinouts. [pinouts]()
- edit the `/boot/firmware/config.txt` this command changes based on the version of the Pi.
- reboot and test.
"in the case of lilybot the audio amplifier and microphone both had to be plugged in the GPIO 19 (pin 35). so i got a breadboard for a more organized and a safest way"

