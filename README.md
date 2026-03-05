🛡️ Project Maester: AI-Driven Emergency Response System
Project Maester is an end-to-end medical response pipeline designed to eliminate data bottlenecks in emergency medicine. It integrates Computer Vision, High-Velocity Data Streaming, and Deep Learning to bridge the gap between an unidentified casualty and a stabilized patient.

🚀 Key Features
Biometric Identification: Utilizes PyTorch and OpenCV to instantly identify patients via facial recognition and retrieve their encrypted medical histories (Allergies, Blood Group, etc.).

Predictive Health Monitoring: Employs a TensorFlow-based LSTM (Long Short-Term Memory) model to analyze time-series vital signs (Heart Rate, SpO2) and predict medical crises before they occur.

Real-time Big Data Pipeline: Engineered to ingest and process high-velocity sensor streams with sub-second latency for immediate visual triage.

Secure Persistence: Implements a modular SQLite3 database to manage patient records and biometric embeddings.

🛠️ Technical Stack
Languages: Python (v3.13).

Frameworks: TensorFlow (Keras), PyTorch.

Computer Vision: OpenCV, Face-Recognition.

Data Science: NumPy, Time-series Anomaly Detection.

Database: SQLite3.

📂 Project Structure
Bash
Project_Maester/
├── data/               # Persistent SQLite storage
├── modules/            # Backend logic modules
│   ├── biometrics.py   # Facial recognition logic
│   ├── database.py     # SQL queries & persistence
│   ├── intelligence.py # LSTM model architecture
│   └── sensor.py       # Real-time vital sign simulator
├── main.py             # Central orchestration & UI
├── enroll_patient.py   # Secure patient onboarding
└── requirements.txt    # Dependency manifest
🏁 Installation & Usage
Clone the Repo:
git clone https://github.com/FREEGUY31/Project_Maestor.git

Install Dependencies:
pip install -r requirements.txt

Enroll a Patient:
Run python enroll_patient.py to capture a face and medical history.

Launch the System:
Execute python main.py. Press 'i' to identify a patient and trigger the AI risk assessment.
