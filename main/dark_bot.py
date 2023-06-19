import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes, Application, CommandHandler, CallbackQueryHandler

from typing import Final
import dotenv

dotenv.load_dotenv()

TOKEN: Final = os.getenv("token")
BOT_USERNAME: Final = os.getenv("bot_username")

selected_data = []


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id

    russian_button = InlineKeyboardButton('🇷🇺 RU', callback_data='RU')
    english_button = InlineKeyboardButton('🇺🇲 ENG', callback_data="ENG")
    polish_button = InlineKeyboardButton('🇵🇱 PL', callback_data='PL')

    keyboard = InlineKeyboardMarkup([[russian_button, english_button, polish_button]])
    await context.bot.send_message(chat_id=chat_id, text="Выберите язык     Choose your language    Wybierz język:", reply_markup=keyboard)


async def start_command(selected_data: str, chat_id: int, context: ContextTypes.DEFAULT_TYPE):
    if 'care' in selected_data:
        if "ENG" in selected_data:
            photo_path = "C:\\Users\\rober\\OneDrive\\Робочий стіл\\GC_05700.jpeg"
            await context.bot.send_photo(chat_id=chat_id, photo=open(photo_path, 'rb'))
            await context.bot.send_document(chat_id=chat_id, document=open('C:\\Users\\rober\\OneDrive\\Робочий стіл\\Уход за тату.docx', 'rb'))
        elif "RU" in selected_data:
            photo_path = "C:\\Users\\rober\\OneDrive\\Робочий стіл\\GC_05700.jpeg"
            await context.bot.send_photo(chat_id=chat_id, photo=open(photo_path, 'rb'))
            await context.bot.send_document(chat_id=chat_id, document=open('C:\\Users\\rober\\OneDrive\\Робочий стіл\\Уход за тату.docx', 'rb'))
        elif "PL" in selected_data:
            photo_path = "C:\\Users\\rober\\OneDrive\\Робочий стіл\\GC_05700.jpeg"
            await context.bot.send_photo(chat_id=chat_id, photo=open(photo_path, 'rb'))
            await context.bot.send_document(chat_id=chat_id, document=open('C:\\Users\\rober\\OneDrive\\Робочий стіл\\Уход за тату.docx', 'rb'))

    elif 'how_to' in selected_data:
        if "ENG" in selected_data:
            photo_path = "C:\\Users\\rober\\OneDrive\\Робочий стіл\\maxresdefault.jpg"
            await context.bot.send_photo(chat_id=chat_id, photo=open(photo_path, 'rb'))
            await context.bot.send_document(chat_id=chat_id, document=open('C:\\Users\\rober\\OneDrive\\Робочий стіл\\Уход за тату.docx', 'rb'))
        elif "RU" in selected_data:
            photo_path = "C:\\Users\\rober\\OneDrive\\Робочий стіл\\maxresdefault.jpg"
            await context.bot.send_photo(chat_id=chat_id, photo=open(photo_path, 'rb'))
            await context.bot.send_document(chat_id=chat_id, document=open('C:\\Users\\rober\\OneDrive\\Робочий стіл\\Уход за тату.docx', 'rb'))
        elif "PL" in selected_data:
            photo_path = "C:\\Users\\rober\\OneDrive\\Робочий стіл\\maxresdefault.jpg"
            await context.bot.send_photo(chat_id=chat_id, photo=open(photo_path, 'rb'))
            await context.bot.send_document(chat_id=chat_id, document=open('C:\\Users\\rober\\OneDrive\\Робочий стіл\\Уход за тату.docx', 'rb'))

    elif 'how_much' in selected_data:
        if "ENG" in selected_data:
            photo_path = "C:\\Users\\rober\\OneDrive\\Робочий стіл\\pricing.png"
            await context.bot.send_photo(chat_id=chat_id, photo=open(photo_path, 'rb'))
            await context.bot.send_document(chat_id=chat_id, document=open('C:\\Users\\rober\\OneDrive\\Робочий стіл\\Уход за тату.docx', 'rb'))
        elif "RU" in selected_data:
            photo_path = "C:\\Users\\rober\\OneDrive\\Робочий стіл\\pricing.png"
            await context.bot.send_photo(chat_id=chat_id, photo=open(photo_path, 'rb'))
            await context.bot.send_document(chat_id=chat_id, document=open('C:\\Users\\rober\\OneDrive\\Робочий стіл\\Уход за тату.docx', 'rb'))
        elif "PL" in selected_data:
            photo_path = "C:\\Users\\rober\\OneDrive\\Робочий стіл\\pricing.png"
            await context.bot.send_photo(chat_id=chat_id, photo=open(photo_path, 'rb'))
            await context.bot.send_document(chat_id=chat_id, document=open('C:\\Users\\rober\\OneDrive\\Робочий стіл\\Уход за тату.docx', 'rb'))
    
    
    else:    
        if "ENG" in selected_data:
            photo_path = "C:\\Users\\rober\\OneDrive\\Робочий стіл\\brat.jpg"
            await context.bot.send_photo(chat_id=chat_id, photo=open(photo_path, 'rb'))
            await context.bot.send_message(chat_id=chat_id, text='Finally it works! OMG .... >>>>>> YEAH <<<<<<')
        elif "RU" in selected_data:
            photo_path = "C:\\Users\\rober\\OneDrive\\Робочий стіл\\brat.jpg"
            await context.bot.send_photo(chat_id=chat_id, photo=open(photo_path, 'rb'))
            await context.bot.send_message(chat_id=chat_id, text='Привет мой друг все работает и будет отлично порадую брата нащими успехами и заработаем миллионы вместе!')
        elif "PL" in selected_data:
            photo_path = "C:\\Users\\rober\\OneDrive\\Робочий стіл\\brat.jpg"
            await context.bot.send_photo(chat_id=chat_id, photo=open(photo_path, 'rb'))
            await context.bot.send_message(chat_id=chat_id, text='Kurwa działa chujowstwo, kurwa ręka boli kurwaaaaaa auaaaa ....')
    
    
