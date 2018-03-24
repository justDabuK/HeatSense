from strandtest import *
from neopixel import *

def main():
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    strip.begin()

    try:
        while True:
            print "green"
            strip.setPixelColor(0, Color(200, 0, 0))
            strip.show()

            strip.setPixelColor(1, Color(0, 200, 0))
            strip.show()

            strip.setPixelColor(2, Color(0, 0, 200))
            strip.show()

            strip.setPixelColor(4, Color(200, 0, 0))
            strip.show()

            time.sleep(2)

            print "red"
            strip.setPixelColor(0, Color(0, 200, 0))
            strip.show()

            strip.setPixelColor(1, Color(0, 0, 200))
            strip.show()

            strip.setPixelColor(3, Color(200, 0, 0))
            strip.show()

            strip.setPixelColor(4, Color(0, 200, 0))
            strip.show()

            time.sleep(2)

    except KeyboardInterrupt:
        print "exiting"
        colorWipe(strip, Color(0, 0, 0), 10)


if __name__ == "__main__":
    main()
