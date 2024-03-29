import os

from dotenv import load_dotenv
from supabase.client import Client, create_client

load_dotenv()

url: str = os.environ.get("SUPABASE_URL") or ''
key: str = os.environ.get("SUPABASE_KEY") or ''
supabase: Client = create_client(url, key)