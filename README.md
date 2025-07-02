<div align="center">

# 🎒 AI Smart Safety Bag

[![Python](https://img.shields.io/badge/Python-3.10-blue)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux-green)](#)
[![Last Commit](https://img.shields.io/github/last-commit/Muhammad-Ahmed-Rayyan/AI-Smart-Safety-Bag)](https://github.com/Muhammad-Ahmed-Rayyan/AI-Smart-Safety-Bag/commits/main)
[![License](https://img.shields.io/badge/License-MIT-lightgrey)](#)

</div>

---

## 🚀 Overview

This is an **AI-powered Smart Safety Bag system** designed to improve personal security using:

- **Arduino + GPS + Tilt sensor** for motion and location tracking  
- **Python + OpenCV + Mediapipe** for intruder face detection  
- **IFTTT & Imgbb** for sending real-time intrusion alerts with image & GPS data to your phone

Perfect for students, travelers, or anyone wanting extra security for their belongings.

---

## 🔧 How It Works

- 📡 **Arduino** continuously reads tilt sensor & GPS data and sends to your PC via serial.
- 🎥 **Python script** uses your webcam to detect faces.
- 🧠 Compares faces with a stored image (the authorized user).
- 🚨 If an unrecognized person tries to access, it:
    - Captures an image.
    - Uploads it to **Imgbb**.
    - Sends an alert via **IFTTT** (push notification/email/SMS) with image + GPS location.
- 💾 Updates continuously with latest GPS coordinates and motion status.

---

## 🛠 Hardware Setup

### ⚙ Arduino Connections (GPS + Tilt)

| Arduino Pin | Connected Component |
| ----------- | ------------------- |
| D2          | Tilt sensor OUT     |
| D3 (TX)     | GPS RX              |
| D4 (RX)     | GPS TX              |
| 5V          | GPS VCC, Tilt VCC   |
| GND         | GPS GND, Tilt GND   |

- The Arduino code is in [`arduino.txt`](arduino.txt).  
  👉 Copy it into Arduino IDE, upload to your Arduino Uno.

---

## 🖥 Software Requirements

- Python **3.10** (important: Mediapipe may break on other versions)
- Arduino IDE for uploading code
- Webcam must be connected to your laptop for Python detection

---

## 📥 Installation

### 🔗 Clone & Install Python Libraries
```bash
git clone https://github.com/Muhammad-Ahmed-Rayyan/AI-Smart-Safety-Bag.git
cd AI-Smart-Safety-Bag

pip install -r requirements.txt
