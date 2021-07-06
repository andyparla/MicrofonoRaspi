import RPi.GPIO as GPIO
import signal
import sys

class Botonera():

    BUTTON_GPIO = 4;  # Boton1 para grabar.

    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.BUTTON_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(self.BUTTON_GPIO,
                              GPIO.BOTH,
                              callback=lambda x: self.button_callback(self.BUTTON_GPIO))

        #SI TUVIERAMOS UN LED PARA MOSTRAR QUE ESTA GRABANDO
        # GPIO.setup(LED_output, GPIO.OUT)

    def button_callback(self, numButton):
        if not GPIO.input(self.BUTTON_GPIO):
            print(f"Button pressed {str(numButton)}")
        else:
            print(f"Button released {str(numButton)}")
