from flask import Flask
from flask_restful import Resource, Api, reqparse
from rpi_ws281x import Adafruit_NeoPixel, Color
import time
import random
import led_config as config

app = Flask(__name__)
api = Api(app)

ledStrip_args = reqparse.RequestParser()
ledStrip_args.add_argument("red", type=int, help="red color value was not passed...")
ledStrip_args.add_argument("green", type=int, help="green color Value was not passed...")
ledStrip_args.add_argument("blue", type=int, help="blue color Value was not passed...")

class LedStrip(Resource):

    def clear(self):
        self.colorWipe(Color(0,0,0), 0)

### -- The following effects came from the Core Electronics strandtest.py: https://github.com/rpi-ws281x/rpi-ws281x-python/blob/master/examples/strandtest.py 

    def colorWipe(self, color, seconds):
        """Wipe color across display a pixel at a time."""
        for i in range(300):
            strip.setPixelColor(i, color)
            strip.show()
            time.sleep(seconds)

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
        
    def rainbow(self):
        """Draw rainbow that fades across all pixels at once."""
        for j in range(256):
            for i in range(strip.numPixels()):
                strip.setPixelColor(i, self.wheel((i+j) & 255))
            strip.show()
            time.sleep(20/1000.0)
    
    def rainbowCycle(self, iterations=5):
        """Draw rainbow that uniformly distributes itself across all pixels."""
        for j in range(256*iterations):
            for i in range(strip.numPixels()):
                strip.setPixelColor(i, self.wheel((int(i * 256 / strip.numPixels()) + j) & 255))
            strip.show()
            time.sleep(20/1000.0)
            
### -- End of Core Electronics effects

    def post(self, effect):
        # the strip by setting each pixel to Color(0,0,0)  
        self.clear()

        #red, green, and blue will come as arguments from the request body
        args = ledStrip_args.parse_args()

        if(effect == "wipe"):
            self.colorWipe(Color(args.red, args.green, args.blue), 0.01)

        elif(effect == "randomize"):
            #generate random RGB color codes
            red = random.randint(0, 255)
            green = random.randint(0, 255)
            blue = random.randint(0, 255)

            self.colorWipe(Color(red, green, blue), 0.01)

        elif(effect == "rainbow"):
            self.rainbow()

        elif(effect == "rainbowCycle"):
            self.rainbowCycle()

api.add_resource(LedStrip, '/<string:effect>')

if __name__ == '__main__':

    # NeoPixel Object - references LED Strip
    strip = Adafruit_NeoPixel(config.LED_COUNT, config.LED_PIN, config.LED_FREQ_HZ, config.LED_DMA, config.LED_INVERT, config.LED_BRIGHTNESS, config.LED_CHANNEL)
    
    # Initalize NeoPixel Object
    strip.begin()

    # Run the Server
    app.run(debug=True)