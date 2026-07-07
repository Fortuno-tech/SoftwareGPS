from typing import Callable


class TopicRouter:
    def __init__(self) -> None:
        self.handlers: dict[str, Callable] = {}

    def register(self, topic: str, handler: Callable) -> None:
        self.handlers[topic] = handler

    def route(self, topic: str, message: dict) -> None:
        if handler := self.handlers.get(topic):
            handler(message)
