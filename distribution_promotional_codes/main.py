import smtplib
from email.mime.text import MIMEText
import openpyxl


# Функция для отправки письма
def send_email(to, subject, message):
    # Настройки SMTP-сервера
    smtp_server = 'smtp.example.com'
    smtp_port = 587
    smtp_username = 'your_username'
    smtp_password = 'your_password'

    # Создание MIME-сообщения
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = smtp_username
    msg['To'] = to

    try:
        # Установка соединения с SMTP-сервером
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)

        # Отправка письма
        server.sendmail(smtp_username, to, msg.as_string())
        print(f'Письмо отправлено на адрес: {to}')

        # Закрытие соединения
        server.quit()

    except Exception as e:
        print(f'Ошибка при отправке письма на адрес {to}: {str(e)}')


# # Открытие файла с адресами электронной почты
# with open('email_addresses.txt', 'r') as file:
#     email_addresses = file.readlines()
#
# for email in email_addresses:
#     # Изменение некоторых данных в тексте сообщения
#     message = f'Привет, {email.strip()}! Это тестовое сообщение.'
#
#     # Отправка письма
#     send_email(email.strip(), 'Тестовое письмо', message)
#

# Открытие файла Excel
wb = openpyxl.load_workbook('email_data.xlsx')
ws = wb.active

# Чтение адресов и текста сообщения из файла Excel
for row in ws.iter_rows(min_row=2, values_only=True):
    email = row[0]
    text1 = row[1]

    # Изменение некоторых данных в тексте сообщения
    message = f'Привет {text1}, как дела?'

    # Отправка письма
    send_email(email, 'Тестовое письмо', message)

# Закрытие файла Excel
wb.close()

"""
Вам нужно заменить `smtp.example.com`, `smtp_username` и `smtp_password` на соответствующие значения для вашего 
SMTP-сервера. Также укажите путь к файлу с адресами электронной почты в переменной `email_addresses.txt`.

Код открывает файл `email_addresses.txt`, считывает адреса электронной почты и отправляет каждому адресу индивидуальное
 письмо, изменяя некоторую часть текста сообщения на каждой итерации.
"""
