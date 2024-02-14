from src.services.supabase import supabase
from fastapi import Body
from typing import Annotated
from smtplib import SMTP
from email.mime.text import MIMEText

def create_folder(name: Annotated[str, Body(...)], owner: Annotated[str, Body(...)]):
    supabase.table('folders').insert({
        'name': name,
        'owner': owner
    }).execute()

    return {
        'message': 'Folder created successfully'
    }

def save_mail(mail: str, folder_id: int):
    supabase.table('mails_saved').insert({
        'email': mail,
        'folder': folder_id
    }).execute()

    return {
        'message': 'Mail saved successfully'
    }

def send_mail(mail_account_id: int, folder_id: int, html: Annotated[str, Body(..., embed=True)]):
    mail_info = supabase.table('mail_accounts').select('*, mail_server(*)').eq('id', mail_account_id).single().execute().model_dump()

    url = mail_info['mail_server']['url']
    port = mail_info['mail_server']['port']
    email = mail_info['email'] or ''
    password = mail_info['password']

    server = SMTP(url, port)

    server.starttls()

    server.login(email, password)

    mails = supabase.table('mails_saved').select('email').eq('folder', folder_id).execute().model_dump()

    message = MIMEText(html, 'html')

    for mail in mails:
        server.sendmail(email, mail, message.as_string())

    server.quit()

    return {
        'message': 'Mail sent successfully'
    }