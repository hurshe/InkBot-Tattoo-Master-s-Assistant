import os
from telegram.ext import ContextTypes


class TattooBot:
    def __init__(self):
        self.selected_data = []

    async def choise(selected_data: str, chat_id: int, context: ContextTypes.DEFAULT_TYPE):
        care_photo_path = os.path.join("media", "GC_05700.jpeg")
        how_much_photo_path = "C:\\Users\\rober\\DarkSoulTattoBot\\InkBot-Tattoo-Master-s-Assistant\\main\\media\\pricing.png"
        how_to_photo_path = "C:\\Users\\rober\\DarkSoulTattoBot\\InkBot-Tattoo-Master-s-Assistant\\main\\media\\maxresdefault.jpg"

        care_doc_path = ""
        how_to_doc_path = ""
        how_much_doc_path = ""

        if 'care' in selected_data:
            if "ENG" in selected_data:
                photo_path = care_photo_path
                await context.bot.send_photo(chat_id=chat_id, photo=open(photo_path, 'rb'))
                await context.bot.send_document(chat_id=chat_id,
                                                document=open(
                                                    'C:\\Users\\rober\\DarkSoulTattoBot\\InkBot-Tattoo-Master-s-Assistant\\main\\media\\Уход(ENG).pdf',
                                                    'rb'))
            elif "RU" in selected_data:
                photo_path = care_photo_path
                await context.bot.send_photo(chat_id=chat_id, photo=open(photo_path, 'rb'))
                await context.bot.send_document(chat_id=chat_id,
                                                document=open(
                                                    'C:\\Users\\rober\\DarkSoulTattoBot\\InkBot-Tattoo-Master-s-Assistant\\main\\media\\Уход(RU).pdf',
                                                    'rb'))
            elif "PL" in selected_data:
                photo_path = care_photo_path
                await context.bot.send_photo(chat_id=chat_id, photo=open(photo_path, 'rb'))
                await context.bot.send_document(chat_id=chat_id,
                                                document=open(
                                                    'C:\\Users\\rober\\DarkSoulTattoBot\\InkBot-Tattoo-Master-s-Assistant\\main\\media\\Уход(PL).pdf',
                                                    'rb'))

        elif 'how_to' in selected_data:
            if "ENG" in selected_data:
                photo_path = how_to_photo_path
                await context.bot.send_photo(chat_id=chat_id, photo=open(photo_path, 'rb'))
                await context.bot.send_document(chat_id=chat_id,
                                                document=open(
                                                    'C:\\Users\\rober\\DarkSoulTattoBot\\InkBot-Tattoo-Master-s-Assistant\\main\\media\\Уход(ENG).pdf',
                                                    'rb'))
            elif "RU" in selected_data:
                photo_path = how_to_photo_path
                await context.bot.send_photo(chat_id=chat_id, photo=open(photo_path, 'rb'))
                await context.bot.send_document(chat_id=chat_id,
                                                document=open(
                                                    'C:\\Users\\rober\\DarkSoulTattoBot\\InkBot-Tattoo-Master-s-Assistant\\main\\media\\Уход(ENG).pdf',
                                                    'rb'))
            elif "PL" in selected_data:
                photo_path = how_to_photo_path
                await context.bot.send_photo(chat_id=chat_id, photo=open(photo_path, 'rb'))
                await context.bot.send_document(chat_id=chat_id,
                                                document=open(
                                                    'C:\\Users\\rober\\DarkSoulTattoBot\\InkBot-Tattoo-Master-s-Assistant\\main\\media\\Уход(ENG).pdf',
                                                    'rb'))

        elif 'how_much' in selected_data:
            if "ENG" in selected_data:
                photo_path = how_much_photo_path
                await context.bot.send_photo(chat_id=chat_id, photo=open(photo_path, 'rb'))
                await context.bot.send_message(chat_id=chat_id, text='Price is good')
            elif "RU" in selected_data:
                photo_path = how_much_photo_path
                await context.bot.send_photo(chat_id=chat_id, photo=open(photo_path, 'rb'))
                await context.bot.send_document(chat_id=chat_id,
                                                document=open(
                                                    'C:\\Users\\rober\\DarkSoulTattoBot\\InkBot-Tattoo-Master-s-Assistant\\main\\media\\Уход(ENG).pdf',
                                                    'rb'))
            elif "PL" in selected_data:
                photo_path = how_much_photo_path
                await context.bot.send_photo(chat_id=chat_id, photo=open(photo_path, 'rb'))
                await context.bot.send_document(chat_id=chat_id,
                                                document=open(
                                                    'C:\\Users\\rober\\DarkSoulTattoBot\\InkBot-Tattoo-Master-s-Assistant\\main\\media\\Уход(ENG).pdf',
                                                    'rb'))

        else:
            if "ENG" in selected_data:
                photo_path = "C:\\Users\\rober\\DarkSoulTattoBot\\InkBot-Tattoo-Master-s-Assistant\\main\\media\\brat.jpg"
                await context.bot.send_photo(chat_id=chat_id, photo=open(photo_path, 'rb'))
                await context.bot.send_message(chat_id=chat_id, text='Finally it works! OMG .... >>>>>> YEAH <<<<<<')
            elif "RU" in selected_data:
                photo_path = "C:\\Users\\rober\\DarkSoulTattoBot\\InkBot-Tattoo-Master-s-Assistant\\main\\media\\brat.jpg"
                await context.bot.send_photo(chat_id=chat_id, photo=open(photo_path, 'rb'))
                await context.bot.send_message(chat_id=chat_id,
                                               text='Привет мой друг все работает и будет отлично порадую брата нащими успехами и заработаем миллионы вместе!')
            elif "PL" in selected_data:
                photo_path = "C:\\Users\\rober\\DarkSoulTattoBot\\InkBot-Tattoo-Master-s-Assistant\\main\\media\\brat.jpg"
                await context.bot.send_photo(chat_id=chat_id, photo=open(photo_path, 'rb'))
                await context.bot.send_message(chat_id=chat_id,
                                               text='Kurwa działa chujowstwo, kurwa ręka boli kurwaaaaaa auaaaa ....')

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

        await choise(selected_data, chat_id, context)