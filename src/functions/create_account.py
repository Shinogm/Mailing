from src.services.supabase import supabase
from typing import Annotated
from fastapi import Body

def create_account(email: Annotated[str, Body(...)], password: Annotated[str, Body(...)], mail_server: int):
    supabase.table('accounts').insert({
        'email': email,
        'password': password,
        'mail_server': mail_server
    }).execute()

    return {
        'message': 'Account created successfully'
    }