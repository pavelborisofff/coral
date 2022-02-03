from os import environ, path
from dotenv import load_dotenv

# Find .env file
basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

# General Config
YANDEX_MAPS_API_KEY = environ.get('YANDEX_MAPS_API_KEY')
