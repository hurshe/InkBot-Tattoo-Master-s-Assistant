import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from user_data_handler import selected_data

selected_data = selected_data


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    selected_data.clear()
    chat_id = update.effective_chat.id
    russian_button = InlineKeyboardButton('🇺🇦 RU', callback_data='RU')
    english_button = InlineKeyboardButton('🇺🇲 ENG', callback_data="ENG")
    polish_button = InlineKeyboardButton('🇵🇱 PL', callback_data='PL')

    keyboard = InlineKeyboardMarkup([[russian_button, english_button, polish_button]])
    await context.bot.send_message(chat_id=chat_id, text="Выберите язык     Choose your language    Wybierz język:", reply_markup=keyboard)


async def kontakt_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global selected_data

    instagram_keyboard = [InlineKeyboardButton("Instagram", url='https://www.instagram.com/alexandr_darksoul/')]
    linkedin_keyboard = [InlineKeyboardButton('Facebook', url='https://www.facebook.com/AlexINKINK/')]
    keyboard = InlineKeyboardMarkup([instagram_keyboard, linkedin_keyboard])

    photo_path = os.path.join(os.path.dirname(__file__), "media", "instagram.jpg")
    await context.bot.send_photo(chat_id = update.message.chat_id, photo=photo_path)

    if 'RU' in selected_data:
        await update.message.reply_text("🔥Подписывайся что бы быть вкурсе всех событий🔥", reply_markup=keyboard)

    elif 'ENG' in selected_data:
        await update.message.reply_text("🔥Subscribe to stay informed about all events🔥", reply_markup=keyboard)

    elif 'PL' in selected_data:
        await update.message.reply_text("🔥Subskrybuj, aby być na bieżąco ze wszystkimi wydarzeniami🔥", reply_markup=keyboard)


async def faq_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global selected_data
    chat_id = update.effective_chat.id
    photo_path = os.path.join(os.path.dirname(__file__), "media/FAQ", "FAQ-picture.jpg")

    russian_how_to = InlineKeyboardButton('Подготовка к сеансу', callback_data='how_to')
    russian_care = InlineKeyboardButton('Уход за тату', callback_data='care')
    russian_how_much = InlineKeyboardButton('От чего зависит цена', callback_data='how_much')

    ru_keyboard = InlineKeyboardMarkup([[russian_how_to], [russian_care], [russian_how_much]])

    eng_how_to = InlineKeyboardButton(' Preparation to session ', callback_data='how_to')
    eng_care = InlineKeyboardButton(' How care to youre tattoo ', callback_data='care')
    eng_how_much = InlineKeyboardButton('Pricing', callback_data='how_much')

    eng_keyboard = InlineKeyboardMarkup([[eng_how_to], [eng_care], [eng_how_much]])

    pl_how_to = InlineKeyboardButton('Przygotowanie do sesji ', callback_data='how_to')
    pl_care = InlineKeyboardButton('Pielęgacja tatuażu ', callback_data='care')
    pl_how_much = InlineKeyboardButton('Cennik ', callback_data='how_much')

    pl_keyboard = InlineKeyboardMarkup([[pl_how_to], [pl_care], [pl_how_much]])

    await context.bot.send_photo(chat_id=chat_id, photo=photo_path)

    if 'RU' in selected_data:
        await context.bot.send_message(chat_id=chat_id, text='Выбирите что вас интересует :', reply_markup=ru_keyboard)

    elif 'PL' in selected_data:
        await context.bot.send_message(chat_id=chat_id, text='Wybierz o czym chcesz wiedzieć :', reply_markup=pl_keyboard)
    elif 'ENG' in selected_data:
        await context.bot.send_message(chat_id=chat_id, text="Choise the option :", reply_markup=eng_keyboard)


async def location_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global selected_data

    if 'RU' in selected_data:
        await update.message.reply_text('📍 Место расположения студии: Wojciecha Górskiego 4, Warszawa 🪂')

    elif 'ENG' in selected_data:
        await update.message.reply_text('📍 Studio location, Wojciecha Górskiego 4, Warszawa 🪂')

    elif 'PL' in selected_data:
        await update.message.reply_text('📍 Lokalizacja studio, Wojciecha Górskiego 4, Warszawa 🪂')

    chat_id = update.message.chat_id
    latitude, longitude = 52.2343483586397, 21.016758841301986
    await context.bot.send_location(chat_id=chat_id, latitude=latitude, longitude=longitude)
