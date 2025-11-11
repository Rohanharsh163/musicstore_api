# dao/artist_dao.py
from typing import List
from db import get_pool
from schemas.artist import Artist

async def list_artists() -> List[Artist]:
    pool = get_pool()
    if pool is None:
        raise RuntimeError("DB pool not initialized")
    sql = "SELECT artist_id, name FROM artist ORDER BY name;"
    async with pool.acquire() as conn:
        rows = await conn.fetch(sql)
    return [Artist(artist_id=r["artist_id"], name=r["name"]) for r in rows]
