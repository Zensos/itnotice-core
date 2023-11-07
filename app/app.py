from fastapi import FastAPI
from .routers import tasks
from .prisma import prisma
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.include_router(tasks.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup():
    await prisma.connect()

@app.on_event("shutdown")
async def shutdown():
    await prisma.disconnect()
