"""Pydantic schemas for conservation story endpoints."""

import json

from pydantic import BaseModel, ConfigDict, field_validator


class TimelineEvent(BaseModel):
    year: str
    event: str


class StoryBase(BaseModel):
    title: str
    summary: str
    image_url: str
    achievements: list[str]
    timeline: list[TimelineEvent]


class StoryResponse(StoryBase):
    id: int

    model_config = ConfigDict(from_attributes=True)

    @field_validator("achievements", "timeline", mode="before")
    @classmethod
    def parse_json_fields(cls, value):
        if isinstance(value, str):
            return json.loads(value)
        return value


class StoryListResponse(BaseModel):
    items: list[StoryResponse]
    total: int
