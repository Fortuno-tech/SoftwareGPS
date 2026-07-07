from typing import Any


def create_alert(sensor_data: dict[str, Any]) -> dict[str, Any]:
    return {"alert": "created", "source": sensor_data}
