"""Mock AI wildlife identification service.

This module provides a placeholder implementation that simulates
species identification from uploaded images. Replace with a real
ML model (e.g. TensorFlow, PyTorch) in production.
"""

import hashlib
import random

from app.schemas.identify import IdentifyResponse

# Mock species database for identification results
MOCK_SPECIES = [
    {
        "species_name": "Bengal Tiger",
        "habitat": "Rainforests",
        "conservation_status": "Endangered",
        "interesting_fact": "Each tiger's stripe pattern is unique, like a human fingerprint.",
    },
    {
        "species_name": "African Elephant",
        "habitat": "Grasslands",
        "conservation_status": "Endangered",
        "interesting_fact": "Elephants can communicate using infrasound over distances of up to 10 kilometers.",
    },
    {
        "species_name": "Blue Whale",
        "habitat": "Oceans",
        "conservation_status": "Endangered",
        "interesting_fact": "A blue whale's heart is roughly the size of a small car.",
    },
    {
        "species_name": "Giant Panda",
        "habitat": "Mountains",
        "conservation_status": "Vulnerable",
        "interesting_fact": "Pandas spend up to 14 hours a day eating bamboo.",
    },
    {
        "species_name": "Snow Leopard",
        "habitat": "Mountains",
        "conservation_status": "Vulnerable",
        "interesting_fact": "Snow leopards can leap up to 15 meters in a single bound.",
    },
    {
        "species_name": "Green Sea Turtle",
        "habitat": "Oceans",
        "conservation_status": "Endangered",
        "interesting_fact": "Green turtles can navigate thousands of miles to return to their birthplace.",
    },
    {
        "species_name": "Red Panda",
        "habitat": "Mountains",
        "conservation_status": "Endangered",
        "interesting_fact": "Red pandas use their bushy tails as blankets during cold mountain nights.",
    },
    {
        "species_name": "Humpback Whale",
        "habitat": "Oceans",
        "conservation_status": "Least Concern",
        "interesting_fact": "Humpback whale songs can last up to 20 minutes and evolve each season.",
    },
]


def identify_wildlife(image_bytes: bytes) -> IdentifyResponse:
    """Simulate AI identification based on image content hash.

    Uses a deterministic hash of the image bytes to consistently
    return the same prediction for the same image, while varying
    results across different uploads.
    """
    image_hash = hashlib.md5(image_bytes).hexdigest()
    seed = int(image_hash[:8], 16)
    rng = random.Random(seed)

    species = rng.choice(MOCK_SPECIES)
    confidence = round(rng.uniform(0.72, 0.98), 2)

    return IdentifyResponse(
        species_name=species["species_name"],
        confidence_score=confidence,
        habitat=species["habitat"],
        conservation_status=species["conservation_status"],
        interesting_fact=species["interesting_fact"],
    )
