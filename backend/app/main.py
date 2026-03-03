from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from app.api import endpoints
from app.core.database import engine, Base

import os

# Create DB tables (in a real app, use Alembic)
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Internal CAASM Portal")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1", "http://localhost"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(endpoints.router, prefix="/api")

# Serve frontend static files if they exist
frontend_path = os.path.join(os.path.dirname(__file__), "../../frontend")
if not os.path.exists(frontend_path):
    os.makedirs(frontend_path, exist_ok=True)
    
app.mount("/", StaticFiles(directory=frontend_path, html=True), name="frontend")
