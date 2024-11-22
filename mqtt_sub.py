import paho.mqtt.client as mqtt
import json
from flask import Flask, render_template
from datetime import datetime


BROKER = "localhost"  
PORT = 1883
TOPIC = "iot_device"  

received_messages = []


def on_message(client, userdata, msg):
    global received_messages
    try:
        
        payload = msg.payload.decode("utf-8")
        print(f"Received message (raw): {payload}")  
        
      
        message = json.loads(payload)
        received_messages.append(message)
        print(f"Decoded message: {json.dumps(message, indent=4)}")
    except json.JSONDecodeError:
        print(f"Failed to decode payload: {msg.payload}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Set up MQTT client and callbacks
mqtt_client = mqtt.Client()

# Connect to the MQTT broker
mqtt_client.connect(BROKER, PORT, 60)

# Set the callback for message handling
mqtt_client.on_message = on_message

# Subscribe to the iot_device topic
mqtt_client.subscribe(TOPIC)

# Start the MQTT client loop in a background thread
mqtt_client.loop_start()

# Set up the Flask application
app = Flask(__name__)

# Flask route to return all received messages as a table
@app.route('/data', methods=['GET'])
def get_data():
    # Render all received messages in a table
    return render_template('index.html', messages=received_messages)

# Main function to run the Flask application
if __name__ == '__main__':
    try:
        print("Flask app is running. Access it at http://127.0.0.1:5000/data")
        app.run(debug=True, use_reloader=False) 
    except KeyboardInterrupt:
        print("Server stopped.")
        mqtt_client.disconnect()
