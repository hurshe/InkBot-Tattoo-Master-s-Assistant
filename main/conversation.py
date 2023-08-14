from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler
from user_data_handler import selected_data

questions = {
    'PL': {
        'question1': 'Imię i nazwisko:',
        'question2': 'Twój adres zamieszkania:',
        'question3': 'Numer PESEL lub dane paszportowe:',
        'question4': 'Numer telefonu:',
        'question5': 'Adres email:',
        'question6': 'Skąd dowiedziałeś/łaś się o mnie, proszę podać nazwę portalu społecznościowego:',
        'question7': 'Jeśli wszystko jest wypełnione poprawnie, napisz "ok"; jeśli nie, napisz /cancel i wypełnij ankietę ponownie!',
    },
    'ENG': {
        'question1': 'First and last name:',
        'question2': 'Your residential address:',
        'question3': 'Pesel or passport information:',
        'question4': 'Phone number:',
        'question5': 'Email:',
        'question6': 'How did you find out about me, please write the social network:',
        'question7': 'If everything is filled out correctly, write "ok"; if not, write /cancel and fill out the questionnaire again!',

    },
    'RU': {
        'question1': 'Имя и фамилия:',
        'question2': 'Ваш адрес проживания:',
        'question3': 'Pesel или паспортные данные:',
        'question4': 'Номер телефона:',
        'question5': 'Email:',
        'question6': 'Как вы узнали обо мне напишщите соц сеть:',
        'question7': 'Ксли все заполнено правильно напишите "ok" если нет напишите /cancel и заполните анкету снова!', }
}

user_answers = {}

QUESTION = 1


async def ask_question(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    chat_id = update.effective_chat.id
    user_answer = update.message.text
    current_question = len(user_answers)

    if current_question >= len(questions['ENG'] or len(questions['RU'] or len(questions['PL']))):
        if 'RU' in selected_data:
            await context.bot.send_message(chat_id=chat_id, text="Анкета была успешно заполнена.")
        elif 'ENG' in selected_data:
            await context.bot.send_message(chat_id=chat_id, text="The survey was succesfully finished!")
        elif 'PL' in selected_data:
            await context.bot.send_message(chat_id=chat_id, text="Kwestionariusz został uzupełniony!")
        print("Final user_answers:", user_answers)
        return ConversationHandler.END

    current_key = f'question{current_question}'
    user_answers[current_key] = user_answer

    next_key = f'question{current_question + 1}'
    if 'ENG' in selected_data:
        await context.bot.send_message(chat_id=chat_id, text=questions['ENG'][next_key])
    elif 'RU' in selected_data:
        await context.bot.send_message(chat_id=chat_id, text=questions['RU'][next_key])
    elif 'PL' in selected_data:
        await context.bot.send_message(chat_id=chat_id, text=questions['PL'][next_key])
    return QUESTION


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    chat_id = update.effective_chat.id
    if 'ENG' in selected_data:
        await context.bot.send_message(chat_id=chat_id, text="Survey was canceled.")
    elif 'PL' in selected_data:
        await context.bot.send_message(chat_id=chat_id, text="Ankieta odrzucona.")
    elif 'RU' in selected_data:
        await context.bot.send_message(chat_id=chat_id, text="Анкета отменена.")
    return ConversationHandler.END

