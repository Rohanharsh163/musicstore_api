# services/customer_service.py
from typing import List, Optional
from dao.customer_dao import get_invoices_for_customer, get_customer_total_spend
from schemas.invoice import Invoice

async def get_invoices(customer_id: int) -> List[Invoice]:
    return await get_invoices_for_customer(customer_id)

async def get_total_spend(customer_id: int) -> Optional[dict]:
    """
    Returns row dict with 'customer_id','name','total_spent' or None.
    """
    return await get_customer_total_spend(customer_id)
