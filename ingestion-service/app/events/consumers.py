from typing import Callable


def create_consumer(handler: Callable):
    def consumer(payload: dict) -> None:
        handler(payload)
    return consumer
