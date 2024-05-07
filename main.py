import logging

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart
from aiogram.types import (Message, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery) 



from config_data.config import Config, load_config
from lexicon.lexicon_ru import LEXICON_RU
from lexicon.lexicon_en import LEXICON_EN
from lexicon.lexicon_es import LEXICON_ES
from middlewares.i18n import TranslatorMiddleware
from typing import Any, Awaitable, Callable, Dict
from currency import buying_price, selling_price


logging.basicConfig(level=logging.DEBUG, format="[%(asctime)s] #%(levelname)-8s %(filename)s:%(lineno)d - %(name)s - %(message)s")

logger = logging.getLogger(__name__)
logger.info('Starting bot')


config: Config = load_config()

bot = Bot(token=config.tg_bot.token)
dp = Dispatcher()


translations ={
    'default': 'ru',
    'en': LEXICON_EN,
    'es': LEXICON_ES,
    'ru': LEXICON_RU
}


@dp.message(CommandStart())
async def procces_start_command(message: Message, i18n: dict[str, str]):
    button = InlineKeyboardButton(text=i18n.get('show'), callback_data='курс отображен')
    markup = InlineKeyboardMarkup(inline_keyboard=[[button]], resize_keyboard=True)

    await message.answer(text=i18n.get('/start'), reply_markup=markup)
  

@dp.callback_query(F.data == 'курс отображен')
async def procces_buttons_press(callback: CallbackQuery, i18n: dict[str, str]):
    button_1 = InlineKeyboardButton(text=i18n.get('buy'), callback_data='курс покупки')
    button_2 = InlineKeyboardButton(text=i18n.get('sell'), callback_data='курс продажи')
    markup_1 = InlineKeyboardMarkup(inline_keyboard=[[button_1], [button_2]], resize_keyboard=True)

    await callback.message.edit_text(text=i18n.get('show'),reply_markup=markup_1)

@dp.callback_query(F.data == 'курс покупки')
async def procces_buttons_press(callback: CallbackQuery, i18n: dict[str, str]):
    button_3 = InlineKeyboardButton(text=i18n.get('show'), callback_data='курс отображен')
    markup_2 = InlineKeyboardMarkup(inline_keyboard=[[button_3]], resize_keyboard=True)
    await callback.message.edit_text(
        text=buying_price,
        reply_markup=markup_2, 
    )

@dp.callback_query(F.data == 'курс продажи')
async def procces_buttons_press(callback: CallbackQuery, i18n:dict[str, str]):
    button_4 = InlineKeyboardButton(text=i18n.get('show'), callback_data='курс отображен')
    markup_3 = InlineKeyboardMarkup(inline_keyboard=[[button_4]], resize_keyboard=True)
    await callback.message.edit_text(
        text=selling_price,
        reply_markup=markup_3,    
    )

@dp.message()
async def procces_other_commands(message: Message, i18n:dict[str,str]):
    button_5 = InlineKeyboardButton(text=i18n.get('show'), callback_data='курс отображен')
    markup_4 = InlineKeyboardMarkup(inline_keyboard=[[button_5]], resize_keyboard=True)
    await message.answer (text=i18n.get('pressed show'), reply_markup=markup_4)

logger.info('Подключаем мидлвари')
dp.update.outer_middleware(TranslatorMiddleware())

if __name__== '__main__':
    dp.run_polling(bot, _translations=translations)

