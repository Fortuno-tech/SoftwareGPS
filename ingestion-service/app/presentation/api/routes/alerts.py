from fastapi import APIRouter

router = APIRouter(prefix="/alerts", tags=["alerts"])


@router.get("/")
def list_alerts() -> dict[str, str]:
    return {"message": "Liste des alertes disponible"}
