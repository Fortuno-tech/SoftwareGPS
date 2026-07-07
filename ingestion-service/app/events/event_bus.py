from typing import Callable


class EventBus:
    def __init__(self) -> None:
        self.subscribers: dict[str, list[Callable]] = {}

    def subscribe(self, event_type: str, handler: Callable) -> None:
        self.subscribers.setdefault(event_type, []).append(handler)

    def publish(self, event_type: str, payload: dict) -> None:
        for handler in self.subscribers.get(event_type, []):
            handler(payload)
