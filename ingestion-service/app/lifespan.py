from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.config.logging import logger


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting ingestion service")
    yield
    logger.info("Stopping ingestion service")
