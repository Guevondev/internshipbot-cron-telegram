from telethon.sync import TelegramClient
from dotenv import load_dotenv
import datetime
import os

# Loads basic data
offersFile = open('offers.txt', 'w', encoding='utf-8')
load_dotenv('.env')
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

    for message in client.iter_messages(
            channel,
            offset_date=datetime.date(2022, 10, 25),
            reverse=True):

        if hasattr(message.media, 'photo') == False:
            message = message.message.split('\n', 1)
            offer = {"author": message[0], "offer": message[1], "source": "telegram"}
            offersFile.write(str(offer) + ',\n')
            
    offersFile.close()

    

