# SmartLights

👋 Welcome to the Smart Lights app!

**Creator:** [@johnnycodes_](https://www.instagram.com/johnnycodes_/)

### **Background:**

This project was created with the purpose of locally being able to control an addressable led strip through a Raspberry Pi. We could of used a WLED controller to make things a bit easier, but as a challenge I decided to create my own full stack application 😅.

### **Tech Stack:**
For the frontend I used **Expo** which allows you to create a mobile app that works with both IOS and Android all through JavaScript. Also, through a QR code, you can locally run the app straight from your mobile device. With the backend, **Flask-RESTFul** was used to service any requests made from the app.
You will notice in my backend app.py file, two NeoPixel Objects were instantiated to interact with the lights. The reason for this is to show the use of both the [Adafruit CircuitPython Animation Library](https://learn.adafruit.com/circuitpython-led-animations/overview) and the [Adafruit Neopixel Library](https://github.com/adafruit/Adafruit_NeoPixel).

### **Working Demo:**
<img src="https://github.com/johnnygoo321/SmartLights/assets/55931717/bab72fff-a247-4abb-aa19-6c3d23fe74a9" width="350" height="250">
<img src="https://github.com/johnnygoo321/SmartLights/assets/55931717/3c6a1bae-574d-44b4-990e-2cd22ec82630" width="350" height="250">

### **Custom Controller:**
You can definitely add customizations, tweak things, and optimize as much as you want. This is a base controller I have hooked up.

<img src="https://github.com/johnnygoo321/SmartLights/assets/55931717/1f3e94bb-e9ae-4045-a083-939a74ec92b3" width="250" height="475">

## Table of Contents:

1. [Hardware Used w/Links](#hardware)
2. [Design](#design)
3. [Cloning the Repo & Getting Started](#cloning-the-repo--getting-started)
4. [LED Strip Configuration File](#led-strip-configuration-file)
5. [Running the app (Locally)](#running-the-app-locally)
6. [License](#license)
7. [Found an issue](#found-an-issue)
8. [Have a question](#have-a-question)

## Hardware

**Please keep in mind these are the items I purchased for this project, you do not have to get the same ones.**

(1) Raspberry Pi 4: [Pi4 64bit 4GB](https://www.amazon.com/Raspberry-Model-2019-Quad-Bluetooth/dp/B07TC2BK1X/ref=sr_1_3?crid=PIVQ34NEUCQ2&keywords=raspberry%2Bpi%2B4&qid=1701222101&sprefix=raspberry%2Bpi%2B4%2Caps%2C105&sr=8-3&th=1) - This is only the PI, but a Micro SD and Power Supply will be needed).

(2) Addressable LED Strip: [WS2812B RGB Strip](https://www.amazon.com/dp/B088FK8NG6?ref=ppx_yo2ov_dt_b_product_details&th=1) - I purchased the White IP67 300LED solely because I like how they look.

(3) LED Strip Power Supply: [ALITOVE 5V 10A Adapter](https://www.amazon.com/dp/B0852HL336?ref=ppx_yo2ov_dt_b_product_details&th=1) - these work great with the strip.

(4) 12V DC Power Connector (Only need one Female Jack): [DAYKIT DC Power Connector](https://www.amazon.com/DAYKIT-Female-2-1x5-5MM-Adapter-Connector/dp/B01J1WZENK/ref=sr_1_10?crid=3SZBSSG1OAABR&keywords=female+dc+jack+connector&qid=1701313367&sprefix=female+dc+jack+cvonnector%2Caps%2C96&sr=8-10)

(5) Jumper Wires (Only need two Male to Female Wires): [Haitronic Wires](https://www.amazon.com/gp/product/B01LZF1ZSZ/ref=ppx_yo_dt_b_asin_title_o06_s01?ie=UTF8&psc=1)

(6) Micro SD Reader (May be optional): With the command below, check which OS version your PI is running. If it is running as 32bit (armv7l), then we will need to upgrade to 64bit to run React Native.
Ensure it can be upgraded to 64bit, then follow the tutorial here: [Raspberry Pi 64 bit install](https://www.youtube.com/watch?v=4_j5lcQEvG4)

```
uname -m
```
## Design
<img src="https://github.com/johnnygoo321/SmartLights/assets/55931717/96fb42c7-1069-4dcc-bf86-b3671301c7f0" width="375" height="275"><br>

I am not using a Level Shifter, refer to the [Adafruit documentation](https://learn.adafruit.com/neopixels-on-raspberry-pi/raspberry-pi-wiring#using-external-power-source-without-level-shifting-3005993) for more on this.
It is important to have an external power supply that is able to power the LEDs (5V 10A in this case to power 300 LEDs).

**BEFORE POWERING ANYTHING ON**

Here is a YouTube walkthrough I really like, go to the section [Assembly For Long LED Strip](https://www.youtube.com/watch?v=aNlaj1r7NKc&t=188s).
Refer back to the bullets below to cross check that you have covered everything.

- Connect a Female to Male jumper wire to both GPIO pin 18 and a Ground pin on your PI.
- Insert the Male end of the Ground jumper wire to the Ground Connection of the LED Strip (your strip will indicate which wire is Ground (GND) normally white).
- Insert the Male end of the GPIO pin 18 jumper wire to the data connection of the LED Strip (your strip will indicate which wire is Data (DIN) normally green).
- **Note with the next step you will first need to use something like a wire stripper to expose the positive and ground connections before connecting it to the Female Jack**
- With the red and white (postive/ground) wires coming out from the strip (reference the image above), connect the red +5V connection to the positive mark on the Female Connector Jack and white GND to negative mark on the Jack.
- Connect the 5V 10A Power Supply (which is what I used to power 300 leds) to the Female Jack.
- Connect the separate PI USBC power cord into the PI.

You should now have a reflection of the image above. Be careful with your connections, and double check everything. You don't want to short your lights lol.<br><br>
[Guide on understanding the White, Red, and Green LED Strip connections.](https://learn.sparkfun.com/tutorials/ws2812-breakout-hookup-guide/addressable-led-strips#pinout)
  
## Cloning the Repo & Getting Started

**For this you can either connect to the PI and use the terminal from there or SSH (much easier) into it.**

I will assume git, python, pip, node, and npm are already installed on your PI.

Install React Native Expo:

```
npm install expo
```

Clone the Repo

```
git clone https://github.com/johnnygoo321 SmartLights.git
```

Install the necessary dependencies

```
cd SmartLights
```

- Open two terminals side-by-side
- cd into smartLights_app on one

```
npm install
```

- cd into smartLights_server on the other

```
pip3 install requirements.txt
```

## LED Strip Configuration File

Update the configuration as needed in the **smartLights_server/led_config.py** file. 
In reality, you probably only need to change the LED_COUNT and can play around with the LED_BRIGHTNESS / LED_BRIGHTNESS_ANIMATION_LIB.

```python
import board

# LED STRIP DEFAULT CONFIGURATION
LED_COUNT      = 300     # Number of LED's.
LED_PIN        = 18      # GPIO PWM pin connected to the pixels.
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating a signal (try 10)
LED_BRIGHTNESS = 25      # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
LED_SECONDS    = 0.01    # Speed it takes to light up a single LED
LED_BRIGHTNESS_ANIMATION_LIB = 0.5 # Brightness range for the Adafruit Animation Library is 0 to 1
LED_PIN_ANIMATION_LIB = board.D18  # Animation Library Pin
```

On top of that, you are going to want to create a .env file in the root of the smartLights_app and smartLights_server folders

```
smartLights_app .env file contents:

IPV4_ADDRESS_OF_PI=http://192.xxx.x.xx
SERVER_PORT=5000
```
```
smartLights_server .env file contents:

IPV4_ADDRESS_OF_PI=192.xxx.x.xx
PORT=5000
```

## Running the App (Locally)

If there are any issues executing these steps or potentially missing steps let me know through a Pull Request or DM me on Instagram [@johnnycodes_](https://www.instagram.com/johnnycodes_/).

Now that we have the initial setup, let's run this thing! Althought this is a single project, it is best to run the backend in a virtual environment.
This will help prevent package versioning issues across many projects.

```
sudo python3 -m venv .venv
source .venv/bin/activate
```
Start the backend server... First run pwd to get the working directory. We will use this to run the venv with root privledges.

```
pwd
sudo 'your_pwd_here'/.venv/bin/python3 app.py
```
In a separate terminal start the frontend application (keep in mind you need to install the Expo Go app on your mobile device to scan the QR code).
Also be sure your PI and mobile device are running under the same network.

```
npx expo start
```
Now you can interact with the lights through your mobile device!

## License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/johnnygoo321/SmartLights/blob/73180602de507baa635b0abe68ac369f08fd7ed6/LICENSE.md) file for details.

## Found an issue
If you have found an issue, please feel free to raise a Pull Request 😊.

## Have a question
Hit me up on Instagram [@johnnycodes_](https://www.instagram.com/johnnycodes_/).
