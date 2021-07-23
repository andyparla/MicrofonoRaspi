from gpiozero import Button
from raspi_manager.microfono_manager import Microfono
from telegram_bot.telegram_bot import TelebotClass
import signal
import warnings
from time import sleep


# GPIOZERO MANUAL https://gpiozero.readthedocs.io/en/stable/recipes.html

class ButtonManager():
    warnings.simplefilter('ignore')
    # GPIOZERO USES: BCM --> PIN7 https://www.programoergosum.com/cursos-online/raspberry-pi
    # /238-control-de-gpio-con-python-en-raspberry-pi/intermitente.
    BUTTON_NIETO_A = None
    BUTTON_SALIDA = None
    microfono_start_audio = None
    microfono_pause_audio = None
    telebotClass = None
    button_map = {4: "NietoA", 14: "Salida"}

    def __init__(self):
        # GPIO.setmode(GPIO.BCM)
        # GPIO.setup(self.BUTTON_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        # GPIO.add_event_detect(self.BUTTON_GPIO, GPIO.BOTH,
        #                       callback=lambda x: self.button_callback(self.BUTTON_GPIO), bouncetime=300)
        self.microfono_start_audio = Microfono(True)
        self.microfono_pause_audio = Microfono(False)
        self.telebotClass = TelebotClass()
        self.__configureBotones()
        try:
            print("En pausa, esperando acción...")
            signal.pause()
        except KeyboardInterrupt:
            print("Saliendo.")

    def __configureBotones(self):
        # for boton_key in self.button_map:
        #     Button(boton_key).when_pressed = lambda: self.button_callback()
        print("Configurando botonera GPIO")
        self.BUTTON_NIETO_A = Button(4)
        self.BUTTON_SALIDA = Button(14)
        self.BUTTON_NIETO_A.when_held = lambda: self.button_callback(self.BUTTON_NIETO_A)
        self.BUTTON_NIETO_A.when_released  = lambda: self.button_callback_release(self.BUTTON_NIETO_A)
        print("FIN de la configuracion GPIO")

    def button_callback(self, boton):
        nombre_boton = self.button_map[boton.pin.number]
        if nombre_boton != "Salida":
            print(f"Boton pulsado {str(boton.pin.number)}")
            self.microfono_start_audio.start()


    def button_callback_release(self, boton):
        nombre_boton = self.button_map[boton.pin.number]
        if nombre_boton != "Salida":
            print(f"Boton liberado {str(boton.pin.number)}")
            fichero_audio = self.microfono_start_audio.start().parar_grabacion(nombre_boton)
            self.telebotClass.enviar_audio(fichero_audio)
