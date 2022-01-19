import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('./recursos/index.html').read_text())
email = EmailMessage()
email['from'] = '<etiqueta-remitente>'
email['to'] = '<correo-destinatario>'
email['subject'] = 'Correo Formato HTML'

email.set_content(html.substitute({'name': 'Pedro'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
  smtp.ehlo()
  smtp.starttls()
  smtp.login('<cuenta-gmail>', '<clave-gmail>')
  smtp.send_message(email)
  print('all good boss!')

