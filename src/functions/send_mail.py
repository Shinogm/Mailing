from fastapi import Body
from pydantic import BaseModel
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from smtplib import SMTP
from typing import Annotated


class MailProperties(BaseModel):
    url: str
    port: str
    email: str
    password: str



def send_mail(title: str, mail_properties: MailProperties, mails: list[str], html: Annotated[str, Body(..., embed=True)]):

    url = mail_properties.url
    port = mail_properties.port
    email = mail_properties.email
    password = mail_properties.password

    server = SMTP(url, int(port))

    server.starttls()

    server.login(email, password)

    for mail in mails:
        msg = MIMEMultipart()
        msg['Subject'] = title
        msg['From'] = email
        msg['To'] = mail


        # Agregar el contenido HTML al mensaje
        msg.attach(MIMEText(html, 'html'))

        server.send_message(msg)

    server.quit()

    return {
        'message': 'Mail sent successfully'
    }
