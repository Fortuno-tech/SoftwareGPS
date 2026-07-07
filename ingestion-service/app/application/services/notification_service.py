from typing import Any


class NotificationService:
    def send_email(self, payload: dict[str, Any]) -> None:
        pass

    def send_sms(self, payload: dict[str, Any]) -> None:
        pass

    def send_push(self, payload: dict[str, Any]) -> None:
        pass
