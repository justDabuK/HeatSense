from Adafruit_BME280 import *
from strandtest import *
from neopixel import *
from send_email import sendemail


def main():
    sensor = BME280(t_mode=BME280_OSAMPLE_8, p_mode=BME280_OSAMPLE_8, h_mode=BME280_OSAMPLE_8)
    print "Initialized sensor"
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    strip.begin()
    print "Initialized strip"
    send_flag = 0
    
    while(True):
        degrees = sensor.read_temperature()
        degrees = sensor.read_temperature()
        pascals = sensor.read_pressure()
        hectopascals = pascals / 100
        humidity = sensor.read_humidity()

        if degrees < 30.0:
            colorWipe(strip, Color(255, 0, 0))
            if send_flag == 0:
                send_flag = 1
                print "everything is normal"
        else:
            colorWipe(strip, Color(0, 255, 0))
            if send_flag == 1:
                send_flag = 0
                sendemail(
                    'heatsense5000@gmail.com',
                    'sinaisabell.springer@outlook.de',
                    '', 'ATTENTION!!!!!',
                    'Your dog is overheating, currently {0:0.3f} deg C'.format(degrees),
                    'heatsense5000@gmail.com',
                    'TMSBausses'
                )
                print "HEAT!!!!!!"
    colorWipe(strip, Color(0, 0, 0), 10)

if __name__ == "__main__":
    main()
