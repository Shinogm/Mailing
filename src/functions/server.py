from src.services.supabase import supabase
from fastapi import Body
from typing import Annotated

def save_server(owner: str, url: str, port: str):
    supabase.table('mail_server').insert({
        'owner': owner,
        'url': url,
        'port': port
    }).execute()

    return {
        'message': 'Server saved successfully'
   }

def get_servers(owner: str):
    return supabase.table('mail_server').select('*').eq('owner', owner).execute().model_dump()

def delete_server(owner: str, id: str):
    return supabase.table('mail_server').delete().eq('owner', owner).eq('id', id).execute().model_dump()

def update_server(owner: str, id: str, url: Annotated[str, Body(...)], port: Annotated[str, Body(...)]):
    return supabase.table('mail_server').update({
        'url': url,
        'port': port
    }).eq('owner', owner).eq('id', id).execute().model_dump()

def create_account(email: Annotated[str, Body(...)], password: Annotated[str, Body(...)], mail_server: int):
    supabase.table('accounts').insert({
        'email': email,
        'password': password,
        'mail_server': mail_server
    }).execute()

    return {
        'message': 'Account created successfully'
    }

def get_accounts(mail_server: int):
    return supabase.table('accounts').select('*').eq('mail_server', mail_server).execute().model_dump()

def delete_account(mail_server: int, id: int):
    return supabase.table('accounts').delete().eq('mail_server', mail_server).eq('id', id).execute().model_dump()

def update_account(mail_server: int, id: int, email: Annotated[str, Body(...)], password: Annotated[str, Body(...)]):
    return supabase.table('accounts').update({
        'email': email,
        'password': password
    }).eq('mail_server', mail_server).eq('id', id).execute().model_dump()