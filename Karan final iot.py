
# coding: utf-8

# In[ ]:


# coding: utf-8

# In[ ]:


# Install below packages
'''
sudo pip3 install azure-iot-device
sudo pip3 install azure-iot-hub
sudo pip3 install azure-iothub-service-client
sudo pip3 install azure-iothub-device-client
'''

# Run below on Azure CLI
'''
#### below to add extension
az extension add --name azure-cli-iot-ext

### Below to start device monitor to check incoming telemetry data
az iot hub monitor-events --hub-name YourIoTHubName --device-id MyPythonDevice

'''

# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

import random
import time

# Using the Python Device SDK for IoT Hub:
#   https://github.com/Azure/azure-iot-sdk-python
# The sample connects to a device-specific MQTT endpoint on your IoT Hub.
from azure.iot.device import IoTHubDeviceClient, Message

# The device connection string to authenticate the device with your IoT hub.
# Using the Azure CLI:
# az iot hub device-identity show-connection-string --hub-name {YourIoTHubName} --device-id MyNodeDevice --output table
CONNECTION_STRING = "HostName=iot-karan.azure-devices.net;DeviceId=mydevice;SharedAccessKey=9nb2KNGOXoRnkgJJK8QZa3JFo1XOI87231YESbb3egM="

# Define the JSON message to send to IoT Hub.
PH = 5.0
TURBUDITY = 0.5
CHLORINE = 2
DISSOLVED_OXYGEN = 6.5
MSG_TXT = '{{"PH": {PH},"TURBUDITY": {TURBUDITY},"CHLORINE":{CHLORINE},"DISSOLVED_OXYGEN": {DISSOLVED_OXYGEN}}}'

def iothub_client_init():
    # Create an IoT Hub client
    client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)
    return client

def iothub_client_telemetry_sample_run():

    try:
        client = iothub_client_init()
        print ( "IoT Hub device sending periodic messages, press Ctrl-C to exit" )
        while True:
            # Build the message with simulated telemetry values.
            ph = PH + (random.random() * 15)
            turbudity = TURBUDITY + (random.random() * 15)
            chlorine= CHLORINE + (random.random() * 15)
            dissolved_oxygen =DISSOLVED_OXYGEN + (random.random() * 15)
            msg_txt_formatted = MSG_TXT.format(ph=ph, turbudity=turbudity,chlorine=chlorine , dissolved_oxygen=dissolved_oxygen)
            message = Message(msg_txt_formatted)

            # Add a custom application property to the message.
            # An IoT hub can filter on these properties without access to the message body.
            #if temperature > 30:
              #message.custom_properties["temperatureAlert"] = "true"
            #else:
              #message.custom_properties["temperatureAlert"] = "false"

            # Send the message.
            print( "Sending message: {}".format(message) )
            client.send_message(message)
            print ( "Message successfully sent" )
            time.sleep(3)

    except KeyboardInterrupt:
        print ( "IoTHubClient sample stopped" )

if __name__ == '__main__':
    print ( "IoT Hub Quickstart #1 - Simulated device" )
    print ( "Press Ctrl-C to exit" )
    iothub_client_telemetry_sample_run()

