from flask import Flask, jsonify
import random
import time

app = Flask(__name__)

@app.route("/home")
def home():
    return "Smart Helmet Backend Running (Flask)"

@app.route("/sensor-data")
def sensor_data():
    # Simulated eye blink sensor
    # 0 = eyes closed, 1 = eyes open
    eye_state = random.choice([0, 1])

    # Simulated MPU6050 values
    ax = random.randint(-20000, 20000)
    ay = random.randint(-20000, 20000)

    # Head tilt logic
    head_tilt = False
    if abs(ax) > 16000 or abs(ay) > 16000:
        head_tilt = True

    # Fatigue detection logic
    if eye_state == 0 and head_tilt:
        status = "Fatigue Detected"
    else:
        status = "Normal Condition"

    return jsonify({
        "eye_state": eye_state,
        "ax": ax,
        "ay": ay,
        "head_tilt": head_tilt,
        "status": status
    })

if __name__ == "__main__":
    app.run(debug=True)