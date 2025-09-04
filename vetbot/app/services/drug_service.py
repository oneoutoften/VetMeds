from app.db_search import DrugSearch
from app.db_search.cascade_search import cascade_search
from app.database.connection import database


class DrugService:
    def __init__(self):
        self.drug_search = DrugSearch(database)

    async def search_drug(self, search_term: str) -> list:
        return await cascade_search(self.drug_search, search_term)

    async def format_drug_response(self, drugs: list) -> str:
        if not drugs:
            return 'Препарат не найден. Попробуйте другой запрос.'

        response = []
        for drug in drugs:
            drug_info = f"💊 <b>{drug.name}</b>\n\n"

            if drug.active_ingredients:
                drug_info += f"<b>Активные вещества:</b> {drug.active_ingredients}\n"
            if drug.analogs:
                drug_info += f"<b>Аналоги:</b> {drug.analogs}\n"
            if drug.dosages:
                drug_info += f"<b>Дозировки:</b>\n{drug.dosages}\n"
            if drug.description:
                drug_info += f"<b>Описание:</b>\n{drug.description}\n"
            if drug.notes:
                drug_info += f"<b>Примечания:</b>\n{drug.notes}\n"
            response.append(drug_info)

        return response[0]

drug_service = DrugService()