from aiogram import Bot,types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

import os 



bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)


@dp.message_handler()
async def echo_send(message:types.Message):
    if message.text == 'Привет':
        await message.answer('И тебе привет')


executor.start_polling(dp,skip_updates=True)
