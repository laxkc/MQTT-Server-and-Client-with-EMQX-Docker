MQTT Server and Client with EMQX Docker
=======================================

This project demonstrates the setup of an MQTT server and client using EMQX (Erlang/Enterprise MQTT Broker) with Docker, facilitating real-time data exchange between an IoT device and a web application. The system uses the MQTT protocol for lightweight and efficient communication between devices and web interfaces. The data flow is managed by an MQTT server running on EMQX, while the client publishes sensor data (such as CPU usage, memory usage, and timestamps) to a specific MQTT topic. The web application subscribes to this topic, receives the data, and displays it in a tabular format on a frontend.

Project Overview
----------------

### Architecture

*   **IoT Device (mqtt\_pub.py)**:
    
    *   This Python script simulates an IoT device that gathers data (e.g., CPU and memory usage, timestamp) and publishes it to the MQTT server on the topic iot\_device.
        
*   **MQTT Server (EMQX Docker)**:
    
    *   The MQTT server is set up using the EMQX broker, which acts as the middleman to receive and forward messages between the device and the web application.
        
*   **Web Application (mqtt\_sub.py)**:
    
    *   A Python Flask-based web application that subscribes to the iot\_device topic. The data received from the MQTT server is processed and rendered as an HTML page.
        
*   **Frontend (HTML)**:
    
    *   The frontend displays the received IoT data in a tabular format.
        

Features
--------

*   **Real-time Data Exchange**:
    
    *   The MQTT protocol ensures that data is transmitted in real time between the IoT device and the web application.
        
*   **Data Display**:
    
    *   The web application processes the data and displays it in an easy-to-read tabular format.
        
*   **Flask Integration**:
    
    *   The web app is built using Flask, making it easy to set up and integrate with various backend services.
        

Setup Instructions
------------------

### Prerequisites

*   Docker
    
*   Python 3.x
    
*   Flask
    
*   EMQX Docker Image
    

### Steps to Run

1.  **Set up MQTT Server with EMQX**:
    
    *   bashCopy codedocker run -d -p 1883:1883 -p 8083:8083 emqx/emqx
        
    *   This will start the MQTT server on port 1883 and the WebSocket on 8083.
        
2.  **Run the IoT Device Simulation (iotdevice.py)**:
    
    *   bashCopy codepip install paho-mqtt
        
    *   bashCopy codepython mqtt\_pub.py
        
3.  **Run the Web Application (webapp.py)**:
    
    *   bashCopy codepip install Flask paho-mqtt
        
    *   bashCopy codepython mqtt\_sub.py
        
    *   The application will start, and you can view the data at http://localhost:5000.
        
4.  **Access the Frontend**:
    
    *   Once the web application is running, navigate to http://localhost:5000/data in your browser to see the data displayed in a table.
        

Notes
-----

*   The mqtt\_pub.py script is responsible for publishing the data from the simulated IoT device to the MQTT server.
    
*   The mqtt\_sub.py script subscribes to the iot\_device topic and displays the incoming data on a simple HTML page.
    

Contributing
------------

Feel free to fork this repository and contribute improvements. You can open issues or create pull requests for bug fixes and new features.