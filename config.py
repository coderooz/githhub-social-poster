import os
from dotenv import load_dotenv

load_dotenv(dotenv_path='./.env', )

template = os.getenv('Template', 'default_template_text')

owner = os.getenv('OWNER', 'default_owner')
mongo_url = os.getenv('MONGO_URI', 'default_mongo_url')
facebook_access_key = os.getenv('FB_ACCESS_TOKEN', 'default_access_token')
fb_page = os.getenv('FB_PAGE_NAME', 'default_page_name')

insta_access_key = os.getenv('INSTA_ACESS_TOKEN', 'default_page_name')


if not facebook_access_key:
    raise ValueError("ACCESS_TOKEN environment variable not set")
