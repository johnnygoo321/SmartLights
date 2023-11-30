# SmartLights

👋 Welcome to the Smart Lights app!

### **Background:**

This project was created with the purpose of locally being able to control an addressable led strip through a Raspberry Pi. We could of used a WLED controller to make things a bit easier, but as a challenge I decided to create my own full stack app 😅.

### **Tech Stack:**

For the frontend I used **Expo** which allows me to create a mobile app that works with both IOS and Android all through JavaScript. With the backend, **Flask-RESTFul** was used to service any requests made from the app.

### **Working Demo:**

...insert image...

...insert image...

...insert image...

## Table of Contents:

1. [Hardware Used w/Links](#hardware)
2. [Design](#design)
3. [Cloning the Repo & Getting Started](#cloning-the-repo--getting-started)
4. [LED Strip Configuration File](#led-strip-configuration-file)
5. [Running the app (Locally)](#running-the-app-locally)

## Hardware

**Please keep in mind these are the items I purchased for this project, you do not have to get the same ones.**

(1) Raspberry Pi 4: [Pi4 64bit 4GB](https://www.amazon.com/Raspberry-Model-2019-Quad-Bluetooth/dp/B07TC2BK1X/ref=sr_1_3?crid=PIVQ34NEUCQ2&keywords=raspberry%2Bpi%2B4&qid=1701222101&sprefix=raspberry%2Bpi%2B4%2Caps%2C105&sr=8-3&th=1) - This is only the PI, but a Micro SD and Power Supply will be needed)

(2) Addressable LED Strip: [WS2812B RGB Strip](https://www.amazon.com/dp/B088FK8NG6?ref=ppx_yo2ov_dt_b_product_details&th=1) - I purchased the White IP67 300LED solely because I like how they look.

(3) LED Strip Power Supply: [ALITOVE 5V 10A Adapter](https://www.amazon.com/dp/B0852HL336?ref=ppx_yo2ov_dt_b_product_details&th=1) - these work great with the strip.

(4) Jumper Wires: [Haitronic Wires](https://www.amazon.com/gp/product/B01LZF1ZSZ/ref=ppx_yo_dt_b_asin_title_o06_s01?ie=UTF8&psc=1)

## Design

... insert image...

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
In reality, you probably only need to change the LED_COUNT and can play around with the LED_BRIGHTNESS.

https://github.com/johnnygoo321/SmartLights/blob/491c97d671964ce35bc1f0f61a949e27319120fe/smartLights_server/led_config.py#L1C1-L8C69

## Running the App (Locally)

Now that we have the initial setup, let's run this thing! Althought this is a single project, it is best to run the backend in a virutal environment.
This will help prevent package versioning issues across many projects.

```
sudo python3 -m venv venv
source .venv/bin/activate
```
Start the backend server... First run pwd to get the working directory. We will use this to run the venv with root privledges.

```
pwd
sudo 'your_pwd_here'/.venv/bin/python3 app.py
```
In a separate terminal start the frontend application (keep in mind you need to install expo on your mobile device to scan the QR code)

```
npx start expo
```
