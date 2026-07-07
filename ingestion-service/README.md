# Ingestion Service

Microservice FastAPI pour l'ingestion de données capteurs, l'alerte et la publication de commandes.

## Structure

- `app/` : code métier, présentation, infrastructure
- `tests/` : tests unitaires, d'intégration et MQTT
- `docker/` : Dockerfile et script d'entrypoint

## Démarrage

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```
