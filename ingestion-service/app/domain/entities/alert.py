from datetime import datetime
from pydantic import BaseModel


class Alert(BaseModel):
    id: str
    device_id: str
    level: str
    message: str
    created_at: datetime
