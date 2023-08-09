from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler
from user_data_handler import selected_data

questions = {

    'question1': 'Имя и фамилия',
    'question2': 'Ваш адрес проживания:',
    'question3': 'Pesel или паспортные данные:',
    'question4': 'Номер телефона:',
    'question5': 'Email:',
    'question6': 'Подтвердите что введеные данные верны напишите "ок", в противном случае /cancel'
                 'Если вы допустили ошибку или ввели непраильніе данные'
}

user_answers = {}
print("Initial user_answers:", user_answers)

QUESTION = 1


async def start_survey(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    if "RU" in selected_data:
        await context.bot.send_message(chat_id=chat_id, text='Привет, єта анкета предназначена для уже записаных клиентов на тату сеанс.\nТут вы заполните анкету о вашем здоровьи. Если хотите отменить напишите команду /cancel !\n '
                                                         'Напишите имя и фамилию латиницей exp: Robert Khursdhuian')
    elif 'ENG' in selected_data:
        await context.bot.send_message(chat_id=chat_id,
                                       text="Hello, this form is intended for clients who are already scheduled for a tattoo session. Here you will fill out a health questionnaire. If you want to cancel, please type the command /cancel!"
                                       "Please write your first and last name in Latin script, e.g. Robert Khursdhuian.")
    elif 'PL' in selected_data:
        await context.bot.send_message(chat_id=chat_id,
                                       text="Witaj, ten formularz jest przeznaczony dla klientów, którzy już umówili się na sesję tatuażu. Tutaj wypełnisz ankietę zdrowotną. Jeśli chcesz anulować, wpisz komendę /cancel!"
                                        "Proszę podać imię i nazwisko w alfabecie łacińskim, np. Robert Khursdhuian.")
    return QUESTION


async def ask_question(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    chat_id = update.effective_chat.id
    user_answer = update.message.text
    current_question = len(user_answers)

    if current_question >= len(questions):
        if "RU" in selected_data:
            await context.bot.send_message(chat_id=chat_id, text="Анкета была успешно заполнена.")
        elif "ENG" in selected_data:
            await context.bot.send_message(chat_id=chat_id, text="The form has been successfully filled out.")
        elif "PL" in selected_data:
            await context.bot.send_message(chat_id=chat_id, text="Formularz został pomyślnie wypełniony.")
        print("Final user_answers:", user_answers)
        return ConversationHandler.END

    current_key = f'question{current_question}'
    user_answers[current_key] = user_answer

    next_key = f'question{current_question + 1}'
    await context.bot.send_message(chat_id=chat_id, text=questions[next_key])
    print(f"Asked question: {questions[next_key]}")
    return QUESTION


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    chat_id = update.effective_chat.id
    if 'RU' in selected_data:
        await context.bot.send_message(chat_id=chat_id, text="Опрос отменен.")
    if 'ENG' in selected_data:
        await context.bot.send_message(chat_id=chat_id, text="The survey has been canceled.")
    if 'PL' in selected_data:
        await context.bot.send_message(chat_id=chat_id, text="Ankieta została anulowana.")
    return ConversationHandler.END

