from typing import Protocol


class DeviceRepository(Protocol):
    def list(self) -> list[dict[str, str]]:
        ...

    def get(self, device_id: str) -> dict[str, str] | None:
        ...
