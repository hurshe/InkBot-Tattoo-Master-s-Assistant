import os
from reportlab.pdfgen import canvas
from PyPDF2 import PdfReader, PdfWriter
from telegram.ext import ContextTypes
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from conversation import user_answers
from user_data_handler import selected_data

selected_data = selected_data


input_pdf_path = "media/anketa.pdf"
output_pdf_path = "media/filled_form.pdf"


async def generic_pdf(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    c = canvas.Canvas(output_pdf_path)
    c.drawString(50, 710, user_answers['question1'])
    c.drawString(250, 710, user_answers['question2'])
    c.drawString(50, 665, user_answers['question3'])
    c.drawString(220, 665, user_answers['question4'])
    c.drawString(385, 665, user_answers['question5'])
    c.drawString(50, 120, user_answers['question6'])
    c.save()

    reader = PdfReader(input_pdf_path)
    writer = PdfWriter()
    page = reader.pages[0]
    page.merge_page(PdfReader(output_pdf_path).pages[0])
    writer.add_page(page)
    with open(output_pdf_path, 'wb') as output_file:
        writer.write(output_file)
    doc_path = os.path.join(os.path.dirname(__file__), 'media', 'filled_form.pdf')
    await context.bot.send_document(chat_id=(chat_id, 742290897), document=doc_path)
