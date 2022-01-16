import smtplib
from email.message import EmailMessage
from turtle import st
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Nguyen Nam'
email['to'] = 'nam.nv205106@sis.hust.edu.vn'
email['subject'] = 'Hello this is my first email sent by Python'
email.set_content(html.safe_substitute(name='Test'),'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('432dsdada@gmail.com', password='q52431')
    smtp.send_message(email)
    print('Email sent')
