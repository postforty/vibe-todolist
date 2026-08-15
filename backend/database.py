import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

url = os.environ.get("SUPABASE_URL", "")
key = os.environ.get("SUPABASE_KEY", "")

_supabase: Client | None = None

if url and key:
    _supabase = create_client(url, key)

def get_db():
    return _supabase
