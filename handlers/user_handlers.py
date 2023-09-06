from aiogram import Router
from aiogram.filters import Command, CommandStart, Text
from aiogram.types import CallbackQuery, Message


from config_data.config import Config, load_config
from keyboards.start_kb import create_main_keyboard
from lexicon.lexicon import LEXICON
from services.div_calendar import get_div_string
from database.database import users_db, users_feedback_db
from services.what_can_buy import get_all_info_on_stocks, get_list_stocks
from services.currency_rate import get_all_currency_rate, get_all_currency
from services.common_features import get_message_max_len_in_dict, get_message_max_len_in_list
from services.index_moex import get_ind_info, get_main_indexes


router: Router = Router()
config: Config = load_config()


# Этот хэндлер будет срабатывать на команду "/start" -
# отправлять ему приветственное сообщение и отправлять
# основную клавиатуру
@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text=LEXICON[message.text],
        reply_markup=create_main_keyboard())


# Этот хэндлер будет срабатывать на команду "/keyboard" -
# отправлять ему приветственное сообщение и отправлять
# основную клавиатуру
@router.message(Command(commands='keyboard'))
async def process_start_command(message: Message):
    await message.answer(text='Возможности бота, узнать:', reply_markup=create_main_keyboard())


# Этот хэндлер будет срабатывать на команду "/help"
# и отправлять пользователю сообщение со списком доступных команд в боте
@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(LEXICON[message.text])


# Этот хэндлер будет срабатывать на команду "/feedback"
# и отправлять пользователю сообщение со списком доступных команд в боте
@router.message(Command(commands='feedback'))
async def process_help_command(message: Message):
    users_feedback_db.append(message.from_user.id)
    await message.answer(LEXICON[message.text])


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки "основные индексы ММВБ."
@router.callback_query(Text(text='moex_index'))
async def process_forward_press(callback: CallbackQuery):
    index_info = get_main_indexes(get_ind_info()).strip()
    await callback.message.answer(text=index_info)
    await callback.answer()


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки "Предстоящие дивиденды."
@router.callback_query(Text(text='get_div'))
async def process_forward_press(callback: CallbackQuery):
    for string in get_message_max_len_in_list(get_div_string()):
        await callback.message.answer(text=string)
    await callback.answer(
        text="Идет сбор информации, это может занять некоторое время.",
        show_alert=True)


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки "Валютный рынок."
@router.callback_query(Text(text='what_can_buy'))
async def process_forward_press(callback: CallbackQuery):
    await callback.message.answer(text='<b>Введите сумму, с точностью до рубля:</b>')
    users_db.append(callback.from_user.id)
    await callback.answer()


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки "Какие акции возможно приобрести на определенную сумму."
@router.callback_query(Text(text='currency'))
async def process_forward_press(callback: CallbackQuery):
    for info in get_message_max_len_in_list(get_all_currency(get_all_currency_rate())):
        await callback.message.answer(info)
    users_db.append(callback.from_user.id)
    await callback.answer(
        text="Идет сбор информации, это может занять некоторое время.\n"
             "В связи с большим объемом информация может быть доставлена в нескольких сообщениях",
        show_alert=True)


@router.message(lambda x: x.text and x.text.isdigit())
async def process_numbers_answer(message: Message):
    if message.from_user.id in users_db:
        await message.answer('Идет сбор информации, это может занять некоторое время.\n'
                             'В связи с большим объемом информация может быть доставлена в нескольких сообщениях', )
        for i in get_message_max_len_in_dict(get_list_stocks(get_all_info_on_stocks(), int(message.text))):
            await message.answer(i.strip())
    else:
        await message.answer('Некорректное сообщение.')


@router.message(lambda x: x.text)
async def process_numbers_answer(message: Message):
    if message.from_user.id in users_feedback_db:
        await message.answer('Спасибо за Ваше мнение. Мы постараемся учесть его при дальнейшей модернизации бота', )
        admin_id = 2102532729
        await message.forward(chat_id=admin_id, text=f"Новый отзыв от {str(message.from_user.id)}:\n{message.text}")
    else:
        await message.answer('Некорректное сообщение.')
