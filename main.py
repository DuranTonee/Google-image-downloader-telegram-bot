from aiogram.utils import executor
import telegram_bot
from create_bot import dp

telegram_bot.register_handlers(dp)

executor.start_polling(dp, skip_updates=True)
