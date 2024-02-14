from src.services.supabase import supabase

def create_account(email: str, password: str, mail_server: int):
    supabase.table('accounts').insert({
        'email': email,
        'password': password,
        'mail_server': mail_server
    }).execute()

    return {
        'message': 'Account created successfully'
    }