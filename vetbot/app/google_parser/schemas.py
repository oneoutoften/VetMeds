from dataclasses import dataclass
from typing import Optional

@dataclass
class Drug:
    name: str
    active_ingredients: str
    analogs:  str
    dosages: str
    description: str
    notes: Optional[str]=None