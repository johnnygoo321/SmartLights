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
        self.wipe(Color(0,0,0), 0)

    def wipe(self, color, seconds):
        for i in range(300):
            strip.setPixelColor(i, color)
            strip.show()
            time.sleep(seconds)

    def post(self, effect):      
        # the strip by setting each pixel to Color(0,0,0)  
        self.clear()

        #red, green, and blue will come as arguments from the request body
        args = ledStrip_args.parse_args()

        if(effect == "wipe"):
            self.wipe(Color(args.red, args.green, args.blue), 0.01)

        #NEED RANDOMIZE TO WORK WITH ANY EFFECT
        elif(effect == "randomize"):
            #generate random RGB color codes
            red = random.randint(0, 255)
            green = random.randint(0, 255)
            blue = random.randint(0, 255)

            self.wipe(Color(red, green, blue), 0.01)

api.add_resource(LedStrip, '/<string:effect>')

if __name__ == '__main__':

    # NeoPixel Object - references LED Strip
    strip = Adafruit_NeoPixel(config.LED_COUNT, config.LED_PIN, config.LED_FREQ_HZ, config.LED_DMA, config.LED_INVERT, config.LED_BRIGHTNESS, config.LED_CHANNEL)
    
    # Initalize NeoPixel Object
    strip.begin()

    # Run the Server
    app.run(debug=True)