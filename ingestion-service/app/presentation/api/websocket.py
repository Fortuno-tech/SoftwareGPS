from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from app.infrastructure.websocket.manager import WebsocketManager

router = APIRouter(prefix="/ws", tags=["websocket"])
manager = WebsocketManager()


@router.websocket("/")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(f"Message received: {data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)
