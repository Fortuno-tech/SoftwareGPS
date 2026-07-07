from typing import Protocol


class MeasurementRepository(Protocol):
    def save(self, measurement: dict) -> None:
        ...

    def latest(self, device_id: str) -> list[dict]:
        ...
