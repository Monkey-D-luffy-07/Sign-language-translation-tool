# Install necessary packages
!pip install opencv-python opencv-python-headless

import cv2
import numpy as np
from google.colab import files

# Upload video file
uploaded = files.upload()

# Get the uploaded file name
video_file = list(uploaded.keys())[0]

# Function to detect hands using color segmentation
def detect_hand(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_skin = np.array([0, 20, 70], dtype=np.uint8)
    upper_skin = np.array([20, 255, 255], dtype=np.uint8)
    mask = cv2.inRange(hsv, lower_skin, upper_skin)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return contours, mask

# Function to classify simple gestures
def classify_gesture(contour):
    hull = cv2.convexHull(contour)
    defects = cv2.convexityDefects(contour, cv2.convexHull(contour, returnPoints=False))
    if defects is not None:
        defect_count = len(defects)
        if defect_count == 0:
            return "Fist"
        else:
            return "Open Hand"
    else:
        return "Unknown"

# Map gestures to phrases
def gesture_to_text(gesture):
    gesture_dict = {
        "Fist": "Hello",
        "Open Hand": "Thank You",
    }
    return gesture_dict.get(gesture, "Unknown Gesture")

# Open video
cap = cv2.VideoCapture(video_file)

if not cap.isOpened():
    print("Error: Could not open video.")
else:
    recognized_gestures = []
    last_gesture = None

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        contours, _ = detect_hand(frame)

        for contour in contours:
            if cv2.contourArea(contour) > 500:
                gesture = classify_gesture(contour)
                gesture_text = gesture_to_text(gesture)

                # Only add if different from the last one
                if gesture_text != last_gesture:
                    recognized_gestures.append(gesture_text)
                    last_gesture = gesture_text

    cap.release()

# Print recognized gestures only once per type
output_text = ' '.join(recognized_gestures)
print("\n\nRecognized Sign Language:", output_text)
