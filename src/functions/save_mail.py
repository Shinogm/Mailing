from src.services.supabase import supabase

def save_mail(mail: str, folder_id: int):
    supabase.table('mails_saved').insert({
        'email': mail,
        'folder': folder_id
    }).execute()

    return {
        'message': 'Mail saved successfully'
    }