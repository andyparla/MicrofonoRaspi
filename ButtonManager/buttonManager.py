import RPi.GPIO as GPIO
from MicroInit.microfono import Microfono
from TeleBot.telegramBot import TelebotClass


class ButtonManager():
    BUTTON_GPIO = 4;  # PIN7 https://www.programoergosum.com/cursos-online/raspberry-pi/238-control-de-gpio-con-python-en-raspberry-pi/intermitente.
    microfonoClass = None
    telebotClass = None

    # LED_GRABACION = 17;  # LED INDICADOR DE GRABACION

    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.BUTTON_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(self.BUTTON_GPIO, GPIO.BOTH,
                              callback=lambda x: self.button_callback(self.BUTTON_GPIO), bouncetime=300)
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
            ficheroAudio = self.microfonoClass.pararGrabacion()
            self.telebotClass.enviarAudio(ficheroAudio)

    # def mainAction(self):
    #     try:
    #         print("Waiting for rising edge on port 24")
    #         GPIO.wait_for_edge(24, GPIO.RISING)
    #         print("Rising edge detected on port 24. Here endeth the third lesson.")
    #     except KeyboardInterrupt:
    #         GPIO.cleanup()  # clean up GPIO on CTRL+C exit
    #     GPIO.cleanup()


