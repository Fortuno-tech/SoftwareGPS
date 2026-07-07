from fastapi import FastAPI

from app.config.logging import configure_logging
from app.lifespan import lifespan
from app.presentation.api.routes import routers

configure_logging()

app = FastAPI(lifespan=lifespan)

for router in routers:
    app.include_router(router)
