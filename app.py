# app.py
import uvicorn
from fastapi import FastAPI
from db import create_pool, close_pool
from routers.artists import router as artists_router
from routers.albums import router as albums_router
from routers.customers import router as customers_router

app = FastAPI(title="Music Store API - Phase 2")

# include routers
app.include_router(artists_router)
app.include_router(albums_router)
app.include_router(customers_router)

@app.on_event("startup")
async def startup_event():
    await create_pool()

@app.on_event("shutdown")
async def shutdown_event():
    await close_pool()

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000)
