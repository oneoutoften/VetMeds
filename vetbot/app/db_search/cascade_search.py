from typing import List
from app.database.models import Drug
from app.db_search.queries import DrugSearch


async def cascade_search(searcher: DrugSearch, search_term: str, limit: int = 1) -> List[Drug]:
    results = await searcher.search_by_name(search_term, limit)
    if results:
        return results

    results = await searcher.search_by_analogs(search_term, limit)
    if results:
        return results

    return await searcher.search_by_active_ingredients(search_term, limit)
