import paho.mqtt.client as mqtt #import the client1
import time
from Adafruit_BME280 import *
from strandtest import *
from neopixel import *
from send_email import sendemail
from traffic_light import *

send_flag = 0

def on_message(client, userdata, message):
    degrees = float(str(message.payload.decode("utf-8")).split("#")[1])
    #print("message received ", str(degrees))
    #print("message topic=", message.topic)
    #print("message qos=", message.qos)
    #print("message retain flag=", message.retain)

    global send_flag

    if degrees < 28.0:
        green(strip)
        if send_flag == 0:
            send_flag = 1
            print "everything is ok"
    else:
        red(strip)
        if send_flag == 1:
            send_flag = 0
            """sendemail(
                'heatsense5000@gmail.com',
                'kevinjust87@gmail.com',
                '', 'ATTENTION!!!!!',
                'Your dog is overheating, currently {0:0.3f} deg C'.format(degrees),
                'heatsense5000@gmail.com',
                'TMSBausses'
            )"""
            print "HEAT!!!!!"


if __name__ == "__main__":
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    strip.begin()
    print "Initialized strip"


    broker_address = "127.0.0.1"

    print("creating new instance")
    client = mqtt.Client("P1")  # create new instance
    client.on_message = on_message  # attach function to callback
    print("connecting to broker")
    client.connect(broker_address) # connect to broker
    client.loop_start()  # start the loop
    print("Subscribing to topic", "collarTemp")
    client.subscribe("collarTemp")
    
    yellow(strip)

    try:
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        print "exiting"
        client.disconnect()
        client.loop_stop()

