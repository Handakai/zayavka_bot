import asyncio
import logging
import aiogram

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext





import config
import keyboards as kb
import states


logging.basicConfig(level=logging.INFO)


bot = Bot(token=config.API_TOKEN)
memory_storage = MemoryStorage()
dp = Dispatcher(bot, storage=memory_storage)

@dp.message_handler(commands=['start'], state='*')
async def send_welcome(message: types.Message):
    if message.from_user.id == config.admin_id:
        await message.answer('Admin chat configured')
        return
    await message.answer(config.first_message, reply_markup=kb.greet_kb)
    await states.main.waiting_for_greet.set()

@dp.callback_query_handler(state=states.main.waiting_for_greet)
async def send_rules(c: types.CallbackQuery):
    await c.answer()
    await bot.edit_message_text(config.rules, c.from_user.id, c.message.message_id, reply_markup=kb.rules_confiramtion_kb)
    await states.main.waiting_for_rules_confirmation.set()


@dp.callback_query_handler(state=states.main.waiting_for_rules_confirmation)
async def send_1_question(c: types.CallbackQuery):
    await c.answer()
    await bot.edit_message_text(config.rules_with_confirmation, c.from_user.id, c.message.message_id, reply_markup=None)
    await c.message.answer(config.question_1, parse_mode='Markdown')
    await states.main.question_1.set()

@dp.message_handler(state=states.main.question_1)
async def send_2_question(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data['answers'] = [message.text]
    await message.answer(config.question_2)
    await states.main.question_2.set()


@dp.message_handler(state=states.main.question_2)
async def send_3_question(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data['answers'].append(message.text)
    await message.answer(config.question_3)
    await states.main.question_3.set()

@dp.message_handler(state=states.main.question_3)
async def send_4_question(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data['answers'].append(message.text)
    await message.answer(config.question_4)
    await states.main.question_4.set()

@dp.message_handler(state=states.main.question_4)
async def send_summary_confiramtion(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data['answers'].append(message.text)
        answers = data['answers']

        text = config.summary.format(answers = answers)
        await message.answer('📌 *Ваша заявка готова к отправке*\n\n' + text, reply_markup=kb.applying_kb, parse_mode='Markdown')


        data['summary'] = text

    await states.main.summary_confirmation.set()


@dp.callback_query_handler(state=states.main.summary_confirmation)
async def end_regestration(c:types.CallbackQuery, state=FSMContext):
    await c.answer()
    await bot.edit_message_reply_markup(c.from_user.id, c.message.message_id, reply_markup=None)
    if c.data == 'true':
        async with state.proxy() as data:
            summary = data['summary']

        await c.message.answer(config.for_true)
        await bot.send_message(config.admin_id, 
                                config.text_for_admin + f'[{c.from_user.first_name}](tg://user?id={c.from_user.id})\n\n' + summary, 
                                parse_mode='Markdown', reply_markup=kb.get_accepting_kb(c.from_user.id))
        await state.finish()
        return

    else:
        await c.message.answer(config.for_false)
        await state.finish()
        return
    

@dp.callback_query_handler(lambda c: c.from_user.id == config.admin_id)
async def send_final_message(c:types.CallbackQuery):
    await c.answer()
    try:
        options = c.data.split('_')
    except:
        return

    if options[0] == 'true':
        await bot.send_message(int(options[1]), config.message_for_user_if_accepted, parse_mode='Markdown')
        await bot.edit_message_reply_markup(config.admin_id, c.message.message_id, reply_markup=None)
    else:
        await bot.delete_message(config.admin_id, c.message.message_id)


@dp.message_handler(commands=['clear'], state = '*')
async def clear(message: types.Message):
    await message.answer('Keyboards cleared', reply_markup=kb.ReplyKeyboardRemove())    


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

# Reddington - t.me/RichmondSeller
