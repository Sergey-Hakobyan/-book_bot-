from aiogram.filters.command import Command
from aiogram import Router
from aiogram.types import Message
R = Router()


@R.message(Command("info"))
async def hi_bro(msg:Message):
    msg.reply(f"good day,{msg.from_user.full_name}!,ur id {msg.from_user.id}")