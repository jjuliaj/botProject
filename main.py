from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from responses import get_response

load_dotenv()
TOKEN: Final[str] = os.getenv("DISCORD_TOKEN")

# Bot setup
intents: Intents = Intents.default()
intents.message_content = True # NOQA
client: Client = Client(intents=intents)

# Bot message functionality
async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print('(Message was empty because intents were not enabled)')
        return

    # If private message is needed
    if is_private := user_message[0] == '?':
        user_message = user_message[1:]

    try:
        response: str = get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

# Handling bot going online, the startup for the bot
@client.event
async def on_ready() -> None:
    print(f'{client.user} on täällä nyaaaw! (＾• ω •＾)')

# Handling incoming messages
@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user: # If bot is the one who wrote the message
        return

    username: str = str(message.author)
    user_message: str = str(message.content)
    channel: str = str(message.channel)

    # Check if the bot is mentioned in the message
    if client.user in message.mentions:
        # Remove the bot mention fron the start of the message
        user_message = user_message.replace(f'<@!{client.user.id}>', '').strip() # Handle regular mentions
        user_message = user_message.replace(f'<@!{client.user.id}>', '').strip()  # Handle nickname mentions

        print(f'[{channel}] {username}: "{user_message}"')
        await send_message(message, user_message)

# Main entry point for running code
def main() -> None:
    client.run(token=TOKEN)

if __name__ == '__main__':
    main()