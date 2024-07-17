import re
import json
import asyncio
import requests
from telethon import TelegramClient
from datetime import datetime, timedelta, timezone
from telethon.errors import UserAlreadyParticipantError, FloodWaitError
from telethon.tl.functions.channels import JoinChannelRequest

api_id = 123456 #Your Telegram Api id
api_hash = 'YOUR_HASH' #Your Telegram Api Hash
conf_url = 'https://raw.githubusercontent.com/PATH/TO/YOUR/CONF/FILE' #Your Config File Path
client = TelegramClient('grabber', api_id, api_hash)


async def get_dialogs():

    dialogs = await client.get_dialogs()

    return [
        (d.entity.username.lower() if hasattr(d.entity, 'username') and d.entity.username else d.name)
        for d in dialogs if d.is_channel or d.is_group
    ]

async def join_chat(config_list, dialogs):

    for chat in config_list:
        if chat not in dialogs:
            while True:
                try:
                    await client(JoinChannelRequest(chat))
                    print(f"Joined chat: {chat}")
                    break
                except UserAlreadyParticipantError:
                    print(f"Already a member of chat: {chat}")
                    break
                except FloodWaitError as e:
                    print(
                        f"Rate limited. Waiting for {e.seconds} seconds before retrying..."
                    )
                    await asyncio.sleep(e.seconds)
                except Exception as e:
                    print(f"Failed to join chat {chat}: {e}")
                    break


async def get_channel_messages(input, dialogs):
    if input in dialogs:
        entity = await client.get_entity(input)

        all_configs = []
        async for message in client.iter_messages(
            entity,
            offset_date=datetime.now(tz=timezone.utc) - timedelta(hours=72),
            reverse=True,
        ):

            if (message.message != None) and (len(message.message) != 0):

                pattern = r"(?<![a-zA-Z])(?:(?!https?)[a-zA-Z0-9]+):\/\/\S+"
                configs = re.findall(pattern, message.message, re.IGNORECASE)
                if configs != []:
                    all_configs += configs
        return all_configs
    else:
        return []


async def main():

    config_response = requests.get(conf_url)

    dialogs = await get_dialogs()

    if config_response.status_code == 200:
        status = "OK"

        config_list = config_response.text.strip().lower().split(",")
        
        print(config_list)
        
        await join_chat(config_list, dialogs)
    else:
        status = "LOCAL"
        config_list = dialogs

    all_channels_messages = {"status": status}

    for channel in config_list:
        all_channels_messages[channel] = await get_channel_messages(channel, dialogs)

    with open("configs.json", "w", encoding="utf-8") as f:
        json.dump(all_channels_messages, f, ensure_ascii=False, indent=4)


with client:
    client.loop.run_until_complete(main())