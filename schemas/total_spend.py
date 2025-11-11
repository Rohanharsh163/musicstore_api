# schemas/total_spend.py
from pydantic import BaseModel
from decimal import Decimal

class TotalSpend(BaseModel):
    customer_id: int
    name: str
    total_spent: Decimal
