import cv2
import numpy as np
import time
from modules.database import init_db
from modules.biometrics import identify_patient
from modules.sensor import get_live_vitals
from modules.intelligence import emergency_predictor

# Initialize Project Maester
init_db()
video_capture = cv2.VideoCapture(0)
vitals_history = []  # Buffer for the last 10 readings for LSTM prediction

print("--- Project Maester Active ---")
print("Press 'i' to Identify Patient | Press 'q' to Quit")

while True:
    ret, frame = video_capture.read()
    if not ret:
        break

    # 1. Fetch Real-time Vitals (Big Data Pipeline Simulation)
    vitals = get_live_vitals()
    hr, spo2 = vitals['hr'], vitals['spo2']
    
    # 2. AI Intelligence: Update Risk Prediction
    vitals_history.append([hr, spo2])
    risk_score = 0.0
    
    if len(vitals_history) > 10:
        vitals_history.pop(0)
        # Prepare sequence for TensorFlow LSTM model
        input_data = np.array([vitals_history])
        prediction = emergency_predictor.predict(input_data, verbose=0)
        risk_score = prediction[0][0]

    # 3. Visual Interface & Triage Logic
    # Red background for crisis, Green for stable
    color = (0, 0, 255) if risk_score > 0.8 or hr > 150 or spo2 < 90 else (0, 255, 0)
    
    # Overlay Vitals
    cv2.putText(frame, f"HR: {hr} BPM | SpO2: {spo2}%", (10, 30), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)
    
    # Overlay AI Risk Assessment
    risk_text = "CRITICAL RISK" if risk_score > 0.8 else "STABLE"
    cv2.putText(frame, f"AI Assessment: {risk_text} ({risk_score:.2f})", (10, 60), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)

    # 4. Biometric Identification Trigger
    key = cv2.waitKey(1) & 0xFF
    if key == ord('i'):
        name, history = identify_patient(frame)
        print(f"\n[ALERT] Patient Identified: {name}")
        print(f"[DATA] Medical History: {history}")
        
        # Display history on screen temporarily
        cv2.putText(frame, f"ID: {name}", (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
        cv2.putText(frame, f"HX: {history}", (10, 130), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)

    # Show the Live Feed
    cv2.imshow('Project Maester - Emergency Response Interface', frame)

    if key == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()