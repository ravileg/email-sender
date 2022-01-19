import smtplib
from email.message import EmailMessage

def sendemail(to, subject, message):
    msg = EmailMessage()
    msg.set_content(message)
    msg["subject"] = subject
    msg["to"] = to

    user = "<cuenta-gmail>"
    msg["from"] = user
    password = "<clave-gmail>"

    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
      smtp.ehlo()
      smtp.starttls()
      smtp.login(user, password)
      smtp.send_message(msg)
      smtp.quit()

    print('Todo Ok!')


if __name__ == '__main__':
    sendemail("<correo-destinatario>", "Correo de Prueba", "Hola Raúl!")


