import time

import paho.mqtt.client as mqtt

############################################################
# Relevanter Teil fuer die Uebung
# Hier die MQTT settings eintragen
ONLINE_BROKER = "test.mosquitto.org"
ISW_BROKER = ""
PORT = 1883
TOPIC = "isw/ITArch/Team-TEAMNAME"
MESSAGE = "Hello from Team TEAMNAME"

BROKER = ONLINE_BROKER

#Ab hier muss nichts mehr angepassst werden
############################################################


# Create an MQTT client instance
client = mqtt.Client()

# Connect to the broker
client.connect(BROKER, PORT, 60)

# Publish the message
client.publish(TOPIC, MESSAGE)
print(f"Published message '{MESSAGE}' to topic '{TOPIC}'.")

# In case of continous publishing 
#while True:
#    # Publish the message
#    client.publish(TOPIC, MESSAGE)
#    print(f"Published message '{MESSAGE}' to topic '{TOPIC}'.")
#    time.sleep(5)

# Disconnect from the broker
client.disconnect()

