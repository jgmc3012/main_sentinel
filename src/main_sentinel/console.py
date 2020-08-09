import logging

import click
from decouple import config as env
from aiogram import Bot, Dispatcher, executor, types

from .import __version__

API_TOKEN = env('API_TOKEN')

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi!\nI'm Sentinela2Bot!\nI can't help you now.")

@dp.message_handler()
async def echo(message: types.Message):
    logging.info(message.text)
    await message.answer(message.text)


@click.command()
@click.version_option(version=__version__)
def main():
    """Sentinela Bot"""
    executor.start_polling(dp, skip_updates=True)
