## main.py

import asyncio
from aiogram import Bot, Dispatcher  # type: ignore

from app.handlers import router


async def main():
    bot = Bot(token="6335731592:AAFP4asfevJxr-AtvZqk4Ky4Yz5CXeQ3fYA")
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот выключен")
