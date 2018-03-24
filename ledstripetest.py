from strandtest import *
from neopixel import *

def main():
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    strip.begin()

    try:
        while True:
            print "full red"
            colorWipe(strip, Color(200, 0, 0), wait_ms=500)

            print "full green"
            colorWipe(strip, Color(0, 200, 0), wait_ms=500)

            print "full blue"
            colorWipe(strip, Color(0, 0, 200), wait_ms=500)

            print "full white"
            colorWipe(strip, Color(0, 0, 0, 200), wait_ms=500)

    except KeyboardInterrupt:
        print "exiting"
        colorWipe(strip, Color(0, 0, 0), 10)


if __name__ == "__main__":
    main()