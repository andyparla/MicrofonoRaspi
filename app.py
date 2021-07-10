from raspi_manager.button_manager import ButtonManager
from telegram_bot.telegram_bot_listener import TelebotListener

if __name__ == "__main__":
    manejador_botones = ButtonManager()
    TelebotListener()

