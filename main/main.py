import os
import dotenv
import logging
from typing import Final

from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ConversationHandler, MessageHandler, filters
from telegram import Update

from user_data_handler import button_click
from commands import start_command, kontakt_command, location_command, faq_command
from pdf_generator import generic_pdf
from conversation import ask_question, cancel, QUESTION, user_answers

dotenv.load_dotenv()

TOKEN: Final = os.getenv("token")
BOT_USERNAME: Final = os.getenv("bot_username")


logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logging.getLogger("httpx").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)


conv_handler = ConversationHandler(
        entry_points=[CommandHandler('conversation', ask_question)],
        states={
            QUESTION: [MessageHandler(filters.TEXT & ~filters.COMMAND, ask_question)],
        },
        fallbacks=[CommandHandler('cancel', cancel)]
    )


if __name__ == "__main__":
    print('Start polling...')
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CallbackQueryHandler(button_click))
    app.add_handler(CommandHandler('kontakt', kontakt_command))
    app.add_handler(CommandHandler('location', location_command))
    app.add_handler(CommandHandler('faq', faq_command))
    print('Polling...')

    app.run_polling(allowed_updates=Update.ALL_TYPES)
    print("After polling:", user_answers)




