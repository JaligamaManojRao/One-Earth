"""One Earth API — FastAPI application entry point."""

from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.database.database import Base, SessionLocal, engine
from app.database.seed import SPECIES_DATA, STORIES_DATA, serialize_story
from app.models.species import Species
from app.models.story import Story
from app.routers import identify, species, stories


def seed_database():
    """Populate database with sample wildlife data if empty or outdated."""
    db = SessionLocal()
    try:
        expected_species = len(SPECIES_DATA)
        expected_stories = len(STORIES_DATA)
        species_count = db.query(Species).count()
        stories_count = db.query(Story).count()

        if species_count != expected_species or stories_count != expected_stories:
            db.query(Story).delete()
            db.query(Species).delete()
            db.commit()
            species_count = 0
            stories_count = 0

        if species_count == 0:
            for item in SPECIES_DATA:
                db.add(Species(**item))
            db.commit()

        if stories_count == 0:
            for item in STORIES_DATA:
                db.add(Story(**serialize_story(item)))
            db.commit()
    finally:
        db.close()


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    seed_database()
    yield


app = FastAPI(
    title="One Earth API",
    description="REST API for wildlife, conservation stories, and AI species identification",
    version="1.0.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origin_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(species.router)
app.include_router(stories.router)
app.include_router(identify.router)


@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "One Earth API"}
