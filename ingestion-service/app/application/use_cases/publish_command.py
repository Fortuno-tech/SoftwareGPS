from typing import Any


def publish_command(command: dict[str, Any]) -> dict[str, Any]:
    return {"command": "published", "payload": command}
