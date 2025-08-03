import asyncio
from app.database.connection import database
from app.db_search import DrugSearch
from app.db_search.cascade_search import cascade_search


async def print_search_results(searcher: DrugSearch, search_term: str):
    results = await cascade_search(searcher, search_term)

    if not results:
        print('Nothing found')
        return

    for drug in results:
        print(f'{drug.name}\n{drug.analogs}\n{drug.active_ingredients}\n{drug.dosages}\n{drug.description}\n{drug.notes}')

async def test_search():
    await database.connect()
    searcher = DrugSearch(database)

    try:
        await print_search_results(searcher, 'адреналин')
    except Exception as e:
        print(f'Error {e}')
    finally:
        await database.engine.dispose()

if __name__ == '__main__':
    asyncio.run(test_search())