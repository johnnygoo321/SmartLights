from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS
from rpi_ws281x import Adafruit_NeoPixel, Color
from dotenv import load_dotenv
import os
import time
import random
import led_config as config

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

    def clear(self):
        #To clear the LED Strip set the RGB color value to 0
        for i in range(300):
            strip.setPixelColor(i, Color(0, 0, 0))
        strip.show()

### -- The following effects came from the Core Electronics strandtest.py: https://github.com/rpi-ws281x/rpi-ws281x-python/blob/master/examples/strandtest.py 
### -- Modifications to the logic have been made as part of this project and additional customizations have been added

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

    def rainbowCycle(self, seconds, iterations=5):
        """Draw rainbow that uniformly distributes itself across all pixels."""
        for j in range(256*iterations):
            for i in range(strip.numPixels()):
                strip.setPixelColor(i, self.wheel((int(i * 256 / strip.numPixels()) + j) & 255))
            strip.show()
            time.sleep(seconds)
        

    def theaterChaseRainbow(self, seconds):
        """Rainbow movie theater light style chaser animation."""
        for j in range(256):
            for q in range(3):
                for i in range(0, strip.numPixels(), 3):
                    strip.setPixelColor(i+q, self.wheel((i+j) % 255))
                strip.show()
                time.sleep(seconds)
                for i in range(0, strip.numPixels(), 3):
                    strip.setPixelColor(i+q, 0)

### -- End of Core Electronics effects
            
    def post(self, effect=None, type=None):
        try:
            #Clear the strip by setting each pixel to Color(0,0,0)  
            self.clear()

            #Red, green, and blue will optionally come as arguments from the request body
            args = self.reqparse.parse_args()

            if(effect == "wipe"):
                self.colorWipe(0.01, Color(args.red, args.green, args.blue))
            
            elif (effect == 'noEffect'):
                self.noEffect(Color(args.red, args.green, args.blue))
            
            elif(effect == "rainbow"):
                self.rainbow(0.02)

            elif(effect == "rainbowCycle"):
                self.rainbowCycle(0.02)
            
            elif(effect == 'randomize'):
                self.randomize()

            elif(effect == "theaterChase"):
                self.theaterChase(0.01, Color(args.red, args.green, args.blue))
            
            elif(effect == "theaterChaseRainbow"):
                self.theaterChaseRainbow(0.01)
            
            return "Lights Configured Successfully...", 200

        except Exception as e:   
            return "Server Error", e
  
api.add_resource(LedStrip, '/clear', '/<string:effect>', '/<string:effect>/<string:type>')

if __name__ == '__main__':

    #NeoPixel Object - references LED Strip
    strip = Adafruit_NeoPixel(config.LED_COUNT, config.LED_PIN, config.LED_FREQ_HZ, config.LED_DMA, config.LED_INVERT, config.LED_BRIGHTNESS, config.LED_CHANNEL)

    #Initalize NeoPixel Object
    strip.begin()

    #Run the Server
    app.run(host=os.environ.get("IPV4_ADDRESS_OF_PI"),debug=True, port=os.environ.get("PORT"), threaded=True)
    