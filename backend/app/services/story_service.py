"""Business logic for conservation story queries."""

from sqlalchemy.orm import Session

from app.models.story import Story
from app.schemas.story import StoryListResponse, StoryResponse


def get_stories(db: Session) -> StoryListResponse:
    items = db.query(Story).order_by(Story.id).all()
    return StoryListResponse(
        items=[StoryResponse.model_validate(s) for s in items],
        total=len(items),
    )


def get_story_by_id(db: Session, story_id: int) -> Story | None:
    return db.query(Story).filter(Story.id == story_id).first()
