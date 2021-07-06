import RPi.GPIO as GPIO
import signal
import sys
from MicroInit.microfono import Microfono
from TeleBot.telegramBot import TelebotClass


class ButtonManager():
    BUTTON_GPIO = 4;  # Boton1 para grabar.
    microfonoClass = None
    telebotClass = None

    # LED_GRABACION = 17;  # LED INDICADOR DE GRABACION

    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.BUTTON_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(self.BUTTON_GPIO,
                              GPIO.BOTH,
                              callback=lambda x: self.button_callback(self.BUTTON_GPIO))
        self.microfonoClass = Microfono()
        self.telebotClass = TelebotClass()

        # SI TUVIERAMOS UN LED PARA MOSTRAR QUE ESTA GRABANDO
        # GPIO.setup(self.LED_GRABACION, GPIO.OUT)

    def button_callback(self, num_button):
        if not GPIO.input(self.BUTTON_GPIO):
            print(f"Boton pulsado {str(num_button)}")
            self.microfonoClass.comenzarGrabacion()
        else:
            print(f"Boton liberado {str(num_button)}")
            self.microfonoClass.pararGrabacion()#Deberia devolvernos la ruta del fichero guardado
            self.telebotClass.enviarAudio('/home/pi/proyectos/MicrofonoRaspi/MicroInit/test1.wav')
