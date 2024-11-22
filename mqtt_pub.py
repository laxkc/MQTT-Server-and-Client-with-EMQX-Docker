import time
import psutil
import paho.mqtt.client as mqtt
from datetime import datetime
import json  

# MQTT broker configuration
BROKER = "localhost"  
PORT = 1883
TOPIC = "iot_device"  

# Function to collect system information
def get_system_stats():
    """Collect system stats: timestamp, memory, and CPU usage."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    memory = psutil.virtual_memory().percent  
    cpu = psutil.cpu_percent(interval=1)  
    return {"timestamp": timestamp, "memory_usage": memory, "cpu_usage": cpu}

# Set up MQTT publisher client
client = mqtt.Client()

# Connect to the broker
client.connect(BROKER, PORT, 60)


try:
    while True:
        stats = get_system_stats()
        

        message = json.dumps(stats)  
        
        # Publish the message to the topic
        print(f"Publishing to {TOPIC}: {message}")  
        client.publish(TOPIC, message)
        
        time.sleep(5)  
except KeyboardInterrupt:
    print("Publisher stopped.")
    client.disconnect()
