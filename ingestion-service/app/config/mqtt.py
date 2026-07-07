from .settings import settings


def get_mqtt_settings() -> dict[str, str | int]:
    return {
        "broker_url": settings.mqtt_broker_url,
        "broker_port": settings.mqtt_broker_port,
    }
