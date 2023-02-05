from aiogram import Router, types, html, F

router = Router()


@router.message(F.chat.type == "private", commands="start")
async def cmd_start(message: types.Message):
    """
    /start command handler for private chats
    :param message: Telegram message with "/start" command
    """
    await message.answer(f"Your Telegram ID is {html.code(message.chat.id)}\n ")


@router.message(F.chat.type == "private", commands="id")
async def cmd_id_pm(message: types.Message):
    """
    /id command handler for private messages
    :param message: Telegram message with "/id" command
    """
    await message.answer(f"Your Telegram ID is {html.code(message.from_user.id)}\n  Name is {html.code(message.from_user.username)}")


@router.message(F.chat.type.in_({"group", "supergroup"}), commands="id")
async def cmd_id_groups(message: types.Message):
    """
    /id command handler for (super)groups
    :param message: Telegram message with "/id" command
    """
    msg = [f"This {message.chat.type} chat ID is {html.code(message.chat.id)}"]
    if message.sender_chat is None:
        msg.append(f"Your Telegram ID is {html.code(message.from_user.id)}")
    else:
        msg.append(f"And you've sent this message as channel with ID {html.code(message.sender_chat.id)}")
    await message.reply("\n".join(msg))


@router.message(commands="help")
async def cmd_help(message: types.Message):
    """
    /help command handler for all chats
    :param message: Telegram message with "/help" command
    """
    await message.answer(
        'Use this bot to get ID for different entities across Telegram:\n'
   )