async def button_click(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global selected_data
    query = update.callback_query
    new_element = query.data
    chat_id = query.message.chat_id
    if new_element == 'send_document':
        selected_data.append('send_document')

    if new_element == "ENG":
        if "PL" in selected_data:
            selected_data.remove('PL')
        elif 'RU' in selected_data:
            selected_data.remove('RU')
        elif "ENG" in selected_data:
            selected_data.remove('ENG')
        selected_data.append('ENG')
    elif new_element == "PL":
        if "ENG" in selected_data:
            selected_data.remove('ENG')
        elif 'RU' in selected_data:
            selected_data.remove('RU')
        elif 'PL' in selected_data:
            selected_data.remove('PL')
        selected_data.append("PL")
    elif new_element == "RU":
        if "ENG" in selected_data:
            selected_data.remove('ENG')
        elif 'PL' in selected_data:
            selected_data.remove('PL')
        elif 'RU' in selected_data:
            selected_data.remove('RU')
        selected_data.append("RU")

    if new_element == "care":                           
        if "how_to" in selected_data:
            selected_data.remove('how_to')
        elif 'how_much' in selected_data:
            selected_data.remove('how_much')
        elif 'care' in selected_data:
            selected_data.remove('care')
        selected_data.append("care")
    elif new_element == "how_to":
        if "care" in selected_data:
            selected_data.remove('care')
        elif 'how_much' in selected_data:
            selected_data.remove('how_much')
        elif "how_to" in selected_data:
            selected_data.remove('how_to')
        selected_data.append("how_to")
    elif new_element == "how_much":
        if "care" in selected_data:
            selected_data.remove('care')
        elif 'how_to' in selected_data:
            selected_data.remove('how_to')
        elif 'how_much' in selected_data:
            selected_data.remove('how_much')
        selected_data.append("how_much")
    print(selected_data)

    await start_command(selected_data, chat_id, context)


async def faq(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global selected_data 
    chat_id = update.effective_chat.id
    photo_path = "C:\\Users\\rober\\OneDrive\\Робочий стіл\\FAQ-picture.jpg"

    russian_how_to = InlineKeyboardButton('Подготовка к сеансу', callback_data='how_to')
    russian_care = InlineKeyboardButton('Уход за тату', callback_data='care')
    russian_how_much = InlineKeyboardButton('От чего зависит цена', callback_data='how_much')

    ru_keyboard = InlineKeyboardMarkup([[russian_how_to], [russian_care], [russian_how_much]])

    eng_how_to = InlineKeyboardButton('Preparation to session', callback_data='how_to')
    eng_care = InlineKeyboardButton('How care to youre tattoo', callback_data='care')
    eng_how_much = InlineKeyboardButton('Pricing', callback_data='how_much')

    eng_keyboard = InlineKeyboardMarkup([[eng_how_to],[eng_care],[eng_how_much]])

    pl_how_to = InlineKeyboardButton('Przygotowanie do sesji', callback_data='how_to')
    pl_care = InlineKeyboardButton('Pielęgacja tatuażu', callback_data='care')
    pl_how_much = InlineKeyboardButton('Cennik', callback_data='how_much')

    pl_keyboard = InlineKeyboardMarkup([[pl_how_to],[pl_care],[pl_how_much]])
    
    await context.bot.send_photo(chat_id=chat_id, photo=photo_path)

    if 'RU' in selected_data:
        await context.bot.send_message(chat_id=chat_id, text='Выбирите что вас интересует :', reply_markup=ru_keyboard)

    elif 'PL' in selected_data:
        await context.bot.send_message(chat_id=chat_id, text='Wybierz o czym chcesz wiedzieć :', reply_markup=pl_keyboard)
    elif 'ENG' in selected_data:
        await context.bot.send_message(chat_id=chat_id, text="Choise the option :", reply_markup=eng_keyboard)


async def kontakt_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global selected_data

    instagram_keyboard = [InlineKeyboardButton("Instagram", url='https://www.instagram.com/alexandr_darksoul/')]
    linkedin_keyboard = [InlineKeyboardButton('Facebook', url='https://www.facebook.com/AlexINKINK/')]
    keyboard = InlineKeyboardMarkup([instagram_keyboard, linkedin_keyboard])

    photo_path = "C:\\Users\\rober\\OneDrive\\Робочий стіл\\instagram.jpg"
    await context.bot.send_photo(chat_id = update.message.chat_id, photo=photo_path)

    if 'RU' in selected_data:
        await update.message.reply_text('Подписывайся что бы быть вкурсе всех событий', reply_markup=keyboard)

    elif 'ENG' in selected_data:
        await update.message.reply_text('Subscribe me for new informations.', reply_markup=keyboard)

    elif 'PL' in selected_data:
        await update.message.reply_text('Subscrybój mnie żeby dostawać najnowszą informację', reply_markup=keyboard)


async def location_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global selected_data

    if 'RU' in selected_data:
        await update.message.reply_text('Место расположения студии')

    elif 'ENG' in selected_data:
        await update.message.reply_text('Studio location')

    elif 'PL' in selected_data:
        await update.message.reply_text('Lokalizacja studio')

    chat_id = update.message.chat_id
    latitude = 52.222585202373146
    longitude = 21.09297611187889 
    await context.bot.send_location(chat_id=chat_id, latitude=latitude, longitude=longitude)
 

if __name__ == "__main__":
    print('Start polling...')
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler('start', start))
    app.add_handler(CallbackQueryHandler(button_click))
    app.add_handler(CommandHandler('kontakt', kontakt_command))
    app.add_handler(CommandHandler('location', location_command))
    app.add_handler(CommandHandler('faq', faq))
    print('Polling...')

    app.run_polling() 

