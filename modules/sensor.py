import random
import time

def get_live_vitals():
    # Simulating a normal heart rate (60-100) and SpO2 (95-100)
    # Occasionally, we will simulate a "Crisis" (e.g., HR > 150 or SpO2 < 90)
    hr = random.randint(60, 110)
    spo2 = random.randint(94, 99)
    
    # 5% chance of simulating a medical emergency
    if random.random() < 0.05:
        hr = random.randint(160, 200) # Tachycardia
        spo2 = random.randint(80, 88)  # Hypoxia
        
    return {"hr": hr, "spo2": spo2}