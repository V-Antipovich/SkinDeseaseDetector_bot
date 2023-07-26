from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from handlers import welcome, image_handler, document_handler, text_handler
from states import States
from config import bot_token

bot = Bot(token=bot_token)
dp = Dispatcher(bot, storage=MemoryStorage())

dp.register_message_handler(welcome, commands=["start"], state="*")
dp.register_message_handler(image_handler, state=States.image, content_types="photo")
dp.register_message_handler(document_handler, state=States.image, content_types="document")
dp.register_message_handler(text_handler, state=States.image, content_types="text")


if __name__ == "__main__":
    executor.start_polling(dp)
