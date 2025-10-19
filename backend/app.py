# backend/app.py
from flask import Flask
from flask_socketio import SocketIO, emit
import time
import threading
from flask import make_response, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}}) 

app.config['SECRET_KEY'] = 'devsecret'
socketio = SocketIO(app, cors_allowed_origins="*", async_mode='eventlet')

# Simulated route (lat, lon) across the US (same idea as frontend)
SIMULATED_ROUTE = [
    (40.7128, -74.0060),  # New York
    (39.9526, -75.1652),  # Philadelphia
    (39.2904, -76.6122),  # Baltimore
    (38.9072, -77.0369),  # Washington DC
    (39.0997, -94.5786),  # Kansas City
    (41.8781, -87.6298),  # Chicago
    (41.2565, -95.9345),  # Omaha
    (38.6270, -90.1994),  # St. Louis
    (34.0522, -118.2437), # Los Angeles
    (37.7749, -122.4194), # San Francisco
]

def simulate_driver(driver_id="driver-1", interval=3):
    i = 0
    n = len(SIMULATED_ROUTE)
    while True:
        lat, lon = SIMULATED_ROUTE[i % n]
        payload = {
            "driver_id": driver_id,
            "lat": lat,
            "lon": lon,
            "timestamp": int(time.time())
        }
        socketio.emit('driver_location', payload, namespace='/track')
        i += 1
        socketio.sleep(interval)  # friendly to eventlet

@socketio.on('connect', namespace='/track')
def connect():
    print("Client connected")
    emit('connected', {'msg': 'connected to backend'})

@socketio.on('update_location', namespace='/track')
def handle_update_location(data):
    """
    Expected data:
      { "driver_id": "driver-123", "lat": 12.34, "lon": 56.78, "timestamp": 1234567890 }
    This handler receives a driver's update and re-broadcasts it to all clients
    on the /track namespace as 'driver_location'.
    """
    # optional: validate data
    driver_id = data.get("driver_id", "unknown")
    lat = data.get("lat")
    lon = data.get("lon")
    timestamp = data.get("timestamp", int(time.time()))

    payload = {
        "driver_id": driver_id,
        "lat": lat,
        "lon": lon,
        "timestamp": timestamp
    }

    # emit to everyone (including origin) on namespace '/track'
    socketio.emit('driver_location', payload, namespace='/track')
    # (optional) log for debugging
    print("Received update_location:", payload)


@app.route('/', methods=['GET'])
def root():
    resp = make_response(jsonify({"status": "ok", "msg": "backend alive"}), 200)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
    resp.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
    return resp


if __name__ == '__main__':
    # start simulator in background thread
    port = int(os.environ.get("PORT", 5000))
    print(f"Starting Flask-SocketIO server on http://0.0.0.0:{port}")
    socketio.run(app, host='0.0.0.0', port=port)
