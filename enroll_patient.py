import cv2
import face_recognition
import numpy as np
from modules.database import save_patient, init_db

def enroll():
    # Ensure the database exists
    init_db()
    
    name = input("Enter Patient Name: ")
    history = input("Enter Medical History (e.g., Allergies, Blood Group): ")
    
    print("Opening camera... Look at the lens and press 's' to capture.")
    cam = cv2.VideoCapture(0)
    
    while True:
        ret, frame = cam.read()
        cv2.imshow("Enrollment - Press 's' to save", frame)
        
        if cv2.waitKey(1) & 0xFF == ord('s'):
            
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            
            
            encodings = face_recognition.face_encodings(rgb_frame)
            
            if len(encodings) > 0:
                
                save_patient(name, history, encodings[0])
                print(f"Success: {name} has been enrolled in Project Maester.")
                break
            else:
                print("No face detected. Please try again.")
        
        elif cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    enroll()
