"""Pydantic schemas for AI wildlife identifier."""

from pydantic import BaseModel, Field


class IdentifyResponse(BaseModel):
    species_name: str
    confidence_score: float = Field(ge=0, le=1)
    habitat: str
    conservation_status: str
    interesting_fact: str
