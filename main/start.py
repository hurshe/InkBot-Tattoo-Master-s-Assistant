from telegram.ext import ContextTypes


async def start_command(selected_data: list, chat_id: int, context: ContextTypes.DEFAULT_TYPE):
    media_paths = {
        "ENG": {
            "care": ("C:\\Users\\rober\\DarkSoulTattoBot\\InkBot-Tattoo-Master-s-Assistant\\main\\media\\GC_05700.jpeg", "C:\\Users\\rober\\DarkSoulTattoBot\\InkBot-Tattoo-Master-s-Assistant\\main\\media\\Уход за тату.docx"),
            "how_to": ("C:\\Users\\rober\\DarkSoulTattoBot\\InkBot-Tattoo-Master-s-Assistant\\main\\media\\maxresdefault.jpg", "C:\\Users\\rober\\DarkSoulTattoBot\\InkBot-Tattoo-Master-s-Assistant\\main\\media\\Уход за тату.docx"),
            "how_much": ("C:\\Users\\rober\\DarkSoulTattoBot\\InkBot-Tattoo-Master-s-Assistant\\main\\media\\pricing.png", "C:\\Users\\rober\\DarkSoulTattoBot\\InkBot-Tattoo-Master-s-Assistant\\main\\media\\Уход за тату.docx"),
            "default": ("C:\\Users\\rober\\DarkSoulTattoBot\\InkBot-Tattoo-Master-s-Assistant\\main\\media\\brat.jpg", None)
        },
        "RU": {
            "care": ("C:\\Users\\rober\\DarkSoulTattoBot\\InkBot-Tattoo-Master-s-Assistant\\main\\media\\GC_05700.jpeg", "C:\\Users\\rober\\DarkSoulTattoBot\\InkBot-Tattoo-Master-s-Assistant\\main\\media\\Уход за тату.docx"),
            "how_to": ("C:\\Users\\rober\\DarkSoulTattoBot\\InkBot-Tattoo-Master-s-Assistant\\main\\media\\maxresdefault.jpg", "C:\\Users\\rober\\DarkSoulTattoBot\\InkBot-Tattoo-Master-s-Assistant\\main\\media\\Уход за тату.docx"),
            "how_much": ("C:\\Users\\rober\\DarkSoulTattoBot\\InkBot-Tattoo-Master-s-Assistant\\main\\media\\pricing.png", "C:\\Users\\rober\\DarkSoulTattoBot\\InkBot-Tattoo-Master-s-Assistant\\main\\media\\Уход за тату.docx"),
            "default": ("C:\\Users\\rober\\DarkSoulTattoBot\\InkBot-Tattoo-Master-s-Assistant\\main\\media\\brat.jpg", None)
        },
        "PL": {
            "care": ("C:\\Users\\rober\\DarkSoulTattoBot\\InkBot-Tattoo-Master-s-Assistant\\main\\media\\GC_05700.jpeg", "C:\\Users\\rober\\DarkSoulTattoBot\\InkBot-Tattoo-Master-s-Assistant\\main\\media\\Уход за тату.docx"),
            "how_to": ("C:\\Users\\rober\\DarkSoulTattoBot\\InkBot-Tattoo-Master-s-Assistant\\main\\media\\maxresdefault.jpg", "C:\\Users\\rober\\DarkSoulTattoBot\\InkBot-Tattoo-Master-s-Assistant\\main\\media\\Уход за тату.docx"),
            "how_much": ("C:\\Users\\rober\\DarkSoulTattoBot\\InkBot-Tattoo-Master-s-Assistant\\main\\media\\pricing.png", "C:\\Users\\rober\\DarkSoulTattoBot\\InkBot-Tattoo-Master-s-Assistant\\main\\media\\Уход за тату.docx"),
            "default": ("C:\\Users\\rober\\DarkSoulTattoBot\\InkBot-Tattoo-Master-s-Assistant\\main\\media\\brat.jpg", None)
        }
    }

    greetings = {
        "ENG": "Greetings! ",
        "RU": "Приветствую! ",
        "PL": "Cześć! ",
    }

    language = "default"
    if "ENG" in selected_data:
        language = "ENG"
    elif "RU" in selected_data:
        language = "RU"
    elif "PL" in selected_data:
        language = "PL"

    selected_key = selected_data

    # Check if the selected data falls under the "faq" category
    is_faq_category = selected_key in ["how_to", "how_much", "care"]

    photo_path, document_path = media_paths[language].get(selected_key, media_paths[language]["default"])

    if photo_path:
        await context.bot.send_photo(chat_id=chat_id, photo=open(photo_path, 'rb'))
    if document_path:
        await context.bot.send_document(chat_id=chat_id, document=open(document_path, 'rb'))

    # Send the greeting only if it's not a "faq" category
    if not is_faq_category:
        greeting = greetings[language]
        await context.bot.send_message(chat_id=chat_id, text=greeting)
