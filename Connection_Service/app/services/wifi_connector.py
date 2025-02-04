import network
import time

class WiFiConnector:
    def __init__(self, ssid, password):
        self.ssid = ssid
        self.password = password
        self.wlan = network.WLAN(network.STA_IF)

    def connect(self):
        self.wlan.active(True)
        if not self.wlan.isconnected():
            print(f"Connecting to Wi-Fi network: {self.ssid}")
            self.wlan.connect(self.ssid, self.password)
            while not self.wlan.isconnected():
                time.sleep(1)
        print(f"Connected to Wi-Fi: {self.wlan.ifconfig()}")

    def disconnect(self):
        self.wlan.active(False)
        print("Wi-Fi disconnected")
