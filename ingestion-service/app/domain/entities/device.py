from pydantic import BaseModel


class Device(BaseModel):
    id: str
    name: str
    status: str
