"""Verified Unsplash image URLs for seed data."""

PHOTOS = {
    "forest_fog": "photo-1470071459604-3b5ec3a7fe05",
    "forest_path": "photo-1500530855697-b586d89ba3ee",
    "mountains_snow": "photo-1464822759023-fed622ff2c3b",
    "mountains": "photo-1506905925346-21bda4d32df4",
    "rainforest": "photo-1518531933037-91b2f5f229cc",
    "grasslands": "photo-1509316785289-025f5b846b35",
    "desert": "photo-1416879595882-3373a0480b5b",
    "ocean": "photo-1559827260-dc66d52bef19",
    "gorilla": "photo-1551969014-7d2c4cddf0b6",
    "panda": "photo-1525382455947-f319bc05fb35",
    "sea_turtle": "photo-1544551763-46a013bb70d5",
    "orangutan": "photo-1597848212624-a19eb35e2651",
    "elephant": "photo-1564760055775-d63b17a55c44",
    "birds": "photo-1444464666168-49d633b86797",
    "leopard": "photo-1511497584788-876760111969",
    "fox": "photo-1469474968028-56623f02e42e",
    "red_panda": "photo-1502082553048-f009c37129b9",
    "bison": "photo-1472214103451-9374bd1c798e",
}


def unsplash(photo_id: str, width: int = 800) -> str:
    return f"https://images.unsplash.com/{photo_id}?auto=format&fit=crop&w={width}&q=80"
