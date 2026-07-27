import os
from supabase import create_client

url = os.environ["SUPABASE_URL"]
key = os.environ["SUPABASE_SECRET_KEY"]

supabase = create_client(url, key)