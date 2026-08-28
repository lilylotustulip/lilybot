# 🤖 LilyBot

[![MIT License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen)]()
[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org/downloads/)

> A privacy-first, offline AI voice assistant running on a Raspberry Pi Zero 2 W — proving that intelligent edge computing doesn't require cloud dependency or massive energy consumption.

## 🎯 The Mission

LilyBot solves three critical problems:

1. **🔐 Privacy** — Your data never leaves your device. No cloud uploads, no tracking.
2. **⚡ Efficiency** — Runs on a $50 Raspberry Pi Zero 2 W with minimal power consumption.
3. **🚀 Accessibility** — No subscription fees, no locked-in ecosystems. True local AI.

---

## 📸 Project Showcase

**Live Presentation:** [Watch LilyBot in action](https://youtu.be/5iiit7Okda8?si=iOipWRsYhxOSS8oy)

### Handcrafted Design
Built the chassis from air-dry clay with a naturalistic, rocky texture for an aesthetically unique desk assistant.

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| **Hardware** | Raspberry Pi Zero 2 W |
| **Microphone** | INMP441 I2S Microphone |
| **Speaker/Amp** | Audio amplifier module |
| **Language** | Python 3.9+ |
| **AI Framework** | Edge-based ML models |
| **Key Learning** | Hardware integration, audio processing, embedded systems |

---

## 📋 Hardware Components

For detailed component specifications and pinout information, see [Hardware Inventory](hardware/components/inventory.md).

**Main Components:**
- Raspberry Pi Zero 2 W (main processor)
- INMP441 I2S Microphone (audio input)
- Audio Amplifier Module (speaker output)
- Clay enclosure (custom, handcrafted)

---

## 🏗️ Project Structure

```
lilybot/
├── code/                   # code
├── hardware/              # Hardware schematics & docs
│   └── components/
│      └── inventory.md
|      └── pinouts.md
     └── wiring.md
├── docs/
│   └── journal.md         # Development journal & troubleshooting
├── README.md              # This file
└── LICENSE                # MIT License
```

---

## 📖 Development Journey

### Challenges Overcome

**Hardware Integration:**
- 🔌 **Soldering Issue**: Accidentally bridged two pins while soldering the INMP441 microphone, causing potential short circuit → had to replace the unit
- 🔗 **Pin Conflict**: Both audio amplifier and microphone needed the same GPIO pin, solved by DIY pin-splicing (cutting and rewiring)
- 🔥 **Thermal Issues**: Troubleshooting revealed burning plastic smell from microphone → identified and fixed via hardware journal

**Key Lessons Learned:**
- GPIO pin planning is critical in hardware projects
- Solid documentation of problems prevents repeated mistakes
- Edge AI on resource-constrained devices is possible with proper optimization

### Journey Documentation
For detailed day-by-day progress, debugging steps, and solutions, see [Development Journal](docs/journal.md) — includes logs from day one.

---

## ⚡ Quick Start

### Prerequisites
- Raspberry Pi Zero 2 W
- MicroSD card (16GB recommended)
- Power supply
- Soldering iron & basic electronics knowledge

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/lilylotustulip/lilybot.git
   cd lilybot
   ```

2. **Set up hardware**
   - Follow the pinout diagram in [Hardware Inventory](hardware/components/inventory.md)
   - Connect microphone and amplifier to designated GPIO pins
   - Mount in clay enclosure (optional)

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure audio settings**
   ```bash
   # Test microphone and speaker
   arecord -D hw:0 test.wav  # Record 5 seconds
   aplay test.wav            # Playback test
   ```

5. **Run LilyBot**
   ```bash
   python src/lilybot.py
   ```

---

## 🎤 How It Works

1. **Audio Input** → INMP441 microphone captures speech
2. **Processing** → Edge AI model processes audio locally
3. **Response Generation** → LLM generates reply (all on-device)
4. **Audio Output** → Speaker plays response

**All processing happens locally — no internet required.**

---

## 🌟 Key Features

| Feature | Details |
|---------|---------|
| **100% Offline** | No cloud dependency, no data transmission |
| **Low Power** | Runs on Raspberry Pi Zero 2 W (~5W average) |
| **Voice I/O** | Natural voice input and speech synthesis |
| **Privacy Focused** | Your conversations stay on your device |
| **Customizable** | Modify prompts, behavior, and responses |
| **Open Source** | Full transparency into how it works |

---

## 🔧 Configuration

### Audio Settings
Edit `config.yaml` to adjust:
- Microphone sensitivity
- Speaker volume
- Audio input/output device selection

### AI Model
Choose between lightweight models optimized for edge devices (see `docs/models.md`)

### Customization
Modify system prompts in `src/prompts/` to change personality and response style

---

## 🐛 Troubleshooting

### Microphone Not Working
1. Check GPIO pin connections (see hardware inventory)
2. Verify I2S driver is loaded: `lsmod | grep i2s`
3. Test with: `arecord -D hw:0 test.wav`
4. See [Development Journal](docs/journal.md) for common issues

### No Audio Output
1. Verify amplifier power connection
2. Test speaker separately: `speaker-test -t sine -f 1000 -l 5`
3. Check audio device: `aplay -l`

### High Latency
1. Reduce model size (trades accuracy for speed)
2. Enable GPU acceleration if available
3. Profile with: `python -m cProfile src/lilybot.py`

See [Journal](docs/journal.md) for more troubleshooting tips.

---

## 📚 Learning Resources

- [Raspberry Pi GPIO Guide](https://www.raspberrypi.org/documentation/usage/gpio/)
- [I2S Audio on Raspberry Pi](https://learn.adafruit.com/adafruit-i2s-stereo-decoder-uda1334a)


---

## 🤝 Contributing

Want to improve LilyBot? Contributions welcome!

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/better-recognition`)
3. Document your changes
4. Submit a Pull Request

---

## ⚠️ Limitations

- Model size limited by Raspberry Pi RAM 
- Inference speed slower than cloud services 
- Requires manual setup (not plug-and-play)

---

## 📝 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **Inspired by**: Privacy-first computing, IoT innovation, and the open-source community
- **Built with**: Raspberry Pi OS, python

---

## 📞 Support & Feedback

- 📖 Check [Development Journal](docs/journal.md) first
- 🐛 Found a bug? Open an [Issue](https://github.com/lilylotustulip/lilybot/issues)
- 💡 Have an idea? Start a [Discussion](https://github.com/lilylotustulip/lilybot/discussions)
- 📸 Want to showcase your build? Share in Discussions!

---

**LilyBot: Big Intelligence on small hardware** 🌱🤖
