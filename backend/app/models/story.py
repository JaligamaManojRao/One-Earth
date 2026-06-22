"""SQLAlchemy model for conservation success stories."""

from sqlalchemy import Column, Integer, String, Text

from app.database.database import Base


class Story(Base):
    __tablename__ = "stories"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    summary = Column(Text, nullable=False)
    image_url = Column(String(500), nullable=False)
    achievements = Column(Text, nullable=False)  # JSON array stored as string
    timeline = Column(Text, nullable=False)  # JSON array stored as string
