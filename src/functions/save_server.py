from src.services.supabase import supabase
from typing import Annotated
from fastapi import Body

def save_server(owner: str, url: Annotated[str, Body(...)], port: Annotated[str, Body(...)]):
    supabase.table('servers').insert({
        'owner': owner,
        'url': url,
        'port': port
    }).execute()

    return {
        'message': 'Server saved successfully'
   }