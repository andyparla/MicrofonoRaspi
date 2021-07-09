import telebot
from utils.utils_encrypt import UtilsEncrypt
from utils.leer_properties import LeerProperty


class TelebotClass():
    # chatId_Bot = 1814801828 , -527590805
    def __init__(self):
        utilDecript = UtilsEncrypt(LeerProperty.get_property_value("api.telegram.key").encode("utf-8"))
        data = utilDecript.decrypt_data(LeerProperty.get_property_value("api.telegram.token").encode("utf-8"))
        self.bot = telebot.TeleBot(data)

    def enviar_texto_chat(self, chat_id: str, texto: str):
        self.bot.send_message(chat_id, texto)

    def get_ultimo_mensaje_recibido(self):
        actualizacion = self.bot.get_updates()
        mensaje = {
            "id": actualizacion.__getitem__(len(actualizacion) - 1).message.message_id,
            "user_id": actualizacion.__getitem__(len(actualizacion) - 1).message.from_user.id,
            "user_name": actualizacion.__getitem__(len(actualizacion) - 1).message.from_user.username,
            "chat_id": actualizacion.__getitem__(len(actualizacion) - 1).message.chat.id,
            "text_message": actualizacion.__getitem__(len(actualizacion) - 1).message.text,
        }
        print(actualizacion.__getitem__(0).message)
        return mensaje

    def enviar_audio(self, url):
        audio = open(url, 'rb')
        # audio = open('/home/andres/Documentos/proyectos/Python/MicrofonoRaspi/microfono_manager/test1.wav', 'rb')
        self.bot.send_audio(-527590805, audio)

# telebotVar = TelebotClass()
# telebotVar.enviarTextoChat('1814801828', "PRUEBA")
# print(telebotVar.getUltimoMensajeRecibido())
# telebotVar.enviarAudio()
