import importlib
import re
from typing import Optional, List

from telegram import Message, Chat, Update, Bot, User
from telegram import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.error import Unauthorized, BadRequest, TimedOut, NetworkError, ChatMigrated, TelegramError
from telegram.ext import CommandHandler, Filters, MessageHandler, CallbackQueryHandler
from telegram.ext.dispatcher import run_async, DispatcherHandlerStop
from telegram.utils.helpers import escape_markdown

from tg_bot import dispatcher, updater, TOKEN, WEBHOOK, OWNER_ID, DONATION_LINK, CERT_PATH, PORT, URL, LOGGER, \
    ALLOW_EXCL
# needed to dynamically load modules
# NOTE: Module order is not guaranteed, specify that in the config file!
from tg_bot.modules import ALL_MODULES
from tg_bot.modules.helper_funcs.chat_status import is_user_admin
from tg_bot.modules.helper_funcs.misc import paginate_modules

PM_START_TEXT = """

ഹായ് {},
ഈ ബോട്ട് Ma മൂവീസ് ഗ്രൂപ്പിലേക്ക് ഉള്ളത് എന്ന് ഇനി വീണ്ടും വീണ്ടും പറയണോ??
അപ്പോ പിന്നെ എന്തിനാ വീണ്ടും വീണ്ടും സ്റ്റാർട്ട് കുത്തി കളിക്കാൻ വരുന്നേ... ആ സൈഡിലോട്ട് എങ്ങാനും മാറി ഇരിക്ക്‌ ഇനി🤭🤭
@Ma_movies_group
"""

