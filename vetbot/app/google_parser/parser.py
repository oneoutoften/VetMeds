from dataclasses import dataclass
from typing import List, Optional
from app.google_parser.schemas import Drug
from app.google_parser.google_docs import GoogleDocsReader
from config import config


async def parse_google_doc(document_id: str) -> List[Drug]:
    reader = GoogleDocsReader()
    text = reader.get_text(document_id)
    return parse_text(text)

def parse_text(text:str) -> List[Drug]:
    drugs = []
    blocks = [block.strip() for block in text.strip().split('###') if block.strip()]

    for block in blocks:
        drug_data = {
            'name':'',
            'active_ingredients':'',
            'analogs':'',
            'dosages':'',
            'description':'',
            'notes':''
        }

        current_field = None
        for line in block.split('\n'):
            line = line.strip()
            if not line: continue

            if line.startswith('Название:'):
                current_field = 'name'
                drug_data[current_field] = line.split(':', 1)[1].strip()
            elif line.startswith('Активные вещества:'):
                current_field = 'active_ingredients'
                drug_data[current_field] = line.split(':', 1)[1].strip()
            elif line.startswith('Аналоги:'):
                current_field = 'analogs'
                drug_data[current_field] = line.split(':', 1)[1].strip()
            elif line.startswith('Дозировки:'):
                current_field = 'dosages'
                drug_data[current_field] = line.split(':', 1)[1].strip()
            elif line.startswith('Описание:'):
                current_field = 'description'
                drug_data[current_field] = line.split(':', 1)[1].strip()
            elif line.startswith('Примечания:'):
                current_field = 'notes'
                drug_data[current_field] = line.split(':', 1)[1].strip()
            else:
                if current_field and current_field in ['description','notes','dosages']:
                    drug_data[current_field] += '\n' + line

        if drug_data['name']:
            drugs.append(Drug(**drug_data))
    return drugs