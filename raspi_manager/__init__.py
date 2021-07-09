
# INSTALACION PYAUDIO
# sudo apt-get install libasound-dev portaudio19-dev libportaudio2 libportaudiocpp0
# sudo apt-get install ffmpeg libav-tools
# sudo pip install pyaudio
# PARA INSTALAR PYAUDIO EN WINDOWS: DESCARGAR EL .WHL ACORDE A LA VERSION PYTHON DESDE AQUI
# https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio

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
