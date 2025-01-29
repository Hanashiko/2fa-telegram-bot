import asyncio
from create_bot import bot, dp
from handlers.general import register_general_handlers
from handlers.admin import register_admin_handlers

async def main():
    register_admin_handlers(dp)
    register_general_handlers(dp)

    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())