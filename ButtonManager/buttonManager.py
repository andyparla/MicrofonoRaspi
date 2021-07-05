import RPi.GPIO as GPIO
import signal
import sys

GPIO.setmode(GPIO.BCM)

BUTTON_GPIO = 4;  # button to monitor for button presses.
LED_output = 17;  # LED to light or not depending on button presses.

# GPIO btn_input set up as input.
GPIO.setup(BUTTON_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# GPIO.setup(LED_output, GPIO.OUT)

def signal_handler(sig, frame):
    GPIO.cleanup()
    sys.exit(0)

def button_callback(channel):
    if not GPIO.input(BUTTON_GPIO):
        print("Button pressed!")
    else:
        print("Button released!")


GPIO.add_event_detect(BUTTON_GPIO, GPIO.BOTH, callback=button_callback)

signal.signal(signal.SIGINT, signal_handler)
signal.pause()