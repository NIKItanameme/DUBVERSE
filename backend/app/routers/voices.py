from fastapi import APIRouter
from typing import List, Dict, Any

router = APIRouter(prefix="/api/voices", tags=["Voices"])

SUPPORTED_LANGUAGES = [
    {"code": "hi", "name": "Hindi", "native": "हिन्दी", "flag": "🇮🇳"},
    {"code": "en", "name": "English", "native": "English", "flag": "🇺🇸"},
    {"code": "es", "name": "Spanish", "native": "Español", "flag": "🇪🇸"},
    {"code": "fr", "name": "French", "native": "Français", "flag": "🇫🇷"},
    {"code": "de", "name": "German", "native": "Deutsch", "flag": "🇩🇪"},
    {"code": "ja", "name": "Japanese", "native": "日本語", "flag": "🇯🇵"},
    {"code": "zh", "name": "Mandarin", "native": "中文", "flag": "🇨🇳"},
    {"code": "ar", "name": "Arabic", "native": "العربية", "flag": "🇸🇦"}
]

VOICE_CLONES = [
    {
        "id": "wise-cherry-3051__nishanth_anna",
        "name": "Nishanth Anna",
        "gender": "Male",
        "language": "Hindi",
        "accent": "Indian Hindi",
        "description": "Deep, clear conversational Hindi voice with natural cadence.",
        "sample_url": "/samples/nishanth.mp3",
        "is_cloned": True
    },
    {
        "id": "priya-hindi-female-01",
        "name": "Priya Sharma",
        "gender": "Female",
        "language": "Hindi",
        "accent": "Standard Hindi",
        "description": "Warm, articulate female voice ideal for tutorials & presentations.",
        "sample_url": "/samples/priya.mp3",
        "is_cloned": True
    },
    {
        "id": "marcus-vance-en-02",
        "name": "Marcus Vance",
        "gender": "Male",
        "language": "English",
        "accent": "American",
        "description": "Authoritative documentary & narrator tone.",
        "sample_url": "/samples/marcus.mp3",
        "is_cloned": True
    },
    {
        "id": "sarah-connor-en-03",
        "name": "Sarah Connor",
        "gender": "Female",
        "language": "English",
        "accent": "British Accent",
        "description": "Crisp, professional corporate voice clone.",
        "sample_url": "/samples/sarah.mp3",
        "is_cloned": True
    },
    {
        "id": "elena-es-04",
        "name": "Elena Rostova",
        "gender": "Female",
        "language": "Spanish",
        "accent": "Latin American",
        "description": "Expressive spanish speaker with high emotion fidelity.",
        "sample_url": "/samples/elena.mp3",
        "is_cloned": False
    },
    {
        "id": "kenji-ja-05",
        "name": "Kenji Takahashi",
        "gender": "Male",
        "language": "Japanese",
        "accent": "Tokyo Standard",
        "description": "Smooth tech & anime style vocal tone.",
        "sample_url": "/samples/kenji.mp3",
        "is_cloned": False
    }
]

@router.get("/languages")
def get_languages() -> List[Dict[str, Any]]:
    return SUPPORTED_LANGUAGES

@router.get("/profiles")
def get_voices() -> List[Dict[str, Any]]:
    return VOICE_CLONES
