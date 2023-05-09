from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo

bot = Bot(token='6215708830:AAGKSA7XfghK_TMBu3obT8-Vs7dbyk5Or2s')

dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.add(types.KeyboardButton('Открыть веб страницу', web_app=WebAppInfo(url='https://hotel-bot.site/')))
    await message.answer('Привет мой друг!', reply_markup=keyboard)

@dp.message_handler(content_types=['web_app_data'])
async def web_app(message: types.Message):
    print('yes')

executor.start_polling(dp)

