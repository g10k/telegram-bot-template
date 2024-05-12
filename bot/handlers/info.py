from aiogram import Router, types
from aiogram.filters import Command
from aiogram.utils.i18n import gettext as _, get_i18n

router = Router(name="info")


@router.message(Command(commands=["info", "help", "about"]))
async def info_handler(message: types.Message) -> None:
    """Information about bot."""
    await message.answer(_("about"))
