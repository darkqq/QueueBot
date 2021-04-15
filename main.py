import logging
import config
import lesson_queue
import TGCalendar.telegramcalendar as tgcalendar
import keyboards as kb
from aiogram import Bot, Dispatcher, executor, types

ADMIN_ID = 465801855

# Configure logging
logging.basicConfig(level=logging.INFO)
# Initialize bot and dispatcher
bot = Bot(token=config.TG_API_TOKEN)
dp = Dispatcher(bot)


@dp.callback_query_handler(lambda c: c.data.startswith('recall'))
async def process_callback_button1(callback_query: types.CallbackQuery):
    if callback_query.data == 'recall_yes':
        # data.collect_data('Да', callback_query.from_user.id)
        await bot.send_message(callback_query.from_user.id, 'Отлично, мы вам перезвоним')
    if callback_query.data == 'recall_no':
        # data.collect_data('Нет', callback_query.from_user.id)
        await bot.send_message(callback_query.from_user.id, 'Хорошо, приходите на праздник!')
    await bot.answer_callback_query(callback_query.id)


@dp.callback_query_handler(lambda c: c.data.startswith('lesson'))
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    # data.collect_data(callback_query.data, callback_query.from_user.id)
    username = callback_query.from_user.username
    lesson_queue.add_person(username)
    await bot.edit_message_text(text=f'@{username} выбрал {callback_query.data}',
                                chat_id=callback_query.message.chat.id,
                                message_id=callback_query.message.message_id)
    # await bot.send_message(callback_query.from_user.id, 'Пожалуйста, напишите свой номер телефона')


# @dp.callback_query_handler(lambda c: c.data == 'yes' or c.data == 'no')
# async def choose_callback(callback_query: types.CallbackQuery):
#     if callback_query.data == 'yes':
#         await bot.edit_message_text(text=f"Пожалуйста, выберите предмет",
#                                     chat_id=callback_query.message.chat.id,
#                                     message_id=callback_query.message.message_id,
#                                     reply_markup=kb.get_lessons(921703, 0, 1))
#     elif callback_query.data == 'no':
#         await bot.edit_message_text(text=f"Ясно!",
#                                     chat_id=callback_query.message.chat.id,
#                                     message_id=callback_query.message.message_id)
#     else:
#         await bot.edit_message_text(text=f"Что-то пошло не так :(",
#                                     chat_id=callback_query.message.chat.id,
#                                     message_id=callback_query.message.message_id)
#     await bot.answer_callback_query(callback_query.id)


@dp.callback_query_handler(lambda c: c.data)
async def callback_calendar(callback_query: types.CallbackQuery):
    response = tgcalendar.process_calendar_selection(bot, callback_query)
    # data.collect_data(response[2], callback_query.from_user.id)
    await response[0]
    await bot.answer_callback_query(callback_query.id)


@dp.message_handler(commands=['queue'])
async def calendar(message: types.Message):
    if message.from_user.id == ADMIN_ID:
        roflan = lesson_queue.get_queue()
        i = 0
        for person in roflan:
            print(str(i) + ". " + person)
            i += 1
        print("")
        await message.answer(roflan)
    else:
        await message.answer('Пашол нахуй!')


@dp.message_handler(commands=['calendar'])
async def calendar(message: types.Message):
    cld = tgcalendar.create_calendar()
    await message.answer('Пожалуйтса, выберите дату:', reply_markup=cld)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.answer("Здарова!\n"
                         "Я тестовый бот\n"
                         "Напиши /calendar чтобы протестировать самую свежую функцию!")


if __name__ == '__main__':
    executor.start_polling(dp)
