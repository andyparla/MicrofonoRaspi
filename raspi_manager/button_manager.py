from gpiozero import Button
from raspi_manager.microfono_manager import Microfono
from telegram_bot.telegram_bot import TelebotClass
import signal
import warnings
import sys


# GPIOZERO MANUAL https://gpiozero.readthedocs.io/en/stable/recipes.html

class ButtonManager():
    warnings.simplefilter('ignore')
    BUTTON_NIETO_A = None  # GPIOZERO USES: BCM --> PIN7 https://www.programoergosum.com/cursos-online/raspberry-pi
    # /238-control-de-gpio-con-python-en-raspberry-pi/intermitente.
    microfonoClass = None
    telebotClass = None
    button_map = {4: "NietoA", 6: "NietoB", 16: "NietoX", 24: "NietoY"}

    def __init__(self):
        # GPIO.setmode(GPIO.BCM)
        # GPIO.setup(self.BUTTON_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        # GPIO.add_event_detect(self.BUTTON_GPIO, GPIO.BOTH,
        #                       callback=lambda x: self.button_callback(self.BUTTON_GPIO), bouncetime=300)
        self.__configureBotones()
        self.microfonoClass = Microfono()
        self.telebotClass = TelebotClass()
        signal.pause()

    def __configureBotones(self):
        self.BUTTON_NIETO_A = Button(4)
        self.BUTTON_NIETO_A.when_pressed = lambda: self.button_callback(self.BUTTON_NIETO_A)
        self.BUTTON_NIETO_A.when_released = lambda: self.button_callback(self.BUTTON_NIETO_A)

    def button_callback(self, boton):
        nombreBoton = self.button_map[boton.pin.number]
        if boton.is_pressed:
            print(f"Boton pulsado {str(nombreBoton)}")
            self.microfonoClass.comenzar_grabacion()
        else:
            print(f"Boton liberado {str(nombreBoton)}")
            ficheroAudio = self.microfonoClass.parar_grabacion()
            self.telebotClass.enviar_audio(ficheroAudio)
            sys.exit(0)

            # try:
            #     button_a.when_pressed = pressed
            #     button_b.when_pressed = pressed
            #     button_x.when_pressed = pressed
            #     button_y.when_pressed = pressed
            #
            #     pause()
            #
            # except KeyboardInterrupt:
            #     button_a.close()
            #     button_b.close()
            #     button_x.close()
            #     button_y.close()
