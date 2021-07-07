import telebot

class TelebotClass():
    # chatId_Bot = 1814801828 , -527590805
    TOKEN = "1856142691:AAFvGIIKkvPsrivlAnL9CRr272xJl-yKi80"  # Ponemos nuestro Token generado con el @BotFather

    def __init__(self):
        self.bot = telebot.TeleBot(self.TOKEN)
        self.bot.set_update_listener(self.listener)  # función escuchadora nuestra función 'listener' declarada arriba.

    def enviarTextoChat(self, chat_id:str, texto:str):
        self.bot.send_message(chat_id, texto)
        self.bot.message_handlers.u

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

    def getQuienSoy(self):
        return self.bot.get_me()

    def enviarAudio(self, url):
        audio = open(url, 'rb')
        # audio = open('/home/andres/Documentos/proyectos/Python/MicrofonoRaspi/MicroInit/test1.wav', 'rb')
        self.bot.send_audio(-527590805, audio)

    # Listener, estamos definiendo una función llamada 'listener', que recibe como parámetro un dato llamado 'messages'.
    def listener(self, messages):
        for mssg in messages:
            # El Cid es el identificador del chat los negativos son grupos y positivos los usuarios
            cid = mssg.chat.id
            if cid > 0:
                # Si 'cid' es positivo, usaremos 'mssg.chat.first_name' para el nombre.
                mensaje = str(mssg.chat.first_name) + " [" + str(cid) + "]: " + mssg.text
            else:
                # Si 'cid' es negativo, usaremos 'mssg.from_user.first_name' para el nombre.
                mensaje = str(mssg.from_user.first_name) + "[" + str(cid) + "]: " + mssg.text

        print(mensaje)  # Imprimimos el mensaje en la terminal, que nunca viene mal :)




telebotVar = TelebotClass()
# telebotVar.enviarTextoChat('1814801828', "PRUEBA")
# print(telebotVar.getUltimoMensajeRecibido())
telebotVar.enviarAudio()
