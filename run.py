import asyncio
import os
import logging

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, F
from aiogram.types import (Message, ReplyKeyboardMarkup, KeyboardButton)
from aiogram.filters import CommandStart, Command

from card_random import get_random_cards
from API import get_gpt_interpretation
from cards import init_db

load_dotenv()

init_db()

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher()

keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Получить расклад')]],
    resize_keyboard=True,
    input_field_placeholder='Нажмите на кнопку',
    one_time_keyboard=False
)


@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        f'Привет! Я твой персональный таролог,'
        f'узнай свлою судьбу! Чтобы получить расклад трех карт таро и'
        f' пояснение к нему нажми на кнопку ниже или введи команду /tarot',
        reply_markup=keyboard
    )


@dp.message(Command('tarot'))
@dp.message(F.text == 'Получить расклад')
async def send_tarot_card(message: Message):
    try:
        jpt = await get_random_cards(message)

        interpretation = await get_gpt_interpretation(jpt)
        await message.answer(interpretation)

    except Exception as e:
        await message.answer(f"Произошла ошибка: {e}")


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('exit')