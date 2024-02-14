from src.services.supabase import supabase
from smtplib import SMTP

def send_mail(mail_account_id: int, folder_id: int):
    mail_info, _ = supabase.table('mail_accounts').select('*, mail_server(*)').eq('id', mail_account_id).single().execute()

    print(mail_info)