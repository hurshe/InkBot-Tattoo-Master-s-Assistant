import secrets
import string
from datetime import date

from reportlab.pdfgen import canvas
from PyPDF2 import PdfReader, PdfWriter


input_pdf_path = "media/voucher/E-VOUCHER.pdf"
output_pdf_path = "media/e_voucher.pdf"

question = {
    'question1': 'Robert Khurshudian',
    'question2': '1000 PLN',
}

code = string.ascii_uppercase + string.ascii_lowercase + string.digits
serial_number = ''.join(secrets.choice(code) for i in range(10))

today = date.today()
date_of_buy = today.strftime("%d/%m/%Y")


def generic_pdf(questions):
    # Создаем новый PDF-файл и добавляем текстовые поля
    c = canvas.Canvas(output_pdf_path)
    c.drawString(100, 440, questions['question1'])   #NAME
    c.drawString(100, 395, questions['question2'])   #COST
    c.drawString(100, 335, date_of_buy)              #DATE
    c.drawString(204, 335, serial_number)            #SERIAL_NUMBER
    c.save()

    reader = PdfReader(input_pdf_path)
    writer = PdfWriter()
    page = reader.pages[0]
    page.merge_page(PdfReader(output_pdf_path).pages[0])
    writer.add_page(page)
    with open(output_pdf_path, 'wb') as output_file:
        writer.write(output_file)


generic_pdf(question)


