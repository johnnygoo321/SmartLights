import board

# LED STRIP DEFAULT CONFIGURATION
LED_COUNT      = 300     # Number of LED's.
LED_PIN        = 18      # GPIO PWM pin connected to the pixels.
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating a signal (try 10)
LED_BRIGHTNESS = 25      # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
LED_SECONDS    = 0.01   # Speed of different animations
LED_BRIGHTNESS_ANIMATION_LIB = 0.5 # Brightness range for the Adafruit Animation Library is 0 to 1
LED_PIN_ANIMATION_LIB = board.D18  # Animation Library Pin