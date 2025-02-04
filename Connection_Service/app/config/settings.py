import os

class Settings:
    GRPC_ASR_HOST = os.getenv("GRPC_ASR_HOST", "asr_service")
    GRPC_ASR_PORT = int(os.getenv("GRPC_ASR_PORT", 50051))
    MQTT_BROKER = os.getenv("MQTT_BROKER", "mqtt_broker")
    MQTT_PORT = int(os.getenv("MQTT_PORT", 1883))

settings = Settings()
