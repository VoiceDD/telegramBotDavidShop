from create_bot import bot, dp

from aiogram import types
from keyboard import ikbSideSellersPanel

from DatabaseHandler import getSellersID
from LoggerHandler import SellerLogger, InitLogger


# @dp.message_handler(commands=['login'], state=None)
async def selLogin(message: types.Message):
    sellers = getSellersID()
    if str(message.from_user.id) in sellers:
        SellerLogger.info(f'{message.from_user.username} entered admin panel')
        await bot.send_message(message.chat.id, 'Успешный вход',
                               reply_markup=ikbSideSellersPanel)
    else:
        await message.reply('У вас нет прав.')


def registerHandlers():
    dp.register_message_handler(selLogin, commands=['login'], state=None)
    InitLogger.info('sideSellers handlers registered')
