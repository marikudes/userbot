from telethon import TelegramClient
from creds import app_id, app_hash, username, delay_time
from bible import Bible
import asyncio

class Application:
    def __init__(self):
        self.client = TelegramClient('session', app_id, app_hash)

    async def sendmsg(self, chat):
        await self.client.start()  
        while True:
            message = str(Bible().return_random_chapter())
            await self.client.send_message(chat, message)
            await asyncio.sleep(delay_time) 

    async def run(self, chat):
        await self.sendmsg(chat)
        await self.client.disconnect()

if __name__ == '__main__':
    app = Application()
    asyncio.run(app.run(username))
