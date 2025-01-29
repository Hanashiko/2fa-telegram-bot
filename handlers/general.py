from aiogram import types, Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
import qrcode
import pyotp
from create_bot import bot
from database.users import UsersManager
from io import BytesIO

router = Router()

class Check2FA(StatesGroup):
    code_2fa = State()

@router.message(Command(commands=['start']))
async def send_welcome(message: types.Message):
    if not UsersManager.get(message.from_user.id):
        UsersManager.add(message.from_user.id)
    await message.reply("Hello! This is a 2FA bot.")

@router.message(Command(commands=['make_qrcode']))
async def make_qrcode(message: types.Message):
    key = pyotp.random_base32()
    uri = pyotp.totp.TOTP(key).provisioning_uri(name=message.from_user.full_name, issuer_name="2FA-Bot")
    img = qrcode.make(uri)
    
    bio = BytesIO()
    img.save(bio, format='PNG')
    bio.seek(0)
    
    input_file = types.BufferedInputFile(bio.read(), filename='qrcode.png')
    await bot.send_photo(message.from_user.id, input_file, caption="Scan this QR code to enable 2FA.")
    UsersManager.edit(message.from_user.id, key)

@router.message(Command(commands=['check_2fa']))
async def check_2fa(message: types.Message, state: FSMContext):
    if not UsersManager.get(message.from_user.id):
        await message.reply("You need to create a QR code first!")
        return
    await message.reply("Enter the 2FA code:")
    await state.set_state(Check2FA.code_2fa)

@router.message(Command("cancel"))
@router.message(F.text.casefold() == "cancel")
async def cancel_handler(message: types.Message, state: FSMContext):
    await state.finish()
    await message.reply("Cancelled!")

@router.message(Check2FA.code_2fa)
async def check_2fa_code(message: types.Message, state: FSMContext):
    key = UsersManager.get(message.from_user.id)[1]
    totp = pyotp.TOTP(key)
    code = message.text.replace(" ", "")
    if totp.verify(code):
        await message.reply("2FA code is correct!")
    else:
        await message.reply("2FA code is incorrect!")
    await state.clear()

def register_general_handlers(dp):
    dp.include_router(router)