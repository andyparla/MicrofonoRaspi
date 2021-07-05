import pyaudio
import wave

# INSTALACION PYAUDIO
# sudo apt-get install libasound-dev portaudio19-dev libportaudio2 libportaudiocpp0
# sudo apt-get install ffmpeg libav-tools
# sudo pip install pyaudio

# INSTALACION GPIO:
# export CFLAGS=-fcommon
# pip3 install RPi.GPIO

# COMO SACAR EL DEVICE ID DEL MICROFONO USB
# sudo arecord --list-devices
#### RETORNA LO SIGUIENTE, VER device 0: USB xxx ####
"""
**** List of CAPTURE Hardware Devices ****
card 1: headset [Sennheiser USB headset], device 0: USB Audio [USB Audio]
  Subdevices: 1/1
  Subdevice #0: subdevice #0
"""
# SACAR DISPOSITIVOS DE AUDIO
"""
import pyaudio
p = pyaudio.PyAudio()
for ii in range (p.get_device_count()):
	print(p.get_device_info_by_index(ii).get("name"))
"""
FORM_1 = pyaudio.paInt16  # 16-bit resolution
CHANS = 1  # 2 channel
SAMP_RATE = 44100  # 44.1kHz sampling rate
CHUNK = 4096  # 2^12 samples for buffer
RECORD_SECS = 3  # seconds to record
DEV_INDEX = 0  # device index found by p.get_device_info_by_index(ii)
WAV_OUTPUT_FILENAME = 'test1.wav'  # name of .wav file


class Microfono():

    def __init__(self):
        print("Inicializando clase")
        self.audio = pyaudio.PyAudio()
        # create pyaudio stream
        self.stream = self.audio.open(format=FORM_1,
                                      rate=SAMP_RATE,
                                      channels=CHANS,
                                      input_device_index=DEV_INDEX,
                                      input=True,
                                      frames_per_buffer=CHUNK)

    def comenzarGrabacion(self):
        print("Grabando...")

        self.frames = []
        # loop through stream and append audio chunks to frame array
        data = self.stream.read(CHUNK)
        self.frames.append(data)

    def pararGrabacion(self):
        print("Fin grabación.")
        # stop the stream, close it, and terminate the pyaudio instantiation
        self.stream.stop_stream()
        self.stream.close()
        self.audio.terminate()

    def guardarAudio(self):
        # save the audio frames as .wav file
        wavefile = wave.open(WAV_OUTPUT_FILENAME, 'wb')
        wavefile.setnchannels(CHANS)
        wavefile.setsampwidth(self.audio.get_sample_size(FORM_1))
        wavefile.setframerate(SAMP_RATE)
        wavefile.writeframes(b''.join(self.frames))
        wavefile.close()

microfonoClass = Microfono()
microfonoClass.comenzarGrabacion()
microfonoClass.pararGrabacion()
microfonoClass.guardarAudio()