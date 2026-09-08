

import asyncio
from os import getenv
import logging 

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

TOKEN = ("8633110607:AAHoFnMT7EP5nkiAzSVEWzbV8FhW67cU1do")
dp = Dispatcher()


# Command handler
@dp.message(Command("start"))
async def command_start_handler(message: Message) -> None:
    await message.answer("Hello! I'm a bot created with aiogram.")

@dp.message(Command("help"))
async def command_helpmenu_handler(message: Message) -> None:
    await message.answer("This is a help message. Use /start to start the bot.")


# Run the bot
async def main() -> None:
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    print("Bot is starting...")
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
          

