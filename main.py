from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
import asyncio
from aiogram.filters.command import Command
import logging
import sys
import re
from aiogram import F
from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.filters import StateFilter
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
import asyncio
import logging
import sys
from aiogram import F
from aiogram import types
import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher, Router, types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
import re
from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv('TOKEN')
dp = Dispatcher()

bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

dp = Router()
logging.basicConfig(level=logging.INFO, stream=sys.stdout)

router = Router()
router.include_router(dp)


def validate_phone_number(value: str) -> bool:
    pattern = re.compile(r'\+998[0-9]{9}')
    return bool(pattern.match(value))


class Sherik(StatesGroup):
    full_name = State()
    phone_number = State()
    location = State()
    level = State()


@dp.message(Command("start"))
async def start_button(message: Message):
    await message.answer(f"Assalomu Alaykum {message.from_user.first_name} Ustoz-Shogird Botiga hush kelibsiz!")

kb = [
        [KeyboardButton(text='/Sherik kerak'), KeyboardButton(text='/start')]
    ]

buttons = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)



@dp.message(F.text == '/Sherik kerak')
async def start_ordering(message: Message, state: FSMContext):
    await message.answer(text='Buyurtma royhatnomasi boshlandi ismingizni kiriting')
    await state.set_state(Sherik.full_name.state)


@dp.message(StateFilter(Sherik.full_name))
async def set_full_name(message: Message, state: FSMContext):

    kb = [
        [KeyboardButton(text='Telefon raqamimni yuborish', request_contact=True)]
    ]

    buttons = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)


    await state.update_data(full_name=message.text)
    await message.answer(text='telefom raqamingizni yuboring', reply_markup=buttons)
    await state.set_state(Sherik.phone_number.state)


@dp.message(StateFilter(Sherik.phone_number))
async def set_full_name(message: Message, state: FSMContext):
    phone_number = message.contact.phone_number if message.contact.phone_number.startswith("+") else "+" + message.contact.phone_number
    if not validate_phone_number(phone_number):
        return await message.answer(text="Tog'ri formatda telefon raqam kiriting")
    await state.update_data(phone_number=phone_number)
    await message.answer(text='Manzilingizni yozing')
    await state.set_state(Sherik.location.state)    


@dp.message(StateFilter(Sherik.location))
async def set_full_name(message: Message, state: FSMContext):
    await state.update_data(location=message.text)
    await message.answer(text='Level Yani darajangizni yonizg!')
    await state.set_state(Sherik.level.state)    


@dp.message(StateFilter(Sherik.level))
async def set_full_name(message: Message, state: FSMContext):
    data = await state.get_data()
    if 'quantity' in data:
        msg = f"""Ariza: \nIsm: {data['full_name']} \nTelefon raqam: {data['phone_number']} \nJoylashuv: {data['location']} \nDaraja: {data['level']}"""

    if message.text == 'Ha':
        await bot.send_message(chat_id=6864190303, text=msg)
        return await state.clear()
    elif message.text == 'Yoq':
        await message.answer(text='Sizning buyurtma arizangiz bekor qilindi')
        return await state.clear() 

    kb = [
        [KeyboardButton(text='Ha'), KeyboardButton(text='Yoq')]
    ]

    buttons = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)

    if not message.text.isdigit():
        return await message.answer(text='qiymat faqat son bo\'lishi kerak')
    

    await state.update_data(quantity=message.text)
    msg = f"""Ariza: \nIsm: {data['full_name']} \nTelefon raqam: {data['phone_number']} \nJoylashuv: {data['location']} \nDaraja: {data['level']}"""
    await message.answer(msg, reply_markup=buttons)

    if message.text == 'Ha':
        await bot.send_message(chat_id=6864190303, text=msg)
        return await state.clear()
    elif message.text == 'Yoq':
        await message.answer(text='Sizning buyurtma arizangiz bekor qilindi')
        return await state.clear() 

    kb = [
        [KeyboardButton(text='Ha'), KeyboardButton(text='Yoq')]
    ]

    buttons = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)

    if not message.text.isdigit():
        return await message.answer(text='qiymat faqat son bo\'lishi kerak')










async def main() -> None:
    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    commands = [
        types.BotCommand(command="start", description="Botni ishga tushurish uchun bosing"),
    ]
    await bot.set_my_commands(commands)

    dp.include_router(router)

    await dp.start_polling(bot)



if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())



