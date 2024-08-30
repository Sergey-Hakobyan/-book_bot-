from logging import basicConfig, DEBUG
from asyncio import run
from aiogram import Bot, Dispatcher
from functions.command import R
basicConfig(level=DEBUG)
TOKEN = "6929158190:AAGDEtisTZtzb0ndC5eN5bZDcFxx4M7CH8c"
Bott = Bot(token = TOKEN)
Dispecher = Dispatcher()

async def main():
    try:
        await Bott.delete_webhook(drop_pending_updates = True)
        Dispecher.include_routers(R,)
        await Dispecher.start_polling(Bott)
    except Exception as f:
        print(f"failure here {f}")
run(main())

run(R)