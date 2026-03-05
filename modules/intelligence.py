import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import LSTM, Dense

def build_anomaly_model():
    # Constructing the LSTM architecture for time-series vitals
    model = Sequential([
        # input_shape=(time_steps, features) -> 10 seconds of HR and SpO2
        LSTM(32, input_shape=(10, 2), return_sequences=False),
        Dense(16, activation='relu'),
        # Output: Probability of a medical crisis (0 to 1)
        Dense(1, activation='sigmoid')
    ])
    
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model

# Initialize the global predictor for main.py
emergency_predictor = build_anomaly_model()