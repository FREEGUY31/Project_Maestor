import sqlite3
import numpy as np

def init_db():
    conn = sqlite3.connect('data/maester.db')
    cursor = conn.cursor()
    # History is stored as text, Face_Vector is stored as a BLOB (binary data)
    cursor.execute('''CREATE TABLE IF NOT EXISTS patients 
                   (id INTEGER PRIMARY KEY, name TEXT, history TEXT, face_vector BLOB)''')
    conn.commit()
    conn.close()

def save_patient(name, history, vector):
    conn = sqlite3.connect('data/maester.db')
    # Convert numpy array vector to binary for storage
    conn.execute("INSERT INTO patients (name, history, face_vector) VALUES (?, ?, ?)", 
                 (name, history, vector.tobytes()))
    conn.commit()
    conn.close()