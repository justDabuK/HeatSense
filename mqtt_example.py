import paho.mqtt.publish as publish
import time
print("Sending 0...")
publish.single("ledStatus", "0", hostname="127.0.0.1")
time.sleep(1)
print("Sending 1...")
publish.single("ledStatus", "1", hostname="127.0.0.1")

