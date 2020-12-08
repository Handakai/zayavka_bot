from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.types import callback_query
import config

greet_kb = InlineKeyboardMarkup().add(InlineKeyboardButton(config.greet_kb, callback_data='1'))

rules_confiramtion_kb = InlineKeyboardMarkup().add(InlineKeyboardButton(config.rules_confirmation_kb, callback_data='1'))

applying_kb = InlineKeyboardMarkup().add(InlineKeyboardButton(config.applying[0], callback_data='true'), 
                                        InlineKeyboardButton(config.applying[1], callback_data='false'))

                            
def get_accepting_kb(user_id):
    kb = InlineKeyboardMarkup().add(InlineKeyboardButton(config.admin_applying[0], callback_data=f'true_{user_id}'), 
                                        InlineKeyboardButton(config.admin_applying[1], callback_data=f'false_{user_id}'))
    return kb

# Reddington - t.me/RichmondSeller
