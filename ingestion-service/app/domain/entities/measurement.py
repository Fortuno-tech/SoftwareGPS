from datetime import datetime
from pydantic import BaseModel


class Measurement(BaseModel):
    device_id: str
    timestamp: datetime
    type: str
    value: float
