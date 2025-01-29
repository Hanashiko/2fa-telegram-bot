import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message
import pyotp
import config

API_TOKEN = config.API_TOKEN

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

user_key = open('2fa.txt').read().strip()

def verify_code(key, user_input):
    totp = pyotp.TOTP(key)
    return totp.verify(user_input)

@dp.message(Command("start"))
async def send_welcome(message: Message):
    await message.answer("Enter the code from your Google Authenticator App")

@dp.message()
async def handle_message(message: Message):
    user_input = message.text
    if verify_code(user_key, user_input):
        await message.answer("Authentication Successful")
    else:
        await message.answer("Authentication Failed")

if __name__ == '__main__':
    dp.run_polling(bot)