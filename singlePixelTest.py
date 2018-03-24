from strandtest import *
from neopixel import *

def main():
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    strip.begin()

    try:
        while True:
            for i in range(3, strip.numPixels()):
                print "LED #", i
                print "-> red"
                strip.setPixelColor(i, Color(200, 0, 0, 0))
                strip.show()
                time.sleep(2)

                print "-> green"
                strip.setPixelColor(i, Color(0, 200, 0, 0))
                strip.show()
                time.sleep(2)

                print "-> blue"
                strip.setPixelColor(i, Color(0, 0, 200, 0))
                strip.show()
                time.sleep(2)

                print "-> white"
                strip.setPixelColor(i, Color(0, 0, 0, 200))
                strip.show()
                time.sleep(2)

    except KeyboardInterrupt:
        print "exiting"
        colorWipe(strip, Color(0, 0, 0), 10)


if __name__ == "__main__":
    main()
