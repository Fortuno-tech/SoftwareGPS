from typing import Any


class RuleEngine:
    def evaluate(self, payload: dict[str, Any]) -> dict[str, Any]:
        return {"actions": []}
