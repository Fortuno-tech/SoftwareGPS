from pydantic import BaseModel


class Command(BaseModel):
    device_id: str
    action: str
    payload: dict[str, str]
