import logging
import os
from telegram.ext import Application, CommandHandler, MessageHandler, filters, InlineQueryHandler
from telegram import __version__ as TG_VER
from src.commands import echo, help_command, inline_query, start
from decouple import config

try:
  from telegram import __version_info__
except ImportError:
  __version_info__ = (0,0,0,0,0)
  
if __version_info__ < (20, 0, 0, "alpha", 1):
  raise RuntimeError(
    f"This example is not compatible with your current PTB version {TG_VER}. To view the "
    f"{TG_VER} version of this example, "
    f"visit https://docs.python-telegram-bot.org/en/v{TG_VER}/examples.html"
  )

logging.basicConfig(
  format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO,
)
logger = logging.getLogger(__name__)

def main() -> None:
  """Start the bot."""
  # Create the Application and pass it your bot's token.
  application = Application.builder().token(config('TOKEN')).build()

  # on different commands - answer in Telegram
  application.add_handler(CommandHandler("start", start))
  application.add_handler(CommandHandler("help", help_command))
  
  application.add_handler(InlineQueryHandler(inline_query))
  
  application.run_polling()
  
if __name__ == "__main__":
  main()