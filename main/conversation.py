from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler


questions = {
    'question1': 'Имя и фамилия',
    'question2': 'Ваш адрес проживания:',
    'question3': 'Pesel или паспортные данные:',
    'question4': 'Номер телефона:',
    'question5': 'Email:',
}

user_answers = {}
print("Initial user_answers:", user_answers)

QUESTION = 1


async def ask_question(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    chat_id = update.effective_chat.id
    user_answer = update.message.text
    current_question = len(user_answers)

    if current_question >= len(questions):
        await context.bot.send_message(chat_id=chat_id, text="Анкета была успешно заполнена.")
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
    await context.bot.send_message(chat_id=chat_id, text="Опрос отменен.")
    return ConversationHandler.END

