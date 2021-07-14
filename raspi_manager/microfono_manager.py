import pyaudio
import wave
from datetime import datetime
import os
from utils.leer_properties import LeerProperty
import threading


class Microfono(threading.Thread):
    FORM_1 = pyaudio.paInt16  # 16-bit resolution
    CHANS = 1  # 2 channel
    SAMP_RATE = 44100  # 44.1kHz sampling rate
    CHUNK = 4096  # 2^12 samples for buffer
    DEV_INDEX = 0  # device index found by p.get_device_info_by_index(ii)
    FRAMES = []
    GRABAR_AUDIO = False
    WAV_OUTPUT_FILENAME = ""  # name of .wav file
    WAV_OUTPUT_FOLDER = ""
    audioObject = None
    stream = None

    def __init__(self):
        print("Inicializando clase Microfono")
        threading.Thread.__init__(self)

    def run(self):
        if self.audioObject is None and self.stream is None:
            self.audioObject = pyaudio.PyAudio()
            # create pyaudio stream
            self.stream = self.audioObject.open(format=self.FORM_1,
                                      rate=self.SAMP_RATE,
                                      channels=self.CHANS,
                                      input_device_index=self.DEV_INDEX,
                                      input=True,
                                      frames_per_buffer=self.CHUNK)
            self.comenzar_grabacion()


    def comenzar_grabacion(self):
        print("Grabando...")
        # loop through stream and append audio chunks to frame array
        self.GRABAR_AUDIO = True
        while self.GRABAR_AUDIO:
            data = self.stream.read(self.CHUNK, exception_on_overflow=False)
            self.FRAMES.append(data)

    def parar_grabacion(self, button_name):
        print("Fin grabación.")
        self.GRABAR_AUDIO = False
        # stop the stream, close it, and terminate the pyaudio instantiation
        self.stream.stop_stream()
        self.stream.close()
        self.audioObject.terminate()
        fichero_audio = self.__generar_ruta_audio(button_name) + "/" + \
                        button_name + "_" + datetime.now().strftime("%d-%b-%Y_%H:%M:%S.%f") + ".wav"
        self.__guardar_audio(fichero_audio)
        return fichero_audio

    def __guardar_audio(self, fichero_audio):
        print("Guardando audio...")
        # save the audio frames as .wav file

        print(f"Audio almacenado: {fichero_audio}")
        wavefile = wave.open(fichero_audio, 'wb')
        wavefile.setnchannels(self.CHANS)
        wavefile.setsampwidth(self.audioObject.get_sample_size(self.FORM_1))
        wavefile.setframerate(self.SAMP_RATE)
        wavefile.writeframes(b''.join(self.FRAMES))
        wavefile.close()
        print("Audio guardado.")

    def __generar_ruta_audio(self, name):
        ruta_audio = LeerProperty.get_property_value("ruta.fichero.audio") + "/" + name
        if not os.path.exists(ruta_audio):
            os.makedirs(ruta_audio)
        return ruta_audio

# microfonoClass = Microfono()
# try:
#     microfonoClass.comenzarGrabacion()
# except KeyboardInterrupt:
#     microfonoClass.pararGrabacion()
#     microfonoClass.guardarAudio("boton1")
