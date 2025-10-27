from aiogram import F,Router
from aiogram.filters import Command,CommandStart
from aiogram.types import Message
from lexicon.lexicon import LEXICON_RU
from services.services import get_weather



user_router=Router()


@user_router.message(CommandStart())
async def process_start_command(message:Message):
    await message.answer(text=LEXICON_RU["/start"])


@user_router.message(Command(commands="help"))
async def process_help_command(message:Message):
    await message.answer(text=LEXICON_RU["/help"])


@user_router.message(Command(commands=["weather","погода"]))
async def process_weather_answer(message:Message):
    await message.answer(await get_weather(message.text.lower().split(maxsplit=1)[-1]))
