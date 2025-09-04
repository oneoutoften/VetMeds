import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties

from app.services.handlers import router
from app.database.connection import database
from config import config

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filename='bot.log',
    filemode='a'
)

logger = logging.getLogger(__name__)


async def main():
    try:
        logger.info('Connecting to DB...')
        await database.connect()
        logger.info('DB connected.')

        logger.info('Initializing bot...')
        bot = Bot(
            token=config.TOKEN,
            default=DefaultBotProperties(
                parse_mode='HTML'
            )
        )
        logger.info('Bot initialization completed.')

        dp = Dispatcher()
        dp.include_router(router)

        logger.info("Starting bot polling...")
        await dp.start_polling(bot)

    except Exception as e:
        logger.error(F'Error starting bot: {e}')
        raise


    finally:
        if hasattr(database, 'engine') and database.engine:
            await database.engine.dispose()
            logger.info('Database connection closed.')
        logger.info('Bot stopped.')

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        print(f"Fatal error outside main: {e}")