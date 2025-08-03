from sqlalchemy.ext.asyncio import AsyncSession
from app.database.models import Drug as DrugModel
from app.google_parser.schemas import Drug
from sqlalchemy.dialects.postgresql import insert

async def load_to_db(session: AsyncSession, drugs: list[Drug]):
    if not drugs:
        return

    values = [{
        'name':drug.name,
        'active_ingredients': drug.active_ingredients,
        'analogs': drug.analogs,
        'dosages': drug.dosages,
        'description': drug.description,
        'notes': drug.notes
    } for drug in drugs]

    stmt = insert(DrugModel).values(values)
    stmt = stmt.on_conflict_do_nothing(index_elements=['name'])

    await session.execute(stmt)
    # db_drugs = [
    #     DrugModel(
    #     name=drug.name,
    #     active_ingredients=drug.active_ingredients,
    #     analogs=drug.analogs,
    #     dosages=drug.dosages,
    #     description=drug.description,
    #     notes=drug.notes
    #     )
    #     for drug in drugs
    # ]
    # session.add_all(db_drugs)
    await session.commit()