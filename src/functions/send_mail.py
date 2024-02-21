from src.services.supabase import supabase
from fastapi import Body
from smtplib import SMTP
from email.mime.text import MIMEText
from typing import Annotated

def send_mail(mail_account_id: int, folder_id: int, annotated_html_body: Annotated[str, Body(...)]):
    mail_info = supabase.table('mail_accounts').select('*, mail_server(*)').eq('id', mail_account_id).single().execute().model_dump()

    url = mail_info['mail_server']['url']
    port = mail_info['mail_server']['port']
    email = mail_info['email'] or ''
    password = mail_info['password']

    server = SMTP(url, port)

    server.starttls()

    server.login(email, password)

    mails = supabase.table('mails_saved').select('email').eq('folder', folder_id).execute().model_dump()

    message = MIMEText(annotated_html_body, 'html')

    for mail in mails:
        server.sendmail(email, mail, message.as_string())

    server.quit()

    return {
        'message': 'Mail sent successfully'
    }