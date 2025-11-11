# routers/customers.py
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from typing import List
from db import get_pool
from services.customer_service import get_invoices, get_total_spend
from schemas.invoice import Invoice
from schemas.total_spend import TotalSpend

router = APIRouter(prefix="/customers", tags=["customers"])

@router.get("/{customer_id}/invoices", response_model=List[Invoice])
async def customer_invoices(customer_id: int):
    """Return all invoices for a customer, or 404 with {"error":"Customer not found"}"""
    pool = get_pool()
    if pool is None:
        return JSONResponse(status_code=500, content={"error": "db pool not initialized"})
    # Check existence
    async with pool.acquire() as conn:
        exists = await conn.fetchval("SELECT 1 FROM customer WHERE customer_id = $1", customer_id)
        if not exists:
            return JSONResponse(status_code=404, content={"error": "Customer not found"})
    invoices = await get_invoices(customer_id)
    return invoices

@router.get("/{customer_id}/total_spend", response_model=TotalSpend)
async def customer_total_spend(customer_id: int):
    """Return total spent and name of customer, or 404 with exact error JSON."""
    pool = get_pool()
    if pool is None:
        return JSONResponse(status_code=500, content={"error": "db pool not initialized"})
    row = await get_total_spend(customer_id)
    if not row:
        return JSONResponse(status_code=404, content={"error": "Customer not found"})
    # row contains Decimal for total_spent, already in numeric format
    return TotalSpend(customer_id=row["customer_id"], name=row["name"], total_spent=row["total_spent"])
