"""SQLAlchemy model for wildlife species."""

from sqlalchemy import Column, Integer, String, Text

from app.database.database import Base


class Species(Base):
    __tablename__ = "species"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(120), nullable=False, index=True)
    scientific_name = Column(String(160), nullable=False)
    habitat = Column(String(80), nullable=False, index=True)
    conservation_status = Column(String(40), nullable=False, index=True)
    population_trend = Column(String(40), nullable=False)
    description = Column(Text, nullable=False)
    image_url = Column(String(500), nullable=False)
    interesting_fact = Column(Text, nullable=True)
