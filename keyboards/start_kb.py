from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


# Функция, генерирующая клавиатуру для страницы книги
def create_main_keyboard() -> InlineKeyboardMarkup:
    """Функция для формирования главной инлайн клавиатуры"""
    button_0 = InlineKeyboardButton(text='Основные индексы ММВБ.', callback_data='moex_index')
    button_1 = InlineKeyboardButton(text='Предстоящие дивиденды.', callback_data='get_div')
    button_2 = InlineKeyboardButton(text='Валютный рынок.', callback_data='currency')
    button_3 = InlineKeyboardButton(text='Какие акции можно приобрести на определенную сумму.',
                                    callback_data='what_can_buy')
    keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(
        inline_keyboard=[[button_0], [button_1], [button_2], [button_3]])
    # Возвращаем объект инлайн-клавиатуры
    return keyboard
