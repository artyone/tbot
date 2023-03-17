
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Text, Command
import constants

import logging
import json
import time

with open('db.json', 'r') as f:
    data = json.load(f)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

bot: Bot = Bot(constants.API_KEY)
dp: Dispatcher = Dispatcher()



if __name__ == '__main__':
    dp.run_polling(bot)


