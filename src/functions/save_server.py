from src.services.supabase import supabase

def save_server(owner: str, url: str, port: str):
    supabase.table('servers').insert({
        'owner': owner,
        'url': url,
        'port': port
    }).execute()

    return {
        'message': 'Server saved successfully'
   }