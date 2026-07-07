from fastapi import APIRouter

router = APIRouter(prefix="/measurements", tags=["measurements"])


@router.get("/")
def list_measurements() -> dict[str, str]:
    return {"message": "Liste des mesures disponible"}
