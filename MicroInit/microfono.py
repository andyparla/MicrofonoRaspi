import pyaudio
import wave
import time

class Microfono():

    FORM_1 = pyaudio.paInt16  # 16-bit resolution
    CHANS = 1  # 2 channel
    SAMP_RATE = 44100  # 44.1kHz sampling rate
    CHUNK = 4096  # 2^12 samples for buffer
    RECORD_SECS = 3  # seconds to record
    DEV_INDEX = 0  # device index found by p.get_device_info_by_index(ii)
    WAV_OUTPUT_FILENAME = 'test1.wav'  # name of .wav file
    FRAMES = []
    GRABAR_AUDIO = False

    def __init__(self):
        print("Inicializando clase")
        self.audio = pyaudio.PyAudio()
        # create pyaudio stream
        self.stream = self.audio.open(format=self.FORM_1,
                                      rate=self.SAMP_RATE,
                                      channels=self.CHANS,
                                      input_device_index=self.DEV_INDEX,
                                      input=True,
                                      frames_per_buffer=self.CHUNK)

    def comenzarGrabacion(self):
        print("Grabando...")
        # loop through stream and append audio chunks to frame array
        self.GRABAR_AUDIO = True
        while self.GRABAR_AUDIO:
            data = self.stream.read(self.CHUNK, exception_on_overflow = False)
            self.FRAMES.append(data)
        # for ii in range(0, int((self.SAMP_RATE / self.CHUNK) * self.RECORD_SECS)):
        #     data = self.stream.read(self.CHUNK)
        #     self.FRAMES.append(data)

    def pararGrabacion(self):
        print("Fin grabación.")
        self.GRABAR_AUDIO = False
        # stop the stream, close it, and terminate the pyaudio instantiation
        self.stream.stop_stream()
        self.stream.close()
        self.audio.terminate()

    def guardarAudio(self):
        print("Guardando audio...")
        # save the audio frames as .wav file
        wavefile = wave.open(self.WAV_OUTPUT_FILENAME, 'wb')
        wavefile.setnchannels(self.CHANS)
        wavefile.setsampwidth(self.audio.get_sample_size(self.FORM_1))
        wavefile.setframerate(self.SAMP_RATE)
        wavefile.writeframes(b''.join(self.FRAMES))
        wavefile.close()
        print("Audio guardado.")


microfonoClass = Microfono()
try:
    microfonoClass.comenzarGrabacion()
except KeyboardInterrupt:
    microfonoClass.pararGrabacion()
    microfonoClass.guardarAudio()

