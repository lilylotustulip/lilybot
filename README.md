# Lilybot

## LilyBot: Edge-based AI assistant

Lilybot is a custom AI assistant, born out of desire to solve 3 main problems: **Privacy**, **accessibility** and **effeciency**.
my mission is to prove that high-performance intelligence can exist without cloud dependency or massive energy consumption. and to make that work i decided to choose edge-based AI, using a Raspberry Pi Zero 2 W (512 MB of LPDDR2 SDRAM), and the I2S audio protocols to ensure high quality, local processing, that is accessible anywhere, regardless of the internet connection.

## The Journey
As a beginner i faced many problems during the process.
for instance, hardware problems:
when soldering the INMP441 I2S microphone.
i accidently linked two pins together, which maybe would have caused a short circuit. so i had to buy a new one.

"for more information about the components visit the [hardware inventory](hardware/components/inventory.md)"

an other example is when i had to link both the audio amplifier and the microphone to one pin of the raspberry and i didn't have a breadboard yet so i decided to do the "splice" (cutting one edge of each jumper wire of the componenets (audio aumplifier, microphone and raspberry) and assembling the raw edges together and tape them with an electrical tape).
eventually the audio amplifier did work, but the microphone didn't no matter what i tried, after few minutes of trying to troubleshoot the microphone, i smelled sort of burning plastic and some noise comming from the audio amplifier. i then had to stop everything and start planning the troubleshooting.

"to know how managed to fixed it check out the [journal](docs/journal.md)"