# db.py
import os
import asyncpg
from typing import Optional

# Read DB configuration from environment variables with safe defaults (provided read-only credentials)
DB_HOST = os.getenv("DB_HOST", "aws-1-ap-southeast-1.pooler.supabase.com")
DB_PORT = int(os.getenv("DB_PORT", 6543))
DB_NAME = os.getenv("DB_NAME", "postgres")
DB_USER = os.getenv("DB_USER", "bitshuser_ro.ziyfpepffnykprwwljnc")
DB_PASS = os.getenv("DB_PASS", "weloveancfood")
DB_POOL_MAX = int(os.getenv("DB_POOL_MAX", 10))

_pool: Optional[asyncpg.pool.Pool] = None

async def create_pool():
    global _pool
    if _pool is None:
        _pool = await asyncpg.create_pool(
            host=DB_HOST,
            port=DB_PORT,
            user=DB_USER,
            password=DB_PASS,
            database=DB_NAME,
            max_size=DB_POOL_MAX,
        )
    return _pool

async def close_pool():
    global _pool
    if _pool is not None:
        await _pool.close()
        _pool = None

def get_pool():
    """Return the global pool. Make sure create_pool() was awaited on startup."""
    return _pool
