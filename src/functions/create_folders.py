from src.services.supabase import supabase

def create_folder(name: str, owner: str):
    supabase.table('folders').insert({
        'name': name,
        'owner': owner
    }).execute()

    return {
        'message': 'Folder created successfully'
    }