import paho.mqtt.client as mqtt

class MQTTClient:
    def __init__(self, broker, port, topic, client_id):
        self.client = mqtt.Client(client_id)
        self.broker = broker
        self.port = port
        self.topic = topic

    def connect(self):
        self.client.connect(self.broker, self.port)
        print(f"Connected to MQTT broker at {self.broker}:{self.port}")

    def publish(self, message):
        self.client.publish(self.topic, message)
        print(f"Message published to topic {self.topic}: {message}")

    def disconnect(self):
        self.client.disconnect()
        print("MQTT client disconnected")
