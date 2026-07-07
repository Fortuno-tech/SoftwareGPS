from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "ingestion-service"
    mqtt_broker_url: str = "mqtt://localhost"
    mqtt_broker_port: int = 1883
    database_url: str = "sqlite:///./test.db"
    redis_url: str = "redis://localhost:6379/0"

    class Config:
        env_file = ".env"


settings = Settings()
