"""Conservation stories API routes."""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.story import StoryListResponse, StoryResponse
from app.services import story_service

router = APIRouter(prefix="/stories", tags=["Stories"])


@router.get("", response_model=StoryListResponse)
def list_stories(db: Session = Depends(get_db)):
    return story_service.get_stories(db)


@router.get("/{story_id}", response_model=StoryResponse)
def get_story(story_id: int, db: Session = Depends(get_db)):
    story = story_service.get_story_by_id(db, story_id)
    if not story:
        raise HTTPException(status_code=404, detail="Story not found")
    return StoryResponse.model_validate(story)
