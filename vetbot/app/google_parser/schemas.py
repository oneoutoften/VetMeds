from dataclasses import dataclass
from typing import List, Optional

@dataclass
class Drug:
    name: str
    active_ingredient: str
    analogs: List[str]
    dosages: str
    description: str
    notes: Optional[str]=None