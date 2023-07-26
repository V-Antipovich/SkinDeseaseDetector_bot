from aiogram import types
from aiogram.dispatcher import FSMContext
import messages
from predictor import predict_class, model
from states import States


async def welcome(msg: types.Message):
    await States.image.set()
    await msg.reply(messages.start)


async def image_handler(msg: types.Message, state: FSMContext):
    images = msg.photo

    image = images[-1]
    path = f"{msg.from_user.id}.jpeg"
    await image.download(path)

    prediction = predict_class(path, model=model)  # utils.prepare_image(path)

    await msg.reply(messages.prediction.format(prediction))
    await msg.reply(messages.another)


async def document_handler(msg: types.Message, state: FSMContext):
    await msg.reply("Это не фото.")


async def text_handler(msg: types.Message, state: FSMContext):
    await msg.reply("Это не фото.")
