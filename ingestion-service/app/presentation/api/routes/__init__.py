from .alerts import router as alerts_router
from .devices import router as devices_router
from .health import router as health_router
from .measurements import router as measurements_router
from ..websocket import router as websocket_router


routers = [
    health_router,
    devices_router,
    measurements_router,
    alerts_router,
    websocket_router,
]
