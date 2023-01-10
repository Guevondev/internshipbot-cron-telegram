from telethon.sync import TelegramClient
from dotenv import load_dotenv
import datetime
import os

# Loads basic data
load_dotenv('C:/Users/Kappappita/Desktop/telegram-internship-scrapper/.env')
API_ID = os.getenv('API_ID')
API_HASH = os.getenv('API_HASH')
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
TEST_CHANNEL = os.getenv('TEST_CHANNEL')

# Starts telegram client
with TelegramClient('anon', API_ID, API_HASH).start() as client:
    
    # Retrieves all available dialogs for user
    channels = {dialog.entity.title: dialog.entity \
         for dialog in client.get_dialogs() if dialog.is_channel}

    channel = channels[TEST_CHANNEL]
    # For each message in a channel, checks if it has a photo. If it
    # it does, ignores the offer, otherwise, creates a dictionary
    # with author, message and source.

    totalOffers = 0
    date = datetime.date.today() - datetime.timedelta(days=6)
    print(f'[Telegram] Retrieving messages from {date} until now')
    for message in client.iter_messages(
            channel,
            offset_date=date,
            reverse=True):

        if hasattr(message.media, 'photo') == False:
            message = message.message.split('\n', 1)
            offer = {"author": message[0], "offer": message[1], "source": "telegram"}
            # Actual HTTP request not used until deployment
            totalOffers += 1

    print(f'[Telegram] {totalOffers} messages retrieved')
            