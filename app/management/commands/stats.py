from django.core.management.base import BaseCommand
from datetime import datetime
from django.utils.timezone import utc
from app.bot.main import start
import asyncio
  
def now():
    return datetime.utcnow().replace(tzinfo=utc)
  
  
class Command(BaseCommand):
    help = 'Displays stats related to Article and Comment models'

    def handle(self, *args, **kwargs):
        asyncio.run(start())