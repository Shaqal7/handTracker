import cv2
import mediapipe as mp
import numpy as np
import win32gui
import win32con

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)


def find_landmark_distance(landmarks, idx1, idx2):
    x1, y1 = landmarks[idx1].x, landmarks[idx1].y
    x2, y2 = landmarks[idx2].x, landmarks[idx2].y
    return np.linalg.norm(np.array([x1, y1]) - np.array([x2, y2]))


def minimize_window():
    # Get handle of currently active window
    hwnd_active = win32gui.GetForegroundWindow()
    win32gui.ShowWindow(hwnd_active, win32con.SW_MINIMIZE)


while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        continue

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Define landmarks for finger tips and index+mcp as palm center
            thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
            forefinger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            palm_center = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP]

            # Measure distance between tips and palm
            distance_thumb = find_landmark_distance(hand_landmarks.landmark, mp_hands.HandLandmark.THUMB_TIP,
                                                    mp_hands.HandLandmark.INDEX_FINGER_MCP)
            distance_forefinger = find_landmark_distance(hand_landmarks.landmark,
                                                         mp_hands.HandLandmark.INDEX_FINGER_TIP,
                                                         mp_hands.HandLandmark.INDEX_FINGER_MCP)

            # Clenching is defined as both tips being nearly at the same point (distance minima)
            if distance_thumb < 0.05 and distance_forefinger < 0.05:
                minimize_window()

    cv2.imshow('Hand Tracking', frame)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()