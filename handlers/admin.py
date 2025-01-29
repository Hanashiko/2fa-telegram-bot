from aiogram import types, Router, F
from aiogram.filters import Command

from database.users import UsersManager

from dotenv import load_dotenv
import os
load_dotenv()

OWNER_ID = os.getenv("OWNER_ID") 

router = Router()

@router.message(Command(commands=['create_user_table']))
async def command_create_user_table(message: types.Message):
    if message.from_user.id != int(OWNER_ID):
        await message.reply("You are not the owner!")
        return
    UsersManager.create_table()
    await message.reply("Table created!")

@router.message(Command(commands=['delete_user_table']))
async def command_delete_user_table(message: types.Message):
    if message.from_user.id != int(OWNER_ID):
        await message.reply("You are not the owner!")
        return
    UsersManager.delete_table()
    await message.reply("Table deleted!")
    
@router.message(Command(commands=['get_users']))
async def command_get_users(message: types.Message):
    if message.from_user.id != int(OWNER_ID):
        await message.reply("You are not the owner!")
        return
    users = UsersManager.get_all()
    if not users:
        await message.reply("No users found!")
        return
    result = "ID | Code\n"
    for user in users:
        result += f"{user[0]} | {user[1]}\n"
    await message.reply(result)

def register_admin_handlers(dp):
    dp.include_router(router)