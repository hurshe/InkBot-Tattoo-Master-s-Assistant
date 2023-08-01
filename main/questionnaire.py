import docx
from telegram import Update
from telegram.ext import ContextTypes, CallbackContext, ConversationHandler

async def save_data_to_word_file(user_data):
    doc = docx

    # Добавление данных анкеты в документ Word
    doc.heading('Анкета', level=1)
    doc.paragraph(f'Пол: {user_data["gender"]}')
    doc.paragraph(f'Возраст: {user_data["age"]}')
    doc.paragraph(f'Город: {user_data["city"]}')
    doc.paragraph(f'Алергии: {user_data["alergy"]}')

    # Сохранение документа в файл
    await doc.savedocx('anketa.docx')
    

async def collect_city(update: Update, context: CallbackContext):
    chat_id = update.effective_message.chat_id

    # Завершение сбора данных
    save_data_to_word_file(context.user_data)
    await update.message.reply_text('Спасибо за заполнение анкеты! Ваши данные были сохранены в файле.')
    doc_path = "C:\\Users\\rober\\DarkSoulTattoBot\\anketa.docx"
    await update.message.reply_document(chat_id=chat_id ,document=doc_path)

    # Завершение разговора
    ConversationHandler.END