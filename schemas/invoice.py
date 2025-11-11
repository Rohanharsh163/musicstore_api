# schemas/invoice.py
from pydantic import BaseModel
from decimal import Decimal
from typing import Optional

class Invoice(BaseModel):
    invoice_id: int
    invoice_date: Optional[str]   # allow None
    total: Decimal
