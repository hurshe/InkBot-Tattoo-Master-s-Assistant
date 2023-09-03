import os
from telegram.ext import ContextTypes
from telegram import Update
from telegram import InlineKeyboardButton, InlineKeyboardMarkup


selected_data = []


async def data_controller(selected_data: str, chat_id: int, context, update):
    care_image_path = os.path.join(os.path.dirname(__file__), "media", "GC_05700.jpeg")
    how_much_image_path = os.path.join(os.path.dirname(__file__), "media", "pricing.png")
    how_to_image_path = os.path.join(os.path.dirname(__file__), "media", "maxresdefault.jpg")

    info_cost_tattoo_image1 = os.path.join(os.path.dirname(__file__), "media/FAQ/FAQ - pricing", "length.jpg")
    info_cost_tattoo_image2 = os.path.join(os.path.dirname(__file__), "media/FAQ/FAQ - pricing", "details.jpg")
    info_cost_tattoo_image3 = os.path.join(os.path.dirname(__file__), "media/FAQ/FAQ - pricing", "body.jpg")
    info_cost_tattoo_image4 = os.path.join(os.path.dirname(__file__), "media/FAQ/FAQ - pricing", "color.jpg")
    info_cost_tattoo_image5 = os.path.join(os.path.dirname(__file__), "media/FAQ/FAQ - pricing", "pain.jpg")

    how_care_doc_path_ru = os.path.join(os.path.dirname(__file__), "media/FAQ", "How_to_care(RU).pdf")
    how_care_doc_path_eng = os.path.join(os.path.dirname(__file__), "media/FAQ", "How_to_care(ENG).pdf")
    how_care_doc_path_pl = os.path.join(os.path.dirname(__file__), "media/FAQ", "How_to_care(PL).pdf")

    how_prepare_doc_path_ru = os.path.join(os.path.dirname(__file__), "media/FAQ", "How_to_care(RU).pdf")
    how_prepare_doc_path_eng = os.path.join(os.path.dirname(__file__), "media/FAQ", "How_to_care(ENG).pdf")
    how_prepare_doc_path_pl = os.path.join(os.path.dirname(__file__), "media/FAQ", "How_to_care(PL).pdf")

    if 'care' in selected_data:
        del selected_data[1]
        if "ENG" in selected_data:
            photo_path = care_image_path
            await context.bot.send_photo(chat_id=chat_id, photo=open(photo_path, 'rb'))
            await context.bot.send_document(chat_id=chat_id, document=open(how_care_doc_path_eng, 'rb'))

        elif "RU" in selected_data:
            photo_path = care_image_path
            await context.bot.send_photo(chat_id=chat_id, photo=open(photo_path, 'rb'))
            await context.bot.send_document(chat_id=chat_id, document=open(how_care_doc_path_ru, 'rb'))

        elif "PL" in selected_data:
            photo_path = care_image_path
            await context.bot.send_photo(chat_id=chat_id, photo=open(photo_path, 'rb'))
            await context.bot.send_document(chat_id=chat_id, document=open(how_care_doc_path_pl, 'rb'))

    elif 'how_to' in selected_data:
        del selected_data[1]
        if "ENG" in selected_data:
            photo_path = how_to_image_path
            await context.bot.send_photo(chat_id=chat_id, photo=open(photo_path, 'rb'))
            await context.bot.send_document(chat_id=chat_id, document=open(how_prepare_doc_path_eng, 'rb'))

        elif "RU" in selected_data:
            photo_path = how_to_image_path
            await context.bot.send_photo(chat_id=chat_id, photo=open(photo_path, 'rb'))
            await context.bot.send_document(chat_id=chat_id, document=open(how_prepare_doc_path_ru, 'rb'))

        elif "PL" in selected_data:
            photo_path = how_to_image_path
            await context.bot.send_photo(chat_id=chat_id, photo=open(photo_path, 'rb'))
            await context.bot.send_document(chat_id=chat_id, document=open(how_prepare_doc_path_pl, 'rb'))

    elif 'how_much' in selected_data:
        del selected_data[1]
        if "ENG" in selected_data:
            await context.bot.send_photo(chat_id=chat_id, photo=open(how_much_image_path, 'rb'))
            await context.bot.send_message(chat_id=chat_id, text='Pricing factors:')
            await context.bot.send_message(chat_id=chat_id, text='1) Size of tattoo')
            await context.bot.send_photo(chat_id=chat_id, photo=open(info_cost_tattoo_image1, 'rb'))
            await context.bot.send_message(chat_id=chat_id, text='2) Level of detail and complexity')
            await context.bot.send_photo(chat_id=chat_id, photo=open(info_cost_tattoo_image2, 'rb'))
            await context.bot.send_message(chat_id=chat_id, text='3) Location (where must be tattoo)')
            await context.bot.send_photo(chat_id=chat_id, photo=open(info_cost_tattoo_image3, 'rb'))
            await context.bot.send_message(chat_id=chat_id, text='4) Use of color ')
            await context.bot.send_photo(chat_id=chat_id, photo=open(info_cost_tattoo_image4, 'rb'))
            await context.bot.send_message(chat_id=chat_id, text='5) Pain threshold (quantity of sessions)')
            await context.bot.send_photo(chat_id=chat_id, photo=open(info_cost_tattoo_image5, 'rb'))
            await context.bot.send_message(chat_id=chat_id,
                                           text="For a more detailed assessment of your idea, write to the tattoo artist:")

            instagram_keyboard = [InlineKeyboardButton("Instagram", url='https://www.instagram.com/alexandr_darksoul/')]
            linkedin_keyboard = [InlineKeyboardButton('Facebook', url='https://www.facebook.com/AlexINKINK/')]
            keyboard = InlineKeyboardMarkup([instagram_keyboard, linkedin_keyboard])

            if 'RU' in selected_data:
                await context.bot.send_message(chat_id=chat_id, text="🔥Подписывайся что бы быть вкурсе всех событий🔥",
                                               reply_markup=keyboard)

            elif 'ENG' in selected_data:
                await context.bot.send_message(chat_id=chat_id, text="🔥Subscribe to stay informed about all events🔥",
                                               reply_markup=keyboard)

            elif 'PL' in selected_data:
                await context.bot.send_message(chat_id=chat_id,
                                               text="🔥Subskrybuj, aby być na bieżąco ze wszystkimi wydarzeniami🔥",
                                               reply_markup=keyboard)

        elif "RU" in selected_data:
            await context.bot.send_photo(chat_id=chat_id, photo=open(how_much_image_path, 'rb'))
            await context.bot.send_message(chat_id=chat_id, text='Формирование цены:')
            await context.bot.send_message(chat_id=chat_id, text='1) Размер')
            await context.bot.send_photo(chat_id=chat_id, photo=open(info_cost_tattoo_image1, 'rb'))
            await context.bot.send_message(chat_id=chat_id, text='2) Детализация и сложность')
            await context.bot.send_photo(chat_id=chat_id, photo=open(info_cost_tattoo_image2, 'rb'))
            await context.bot.send_message(chat_id=chat_id, text='3) Место расположения тату')
            await context.bot.send_photo(chat_id=chat_id, photo=open(info_cost_tattoo_image3, 'rb'))
            await context.bot.send_message(chat_id=chat_id, text='4) Использование цветных красок')
            await context.bot.send_photo(chat_id=chat_id, photo=open(info_cost_tattoo_image4, 'rb'))
            await context.bot.send_message(chat_id=chat_id, text='5) Болевой порог (количество сеансов)')
            await context.bot.send_photo(chat_id=chat_id, photo=open(info_cost_tattoo_image5, 'rb'))
            await context.bot.send_message(chat_id=chat_id,
                                           text='Для более детальной оценкой вашей идеи напишите тату мастеру:')

            instagram_keyboard = [InlineKeyboardButton("Instagram", url='https://www.instagram.com/alexandr_darksoul/')]
            linkedin_keyboard = [InlineKeyboardButton('Facebook', url='https://www.facebook.com/AlexINKINK/')]
            keyboard = InlineKeyboardMarkup([instagram_keyboard, linkedin_keyboard])

            if 'RU' in selected_data:
                await context.bot.send_message(chat_id=chat_id, text="🔥Подписывайся что бы быть вкурсе всех событий🔥",
                                               reply_markup=keyboard)

            elif 'ENG' in selected_data:
                await context.bot.send_message(chat_id=chat_id, text="🔥Subscribe to stay informed about all events🔥",
                                               reply_markup=keyboard)

            elif 'PL' in selected_data:
                await context.bot.send_message(chat_id=chat_id, text="🔥Subskrybuj, aby być na bieżąco ze wszystkimi wydarzeniami🔥",
                                               reply_markup=keyboard)

        elif "PL" in selected_data:
            await context.bot.send_photo(chat_id=chat_id, photo=open(how_much_image_path, 'rb'))
            await context.bot.send_message(chat_id=chat_id, text='Kształtowanie ceny:')
            await context.bot.send_message(chat_id=chat_id, text='1) Rozmiar')
            await context.bot.send_photo(chat_id=chat_id, photo=open(info_cost_tattoo_image1, 'rb'))
            await context.bot.send_message(chat_id=chat_id, text='2) Stopień szczegółowości i złożoność')
            await context.bot.send_photo(chat_id=chat_id, photo=open(info_cost_tattoo_image2, 'rb'))
            await context.bot.send_message(chat_id=chat_id, text='3) Lokalizacja, w której usługa jest świadczona')
            await context.bot.send_photo(chat_id=chat_id, photo=open(info_cost_tattoo_image3, 'rb'))
            await context.bot.send_message(chat_id=chat_id, text='4) Użycie kolorów, jeśli ma zastosowanie')
            await context.bot.send_photo(chat_id=chat_id, photo=open(info_cost_tattoo_image4, 'rb'))
            await context.bot.send_message(chat_id=chat_id, text='5) Próg bólu (Liczba sesji)')
            await context.bot.send_photo(chat_id=chat_id, photo=open(info_cost_tattoo_image5, 'rb'))
            await context.bot.send_message(chat_id=chat_id,
                                           text="Dla bardziej szczegółowej oceny swojego pomysłu, napisz do tatuażysty:")

            instagram_keyboard = [InlineKeyboardButton("Instagram", url='https://www.instagram.com/alexandr_darksoul/')]
            linkedin_keyboard = [InlineKeyboardButton('Facebook', url='https://www.facebook.com/AlexINKINK/')]
            keyboard = InlineKeyboardMarkup([instagram_keyboard, linkedin_keyboard])

            if 'RU' in selected_data:
                await context.bot.send_message(chat_id=chat_id, text="🔥Подписывайся что бы быть вкурсе всех событий🔥",
                                               reply_markup=keyboard)

            elif 'ENG' in selected_data:
                await context.bot.send_message(chat_id=chat_id, text="🔥Subscribe to stay informed about all events🔥",
                                               reply_markup=keyboard)

            elif 'PL' in selected_data:
                await context.bot.send_message(chat_id=chat_id,
                                               text="🔥Subskrybuj, aby być na bieżąco ze wszystkimi wydarzeniami🔥",
                                               reply_markup=keyboard)

    else:
        if "ENG" in selected_data:
            photo_path = os.path.join(os.path.dirname(__file__), "media", "brat.jpg")
            await context.bot.send_photo(chat_id=chat_id, photo=open(photo_path, 'rb'))
            await context.bot.send_message(
                chat_id=chat_id,
                text=''' Hi! 👋
                I am DarkSoultattooBot 🤖
                A virtual assistant of tattoo artist AleksandrDarkSoul.
                Go to the menu and check out the information we have prepared for you.🔥
                Have a tattoo-filled day!😉''')

        elif "RU" in selected_data:
            photo_path = os.path.join(os.path.dirname(__file__), "media", "brat.jpg")
            await context.bot.send_photo(chat_id=chat_id, photo=open(photo_path, 'rb'))
            await context.bot.send_message(
                chat_id=chat_id,
                text='''Привет! 👋
                Меня зовут DarkSoultattooBot 🤖
                Я виртуальный помощник тату-мастера AleksandrDarkSoul.
                Перейди в меню и ознакомься с информацией, которую мы для тебя приготовили.🔥
                Желаю татушного дня!😉''')

        elif "PL" in selected_data:
            photo_path = os.path.join(os.path.dirname(__file__), "media", "brat.jpg")
            await context.bot.send_photo(chat_id=chat_id, photo=open(photo_path, 'rb'))
            await context.bot.send_message(
                chat_id=chat_id,
                text='''Cześć! 👋
                Jestem DarkSoultattooBot 🤖
                Jestem wirtualnym asystentem tatuażysty AleksandrDarkSoul.
                Przejdź do menu i zapoznaj się z informacją, którą dla Ciebie przygotowaliśmy.🔥
                Życzę Ci tatuowanego dnia!😉 ''')


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

    await data_controller(selected_data, chat_id, context, update)

if __name__ == '__main__':
    button_click()
