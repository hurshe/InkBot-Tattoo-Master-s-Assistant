import os
import dotenv
from typing import Final
from telegram.ext import Application, CommandHandler, CallbackQueryHandler
from user_data_handler import button_click
from commands import start_command, kontakt_command, location_command, faq_command


dotenv.load_dotenv()

TOKEN: Final = os.getenv("token")
BOT_USERNAME: Final = os.getenv("bot_username")


if __name__ == "__main__":
    print('Start polling...')
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CallbackQueryHandler(button_click))
    app.add_handler(CommandHandler('kontakt', kontakt_command))
    app.add_handler(CommandHandler('location', location_command))
    app.add_handler(CommandHandler('faq', faq_command))
    print('Polling...')

    app.run_polling()

