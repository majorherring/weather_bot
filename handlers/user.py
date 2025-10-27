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


@user_router.message(Command(commands="weather"))
async def process_weather_answer(message:Message):
    await message.answer(await get_weather(message.text.lower().split(maxsplit=1)[-1]))




"""
@user_router.message(
    F.text.in_([LEXICON_RU["rock"],LEXICON_RU["paper"],LEXICON_RU["scissors"]])
)


async def process_game_button(message:Message):
    bot_choice=get_bot_choice()
    await message.answer(text=f"{LEXICON_RU["bot_choice"]} - {LEXICON_RU[bot_choice]}")
    winner=get_winner(message.text,bot_choice)

    if winner=="user_won":
        message_effect_id="5046509860389126442"
    else:
        message_effect_id=None
    await message.answer(
        text=LEXICON_RU[winner],
        message_effect_id=message_effect_id,
        reply_markup=yes_no_kb,
    )
"""