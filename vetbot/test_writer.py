import asyncio
from config import config
from app.database.connection import database
from app.google_parser.parser import parse_google_doc
from app.google_parser.loader import load_to_db

async def test_pipeline():
    try:
        await database.connect()
        await database.create_tables()

        print(f'Parsing document')
        drugs = await parse_google_doc(config.GOOGLE_DOC_ID)
        print(f'Found {len(drugs)} drugs')

        if not drugs:
            print('Doc empty')
            return

        async with database.get_session() as session:
            await load_to_db(session, drugs)
            print('Drugs loaded to db')

    except Exception as e:
        print(f'Error {e}')
    finally:
        await database.engine.dispose()

if __name__ == '__main__':
    asyncio.run(test_pipeline())