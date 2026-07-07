from typing import Protocol


class AlertRepository(Protocol):
    def save(self, alert: dict) -> None:
        ...

    def list(self) -> list[dict]:
        ...
