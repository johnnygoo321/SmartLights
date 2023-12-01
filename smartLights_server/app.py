import os
import time
import random
import neopixel
import led_config as config
from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS
from rpi_ws281x import Adafruit_NeoPixel, Color
from dotenv import load_dotenv
from adafruit_led_animation.animation.sparkle import Sparkle
from adafruit_led_animation.animation.comet import Comet
from adafruit_led_animation.animation.solid import Solid

app = Flask(__name__)
CORS(app)
api = Api(app)
load_dotenv() 

class LedStrip(Resource):

    def __init__(self):
        self.reqparse = reqparse.RequestParser()        
        self.reqparse.add_argument("red", type=int, help="red color value was not passed...")
        self.reqparse.add_argument("green", type=int, help="green color Value was not passed...")
        self.reqparse.add_argument("blue", type=int, help="blue color Value was not passed...")

    def clear(self, effect):
        #To clear the LED Strip set the RGB color value to 0
        if effect not in ["sparkle", "comet"]:
            for i in range(300):
                strip.setPixelColor(i, Color(0, 0, 0))
            strip.show()
        else:
            solid = Solid(pixels, (0, 0, 0))
            solid.animate()

### -- Several of the effects below came from the Core Electronics strandtest.py: https://github.com/rpi-ws281x/rpi-ws281x-python/blob/master/examples/strandtest.py 
### -- Modifications to the logic have been made as part of this project and additional animations have been added via the Adafruit animation library https://docs.circuitpython.org/projects/led-animation/en/latest/index.html

    def colorWipe(self, seconds, color=None, type=None):        
        """Wipe color across display a pixel at a time."""
        for i in range(300):
            color = Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) if type == 'randomize' else color
            strip.setPixelColor(i, color)
            strip.show()
            time.sleep(seconds)

    def noEffect(self, color):
        """Set color across all pixels at the same time."""        
        for i in range(300):
            strip.setPixelColor(i, color)
        strip.show()    

    def randomize(self):
        """Randomize color across all pixels at the same time."""        
        for i in range(300):
            color = Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            strip.setPixelColor(i, color)
        strip.show()

    def theaterChase(self, seconds, color=None, type=None, iterations=50):
        """Movie theater light style chaser animation."""
        for j in range(iterations):
            for q in range(3):
                for i in range(0, strip.numPixels(), 3):
                    color = Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) if type == 'randomize' else color
                    strip.setPixelColor(i+q, color)
                strip.show()
                time.sleep(seconds)
                for i in range(0, strip.numPixels(), 3):
                    strip.setPixelColor(i+q, 0)

    def wheel(self, pos):
        """Generate rainbow colors across 0-255 positions."""
        if pos < 85:
            return Color(pos * 3, 255 - pos * 3, 0)
        elif pos < 170:
            pos -= 85
            return Color(255 - pos * 3, 0, pos * 3)
        else:
            pos -= 170
            return Color(0, pos * 3, 255 - pos * 3)
        
    def rainbow(self, seconds):
        """Draw rainbow that fades across all pixels at once."""
        for j in range(256):
            for i in range(strip.numPixels()):
                strip.setPixelColor(i, self.wheel((i+j) & 255))
            strip.show()
            time.sleep(seconds)

    def rainbowCycle(self, seconds, iterations=2):
        """Draw rainbow that uniformly distributes itself across all pixels."""
        for j in range(256*iterations):
            for i in range(strip.numPixels()):
                strip.setPixelColor(i, self.wheel((int(i * 256 / strip.numPixels()) + j) & 255))
            strip.show()
            time.sleep(seconds)
        
    def theaterChaseRainbow(self, seconds, iterations=60):
        """Rainbow movie theater light style chaser animation."""
        for j in range(iterations):
            for q in range(3):
                for i in range(0, strip.numPixels(), 3):
                    strip.setPixelColor(i+q, self.wheel((i+j) % 255))
                strip.show()
                time.sleep(seconds)
                for i in range(0, strip.numPixels(), 3):
                    strip.setPixelColor(i+q, 0)

    def sparkle(self, seconds, rgbValue):
        """Sparkle animation across the different pixels."""
        sparkle = Sparkle(pixels, seconds, (rgbValue.red, rgbValue.green, rgbValue.blue), num_sparkles=10)   
        runTimer = time.time() + 5.0
        while time.time() < runTimer:
            sparkle.animate()

    def comet(self, seconds, rgbValue):
        """Comet animation across x amount of pixels."""
        comet = Comet(pixels, seconds, (rgbValue.red, rgbValue.green, rgbValue.blue), tail_length=18, bounce=True)
        runTimer = time.time() + 5.0
        while time.time() < runTimer:
            comet.animate()

### -- End of Core Electronics effects
            
    def post(self, effect=None, type=None):
        try:
            #Clear the strip by setting each pixel to rgb(0,0,0)  
            self.clear(effect)

            #Red, green, and blue will optionally come as arguments from the request body
            args = self.reqparse.parse_args()
            print(args)
            
            if(effect == "wipe"):
                self.colorWipe(config.LED_SECONDS, Color(args.red, args.green, args.blue))
            
            elif (effect == 'noEffect'):
                self.noEffect(Color(args.red, args.green, args.blue))
            
            elif(effect == "rainbow"):
                self.rainbow(config.LED_SECONDS)

            elif(effect == "rainbowCycle"):
                self.rainbowCycle(config.LED_SECONDS)
            
            elif(effect == 'randomize'):
                self.randomize()

            elif(effect == "theaterChase"):
                self.theaterChase(config.LED_SECONDS, Color(args.red, args.green, args.blue))
            
            elif(effect == "theaterChaseRainbow"):
                self.theaterChaseRainbow(config.LED_SECONDS)
            
            elif(effect == "sparkle"):
                self.sparkle(config.LED_SECONDS + 0.08, args)
            
            elif(effect == "comet"):
                self.comet(config.LED_SECONDS, args)
            
            return "Lights Configured Successfully...", 200

        except Exception as e:   
            return "Server Error", e
  
api.add_resource(LedStrip, '/clear', '/<string:effect>', '/<string:effect>/<string:type>')

if __name__ == '__main__':

    #NeoPixel instance - references Adafruit CircuitPython Animation library
    pixels = neopixel.NeoPixel(config.LED_PIN_ANIMATION_LIB, config.LED_COUNT, brightness=config.LED_BRIGHTNESS_ANIMATION_LIB, auto_write=False)

    #Instantiating another NeoPixel Object - references Adafruit NeoPixel library
    strip = Adafruit_NeoPixel(config.LED_COUNT, config.LED_PIN, config.LED_FREQ_HZ, config.LED_DMA, config.LED_INVERT, config.LED_BRIGHTNESS, config.LED_CHANNEL)
        
    #Initalize NeoPixel Object
    strip.begin()

    #Run the Server
    app.run(host=os.environ.get("IPV4_ADDRESS_OF_PI"),debug=True, port=os.environ.get("PORT"), threaded=True)