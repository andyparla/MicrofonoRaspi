import telebot

class TelebotClass():
    # chatId_Bot = 1814801828 , -527590805
    TOKEN = "1856142691:AAFvGIIKkvPsrivlAnL9CRr272xJl-yKi80"  # Ponemos nuestro Token generado con el @BotFather

    def __init__(self):
        self.bot = telebot.TeleBot(self.TOKEN)

    def enviarTextoChat(self, chat_id:str, texto:str):
        self.bot.send_message(chat_id, texto)

    def getUltimoMensajeRecibido(self):
        actualizacion = self.bot.get_updates()
        mensaje = {
            "id": actualizacion.__getitem__(len(actualizacion)-1).message.message_id,
            "user_id":  actualizacion.__getitem__(len(actualizacion)-1).message.from_user.id,
            "user_name": actualizacion.__getitem__(len(actualizacion)-1).message.from_user.username,
            "chat_id": actualizacion.__getitem__(len(actualizacion)-1).message.chat.id,
            "text_message": actualizacion.__getitem__(len(actualizacion)-1).message.text,
        }
        print(actualizacion.__getitem__(0).message)
        return mensaje

    def enviarAudio(self, url):
        audio = open(url, 'rb')
        # audio = open('/home/andres/Documentos/proyectos/Python/MicrofonoRaspi/MicroInit/test1.wav', 'rb')
        self.bot.send_audio(-527590805, audio)

telebotVar = TelebotClass()
# telebotVar.enviarTextoChat('1814801828', "PRUEBA")
# print(telebotVar.getUltimoMensajeRecibido())
# telebotVar.enviarAudio()
