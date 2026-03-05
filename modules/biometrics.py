import face_recognition
import cv2
import sqlite3
import numpy as np

def identify_patient(frame):
    # Find all faces in the current frame [cite: 17, 19]
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    conn = sqlite3.connect('data/maester.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name, history, face_vector FROM patients")
    
    for (name, history, vector_blob) in cursor.fetchall():
        stored_vector = np.frombuffer(vector_blob) # Convert back to array [cite: 23]
        
        # Compare live face to stored record [cite: 17, 20]
        matches = face_recognition.compare_faces([stored_vector], face_encodings[0])
        if matches[0]:
            return name, history
            
    return "Unknown", "No history found."