from aiogram import Router
from aiogram.types import Message

router: Router = Router()


# Этот хэндлер будет реагировать на любые сообщения пользователя,
# не предусмотренные логикой работы бота
@router.message()
async def send_echo(message: Message):
    await message.answer(f'Некорректное сообщение. {message.text}.\n '
                         f'Для отправки отзывов и предложений сначала нажмите /feedback в меню бота.\n')
