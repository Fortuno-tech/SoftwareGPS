from typing import Set


class WebsocketManager:
    def __init__(self) -> None:
        self.active_connections: Set = set()

    def connect(self, websocket) -> None:
        self.active_connections.add(websocket)

    def disconnect(self, websocket) -> None:
        self.active_connections.discard(websocket)

    async def broadcast(self, message: str) -> None:
        for connection in self.active_connections:
            await connection.send_text(message)
