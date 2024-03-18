from starlette.datastructures import CommaSeparatedStrings
from starlette.config import Config
from dotenv import load_dotenv
load_dotenv()
env = Config(".env")

BOT_TOKEN ="7097034104:AAGVeWDIG0QCz3pODyJQXS1euIE5gKWe4Ig" 
ADMINS = list(env("ADMINS",cast=CommaSeparatedStrings)) 
IP = env("ip",cast=str)  #
