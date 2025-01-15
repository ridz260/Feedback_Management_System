from fastapi import FastAPI
from routers import surveys, users

app = FastAPI()

app.include_router(surveys.router, prefix="/api")
app.include_router(users.router, prefix="/api")