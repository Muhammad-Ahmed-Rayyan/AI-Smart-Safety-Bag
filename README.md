<div align="center">

# 🎒 AI Smart Safety Bag

[![Last Commit](https://img.shields.io/github/last-commit/Muhammad-Ahmed-Rayyan/AI-Smart-Safety-Bag)](https://github.com/Muhammad-Ahmed-Rayyan/AI-Smart-Safety-Bag/commits/main)
[![Python](https://img.shields.io/badge/Python-3.10-blue)](https://www.python.org/)
![languages](https://img.shields.io/github/languages/count/Muhammad-Ahmed-Rayyan/AI-Hotel-Management-System)

<br>

Built with the tools and technologies:  
![Arduino](https://img.shields.io/badge/Arduino-00979D?style=for-the-badge&logo=arduino&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)
![Mediapipe](https://img.shields.io/badge/MediaPipe-FF6F00?style=for-the-badge&logo=google&logoColor=white)

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
```

## 🔑 API Setup

You'll need to create accounts and get API keys for:
- **IFTTT Webhooks** – to send intrusion notifications (get your key from the IFTTT Webhooks service).
- **Imgbb** – to upload images and get public image URLs.

Update `IFTTT_KEY` and `IMGBB_API_KEY` in your `test.py` script accordingly.

---

## ⚙️ Run the Project

Make sure your Arduino is connected via USB, webcam is ready, and the Arduino code is already uploaded.

Then simply run:

```bash
python test.py
```

---

## 📷 Image Matching

Place your authorized person’s face image at the path specified in test.py.

```bash
reference_img = cv2.imread(r'C:\Users\Desktop\PROJ\image.jpg')
```

Replace this with your own absolute path.

---

## 🌐 Notifications & Hosting

- Uses Imgbb API to upload intruder images.
- Uses IFTTT webhook to push real-time alerts with image + GPS data to your device.

---

## ⚡ Highlights
- Detects unauthorized opening / motion
- Reads live GPS location via NEO-6M module
- Sends alerts with:
   - Intruder snapshot
   -  Latest GPS data
   -   Tilt detection status
- Cooldown system to prevent spam notifications

---
