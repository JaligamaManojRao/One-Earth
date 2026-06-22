"""Business logic for species queries."""

import math

from sqlalchemy.orm import Session

from app.models.species import Species
from app.schemas.species import SpeciesListResponse, SpeciesResponse


def get_species_list(
    db: Session,
    page: int = 1,
    page_size: int = 12,
    habitat: str | None = None,
    conservation_status: str | None = None,
) -> SpeciesListResponse:
    query = db.query(Species)

    if habitat:
        query = query.filter(Species.habitat.ilike(f"%{habitat}%"))
    if conservation_status:
        query = query.filter(Species.conservation_status.ilike(conservation_status))

    total = query.count()
    total_pages = max(1, math.ceil(total / page_size))
    offset = (page - 1) * page_size

    items = query.order_by(Species.name).offset(offset).limit(page_size).all()

    return SpeciesListResponse(
        items=[SpeciesResponse.model_validate(s) for s in items],
        total=total,
        page=page,
        page_size=page_size,
        total_pages=total_pages,
    )


def get_species_by_id(db: Session, species_id: int) -> Species | None:
    return db.query(Species).filter(Species.id == species_id).first()


def search_species(
    db: Session,
    q: str,
    page: int = 1,
    page_size: int = 12,
) -> SpeciesListResponse:
    search_term = f"%{q}%"
    query = db.query(Species).filter(
        (Species.name.ilike(search_term))
        | (Species.scientific_name.ilike(search_term))
        | (Species.habitat.ilike(search_term))
        | (Species.description.ilike(search_term))
    )

    total = query.count()
    total_pages = max(1, math.ceil(total / page_size))
    offset = (page - 1) * page_size

    items = query.order_by(Species.name).offset(offset).limit(page_size).all()

    return SpeciesListResponse(
        items=[SpeciesResponse.model_validate(s) for s in items],
        total=total,
        page=page,
        page_size=page_size,
        total_pages=total_pages,
    )
