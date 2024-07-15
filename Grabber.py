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

    return list(
        map(lambda x: x.lower(), [d.entity.username for d in dialogs if d.is_channel])
    )


async def join_channels(channel_list, dialogs):

    for channel in channel_list:
        if channel not in dialogs:
            while True:
                try:
                    await client(JoinChannelRequest(channel))
                    print(f"Joined channel: {channel}")
                    break
                except UserAlreadyParticipantError:
                    print(f"Already a member of channel: {channel}")
                    break
                except FloodWaitError as e:
                    print(
                        f"Rate limited. Waiting for {e.seconds} seconds before retrying..."
                    )
                    await asyncio.sleep(e.seconds)
                except Exception as e:
                    print(f"Failed to join channel {channel}: {e}")
                    break


async def get_channel_messages(channel, dialogs):
    if channel in dialogs:
        channel_entity = await client.get_entity(channel)

        messages = []
        async for message in client.iter_messages(
            channel_entity,
            offset_date=datetime.now(tz=timezone.utc) - timedelta(hours=72),
            reverse=True,
        ):

            if (message.message != None) and (len(message.message) != 0):

                pattern = r"(?<![a-zA-Z])(?:(?!https?)[a-zA-Z0-9]+):\/\/\S+"
                configs = re.findall(pattern, message.message, re.IGNORECASE)
                if configs != []:
                    messages += configs
        return messages
    else:
        return []


async def main():
    config_response = requests.get(conf_url)

    print(config_response.text)

    dialogs = await get_dialogs()

    if config_response.status_code == 200:
        status = "OK"

        channels = config_response.text.strip().lower().split(",")
        await join_channels(channels, dialogs)
    else:
        status = "LOCAL"
        channels = dialogs

    all_channels_messages = {"status": status}

    for channel in channels:
        all_channels_messages[channel] = await get_channel_messages(channel, dialogs)

    with open("configs.json", "w", encoding="utf-8") as f:
        json.dump(all_channels_messages, f, ensure_ascii=False, indent=4)


with client:
    client.loop.run_until_complete(main())