import pyaudio
import wave
from datetime import datetime
import os
from utils.leer_properties import LeerProperty
import threading


class Microfono(threading.Thread):
    FORM_1 = pyaudio.paInt16  # 16-bit resolution
    CHANS = 1  # 2 channel
    SAMP_RATE = 48000  # 44.1kHz sampling rate
    CHUNK = 4096  # 2^12 samples for buffer
    DEV_INDEX = 0  # device index found by p.get_device_info_by_index(ii)

    WAV_OUTPUT_FILENAME = ""  # name of .wav file
    WAV_OUTPUT_FOLDER = ""
    GRABAR_AUDIO = False
    NOMBRE_BOTON = None

    # FRAMES = []

    def __init__(self):
        self.audioObject = pyaudio.PyAudio()
        self.stream = self.audioObject.open(format=self.FORM_1,
                                            rate=self.SAMP_RATE,
                                            channels=self.CHANS,
                                            input_device_index=self.DEV_INDEX,
                                            input=True,
                                            frames_per_buffer=self.CHUNK)
        self.frames = []
        print("Inicializando clase Microfono")
        # threading.Thread.__init__(self)

    # def run(self):
    #
    #     print("Grabando...")
    #     while True:
    #         data = self.stream.read(self.CHUNK, exception_on_overflow=False)
    #         self.frames.append(data)
    #         if self.GRABAR_AUDIO:
    #             print("parado")
    #             break
    #     self.parar_grabacion(self.NOMBRE_BOTON)

    def comenzar_grabacion(self):
        print("Grabando...")
        while True:
            data = self.stream.read(self.CHUNK, exception_on_overflow=False)
            self.frames.append(data)
            if self.GRABAR_AUDIO:
                print("parado")
                break
        self.parar_grabacion(self.NOMBRE_BOTON)

    def parar_grabacion(self, button_name):
        print("Fin grabación.")
        # stop the stream, close it, and terminate the pyaudio instantiation
        self.stream.stop_stream()
        self.stream.close()
        self.audioObject.terminate()
        self.fichero_audio = self.__generar_ruta_audio(button_name) + "/" + \
                             button_name + "_" + datetime.now().strftime("%d-%b-%Y_%H:%M:%S.%f") + ".wav"
        self.__guardar_audio(self.fichero_audio)

    def obtener_ruta_audio(self):
        return self.fichero_audio

    def __guardar_audio(self, fichero_audio):
        print("Guardando audio...")
        # save the audio frames as .wav file

        print(f"Audio almacenado: {fichero_audio}")
        wavefile = wave.open(fichero_audio, 'wb')
        wavefile.setnchannels(self.CHANS)
        wavefile.setsampwidth(self.audioObject.get_sample_size(self.FORM_1))
        wavefile.setframerate(self.SAMP_RATE)
        wavefile.writeframes(b''.join(self.frames))
        wavefile.close()
        print("Audio guardado.")

    def __generar_ruta_audio(self, name):
        ruta_audio = LeerProperty.get_property_value("ruta.fichero.audio") + "/" + name
        if not os.path.exists(ruta_audio):
            os.makedirs(ruta_audio)
        return ruta_audio
