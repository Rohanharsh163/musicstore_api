# dao/customer_dao.py
from typing import List, Optional
from decimal import Decimal
from db import get_pool
from schemas.invoice import Invoice

async def get_invoices_for_customer(customer_id: int) -> List[Invoice]:
    """
    Fetches all invoices for a given customer.
    Each invoice includes ID, date (ISO format), and total.
    """
    pool = get_pool()
    if pool is None:
        raise RuntimeError("DB pool not initialized")

    sql = """
    SELECT invoice_id, invoice_date, total
    FROM invoice
    WHERE customer_id = $1
    ORDER BY invoice_date DESC;
    """
    async with pool.acquire() as conn:
        rows = await conn.fetch(sql, customer_id)

    invoices = []
    for r in rows:
        inv_date = r["invoice_date"]
        # Convert invoice_date to ISO string for JSON serialization
        inv_date_str = inv_date.isoformat() if inv_date is not None else None
        invoices.append(
            Invoice(
                invoice_id=r["invoice_id"],
                invoice_date=inv_date_str,
                total=r["total"]
            )
        )
    return invoices


async def get_customer_total_spend(customer_id: int) -> Optional[dict]:
    """
    Returns a dictionary with keys: customer_id, name, total_spent
    or None if the customer does not exist.
    """
    pool = get_pool()
    if pool is None:
        raise RuntimeError("DB pool not initialized")

    sql = """
    SELECT
        c.customer_id,
        c.first_name || ' ' || c.last_name AS name,
        COALESCE(SUM(i.total), 0)::numeric(10,2) AS total_spent
    FROM customer c
    LEFT JOIN invoice i ON i.customer_id = c.customer_id
    WHERE c.customer_id = $1
    GROUP BY c.customer_id, c.first_name, c.last_name;
    """
    async with pool.acquire() as conn:
        row = await conn.fetchrow(sql, customer_id)

    # Returns None if no matching customer exists
    return row
