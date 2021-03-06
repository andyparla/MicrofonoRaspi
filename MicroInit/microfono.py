import pyaudio
import wave
import RPi.GPIO as GPIO

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


form_1 = pyaudio.paInt16 # 16-bit resolution
chans = 1 # 2 channel
samp_rate = 44100 # 44.1kHz sampling rate
chunk = 4096 # 2^12 samples for buffer
record_secs = 3 # seconds to record
dev_index = 0 # device index found by p.get_device_info_by_index(ii)
wav_output_filename = 'test1.wav' # name of .wav file


#GPIO pin setup for button
ledPin = 18
buttonPin = 23

audio = pyaudio.PyAudio()

# create pyaudio stream
stream = audio.open(format = form_1,
                    rate = samp_rate,
                    channels = chans,
                    input_device_index = dev_index,
                    input = True,
                    frames_per_buffer=chunk)

print("recording")
frames = []

# while GPIO.input(buttonPin) == False:
#     data = stream.read(chunk)
#     frames.append(data)
#     break

# loop through stream and append audio chunks to frame array
for ii in range(0, int((samp_rate/chunk)*record_secs)):
    data = stream.read(chunk)
    frames.append(data)

print("finished recording")

# stop the stream, close it, and terminate the pyaudio instantiation
stream.stop_stream()
stream.close()
audio.terminate()

# save the audio frames as .wav file
wavefile = wave.open(wav_output_filename,'wb')
wavefile.setnchannels(chans)
wavefile.setsampwidth(audio.get_sample_size(form_1))
wavefile.setframerate(samp_rate)
wavefile.writeframes(b''.join(frames))
wavefile.close()

