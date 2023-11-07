from fastapi import FastAPI
from .routers import tasks
from .prisma import prisma

app = FastAPI()
app.include_router(tasks.router)

@app.on_event("startup")
async def startup():
    await prisma.connect()

@app.on_event("shutdown")
async def shutdown():
    await prisma.disconnect()
