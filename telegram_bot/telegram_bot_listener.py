import telebot


# Este listener se ejecutaria y quedaria en escucha con el comnado screen python telegram_bot_listener.py
class TelebotListener():
    # chatId_Bot = 1814801828 , -527590805
    TOKEN = "1856142691:AAFvGIIKkvPsrivlAnL9CRr272xJl-yKi80"  # Ponemos nuestro Token generado con el @BotFather
    bot = telebot.TeleBot(TOKEN)

    def __init__(self):
        self.bot.set_update_listener(self.listener)  # función escuchadora nuestra función 'listener' declarada arriba.

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

    # filter on a specific message
    @bot.message_handler(func=lambda message: message.text == "hola")
    def command_text_hi(self, m):
        self.bot.send_message(m.chat.id, "I love you too!")

    @bot.message_handler(commands=['start'])
    def send_welcome(self, m):
        self.bot.send_message(m.chat.id, 'Bienvenido!')

    @bot.message_handler(func=lambda message: True, content_types=['text'])
    def command_default(self, m):
        # this is the standard reply to a normal message
        self.bot.send_message(m.chat.id, "I don't understand, try with /help")


# telebotVar = TelebotListener()
