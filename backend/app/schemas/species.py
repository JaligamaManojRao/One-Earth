"""Pydantic schemas for species endpoints."""

from pydantic import BaseModel, ConfigDict


class SpeciesBase(BaseModel):
    name: str
    scientific_name: str
    habitat: str
    conservation_status: str
    population_trend: str
    description: str
    image_url: str
    interesting_fact: str | None = None


class SpeciesResponse(SpeciesBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


class SpeciesListResponse(BaseModel):
    items: list[SpeciesResponse]
    total: int
    page: int
    page_size: int
    total_pages: int
