"""Species API routes."""

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.species import SpeciesListResponse, SpeciesResponse
from app.services import species_service

router = APIRouter(prefix="/species", tags=["Species"])


@router.get("", response_model=SpeciesListResponse)
def list_species(
    page: int = Query(1, ge=1),
    page_size: int = Query(12, ge=1, le=50),
    habitat: str | None = None,
    conservation_status: str | None = None,
    db: Session = Depends(get_db),
):
    return species_service.get_species_list(
        db, page=page, page_size=page_size, habitat=habitat, conservation_status=conservation_status
    )


@router.get("/search", response_model=SpeciesListResponse)
def search_species(
    q: str = Query(..., min_length=1),
    page: int = Query(1, ge=1),
    page_size: int = Query(12, ge=1, le=50),
    db: Session = Depends(get_db),
):
    return species_service.search_species(db, q=q, page=page, page_size=page_size)


@router.get("/{species_id}", response_model=SpeciesResponse)
def get_species(species_id: int, db: Session = Depends(get_db)):
    species = species_service.get_species_by_id(db, species_id)
    if not species:
        raise HTTPException(status_code=404, detail="Species not found")
    return SpeciesResponse.model_validate(species)
