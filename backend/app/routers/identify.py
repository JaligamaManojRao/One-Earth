"""AI wildlife identifier API routes."""

from fastapi import APIRouter, File, HTTPException, UploadFile

from app.schemas.identify import IdentifyResponse
from app.services.identify_service import identify_wildlife

router = APIRouter(prefix="/identify", tags=["AI Identifier"])

ALLOWED_TYPES = {"image/jpeg", "image/png", "image/webp", "image/gif"}
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10 MB


@router.post("", response_model=IdentifyResponse)
async def identify_species(file: UploadFile = File(...)):
    if file.content_type not in ALLOWED_TYPES:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid file type. Allowed: {', '.join(ALLOWED_TYPES)}",
        )

    contents = await file.read()

    if len(contents) == 0:
        raise HTTPException(status_code=400, detail="Empty file uploaded")

    if len(contents) > MAX_FILE_SIZE:
        raise HTTPException(status_code=400, detail="File too large. Maximum size is 10 MB")

    return identify_wildlife(contents)
