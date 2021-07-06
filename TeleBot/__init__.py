"""
DIFERENTES ACCIONES A REALIZAR CON EL BOT:


###################### Enviar una simple foto: ######################
photo = open('/home/lordsergio/Gatito_Feliz.jpg', 'rb')
tb.send_photo(chat_id, photo)
#########################################

###################### Enviar un documento PDF: ######################
doc = open('/home/lordsergio/Documentos/deberes_de_verano.pdf', 'rb') # Es la función equivalente a enviar un archivo desde telegram.
tb.send_document(chat_id, doc)
tb.send_message(109556849, 'Disfruta de tu verano ;)')
#########################################

###################### Enviar un Vídeo: ######################
video = open('/home/lordsergio/Vídeos/Reportaje_sobre_UNIX.mp4', 'rb')
tb.send_video(chat_id, video)
#########################################

###################### Enviar un Audio: ######################
audio = open('/home/lordsergio/Música/Audios/1.ogg', 'rb')
tb.send_audio(chat_id, audio) # No tengo muy claro si lo enviá como una nota de audio o como cuando enviar una canción desde Telegram :(
#########################################

###################### Enviar un Sticker: ######################
sti = open('/tmp/sti.webp', 'rb')
tb.send_sticker(chat_id, sti)
#########################################

###################### Enviar una Localización: ######################
tb.send_location(chat_id, latitud, longitud)
#########################################

###################### Reenviar un mensaje (Cualquier tipo de mensaje): ######################
tb.forward_message(to_chat_id, from_chat_id, message_id)
#########################################

###################### Enviar acciones de chat: ######################
tb.send_chat_action(chat_id, action_string)
# Están disponibles todas estas acciones:
 * typing,
 * upload_photo,
 * record_video,
 * upload_video,
 * record_audio,
 * upload_audio,
 * upload_document,
 * find_location
#########################################

###################### Obtener Actualizaciones: ######################
tb.get_update()
#########################################

###################### Crear un teclado de acciones: ######################
from telebot import types

markup = types.ReplyKeyboardMarkup()
markup.add('a', 'v', 'd')
tb.send_message(chat_id, message, None, None, markup)
# or use row method
markup = types.ReplyKeyboardMarkup()
markup.row('a', 'v')
markup.row('c', 'd', 'e')
tb.send_message(chat_id, message, None, None, markup)
#########################################

###################### Probar si funciona la API: ######################
tb.get_me()
#########################################
"""