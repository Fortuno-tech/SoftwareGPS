from fastapi import APIRouter

router = APIRouter(prefix="/devices", tags=["devices"])


@router.get("/")
def list_devices() -> dict[str, str]:
    return {"message": "Liste des devices disponible"}
