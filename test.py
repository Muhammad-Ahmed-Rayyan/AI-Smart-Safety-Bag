import cv2
import mediapipe as mp
import numpy as np
import requests
import time
import base64
import serial
import threading

# === CONFIGURATION ===
IFTTT_EVENT_NAME = 'intruder_alert'
IFTTT_KEY = 'gdDP02XhlL5kBCDmLbhBE7uAyU1CUP7BFzmqB-oaAXE' # Replace with your IFTTT key
IMGBB_API_KEY = '9413a699b8f32429a8db44299575f462' # Replace with your IMGBB API key
ARDUINO_PORT = 'COM4'  # Change this if needed
BAUD_RATE = 9600

IFTTT_URL = f'https://maker.ifttt.com/trigger/{IFTTT_EVENT_NAME}/with/key/{IFTTT_KEY}'

# === GLOBAL VARIABLES ===
latest_gps_data = "No GPS data yet."
latest_tilt_status = "No tilt detected."

# === FUNCTIONS ===
def upload_to_imgbb(image_path):
    with open(image_path, "rb") as file:
        encoded_image = base64.b64encode(file.read())
    response = requests.post(
        "https://api.imgbb.com/1/upload",
        data={
            "key": IMGBB_API_KEY,
            "image": encoded_image,
            "name": f"intruder_{int(time.time())}"
        }
    )
    result = response.json()
    return result["data"]["url"] if "data" in result else None

def send_ifttt_notification(image_url, gps_data):
    try:
        payload = {
            "value1": "🚨 Intruder Detected!",
            "value2": image_url,
            "value3": f"{gps_data}\n{latest_tilt_status}"
        }
        requests.post(IFTTT_URL, json=payload)
        print("🚨 IFTTT notification sent with image, GPS, and tilt info.")
    except Exception as e:
        print("Failed to send IFTTT notification:", e)

def read_serial():
    global latest_gps_data, latest_tilt_status
    try:
        ser = serial.Serial(ARDUINO_PORT, BAUD_RATE, timeout=1)
    except serial.SerialException as e:
        print(f"❌ Could not open {ARDUINO_PORT}: {e}")
        return

    while True:
        line = ser.readline().decode('utf-8', errors='ignore').strip()
        if line.startswith("GPS:"):
            gps_raw = line[4:]
            latest_gps_data = gps_raw
            print("🔄 GPS Updated:", gps_raw)
        elif line == "TILT":
            latest_tilt_status = "⚠️ Motion Detected!"
            print("⚠️ Tilt detected.")

# Start reading serial in background thread
threading.Thread(target=read_serial, daemon=True).start()

# === COOLDOWN SETTINGS ===
last_alert_time = 0
ALERT_COOLDOWN = 10  # seconds

# === Load Reference Image ===
reference_img = cv2.imread(r'C:\Users\Desktop\PROJ\image.jpg') # Replace with your image path of user 
reference_img = cv2.resize(reference_img, (100, 100))
reference_img = cv2.cvtColor(reference_img, cv2.COLOR_BGR2GRAY)

# === Face Detection Setup ===
mp_face_detection = mp.solutions.face_detection
cap = cv2.VideoCapture(0)

with mp_face_detection.FaceDetection(model_selection=0, min_detection_confidence=0.6) as face_detection:
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = face_detection.process(rgb_frame)

        label = "No Face"

        if results.detections:
            for detection in results.detections:
                bbox = detection.location_data.relative_bounding_box
                h, w, _ = frame.shape
                x = int(bbox.xmin * w)
                y = int(bbox.ymin * h)
                w_box = int(bbox.width * w)
                h_box = int(bbox.height * h)

                if x < 0 or y < 0 or x + w_box > w or y + h_box > h:
                    continue

                face_roi = frame[y:y + h_box, x:x + w_box]

                try:
                    face_resized = cv2.resize(face_roi, (100, 100))
                    face_gray = cv2.cvtColor(face_resized, cv2.COLOR_BGR2GRAY)
                    cv2.imshow("Cropped Face", face_gray)

                    result = cv2.matchTemplate(face_gray, reference_img, cv2.TM_CCOEFF_NORMED)
                    similarity = result[0][0]
                    print(f"Similarity: {similarity:.2f}")

                    if similarity > 0.45:
                        label = "Recognized"
                        color = (0, 255, 0)
                    else:
                        label = "Not Recognized"
                        color = (0, 0, 255)

                        current_time = time.time()
                        if current_time - last_alert_time > ALERT_COOLDOWN:
                            image_path = "intruder.jpg"
                            cv2.imwrite(image_path, face_roi)

                            print("Uploading to imgbb...")
                            image_url = upload_to_imgbb(image_path)
                            if image_url:
                                send_ifttt_notification(image_url, latest_gps_data)
                            else:
                                print("Failed to upload image to imgbb.")

                            last_alert_time = current_time

                    cv2.rectangle(frame, (x, y), (x + w_box, y + h_box), color, 2)
                    cv2.putText(frame, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)

                except Exception as e:
                    print(f"Error processing face: {e}")
                    continue

        cv2.imshow("Smart Bag Intruder Detection", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
