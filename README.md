# NutriScan â€” AI Calorie Tracker

A **Django** backend that recognises food from a photo and logs its estimated nutrition.
Image classification runs on a **TensorFlow/Keras** model; heavy work is offloaded to
**Celery** workers, and data is served through both a REST API and a **GraphQL** endpoint.

## Stack

| Layer | Tech |
|-------|------|
| API | Django 5.2, Django REST Framework, `graphene-django` |
| Auth | DRF SimpleJWT |
| Async | Celery + Redis (broker/result) |
| ML | TensorFlow 2.19 / Keras 3 (food image classification) |
| DB | SQLite (dev) |
| Deploy | Dockerfile + docker-compose |

## App layout

```
ai/            model loading + Celery task that classifies an uploaded image
food/          FoodItem model, serializers, REST endpoints
meal/          MealLog model â€” a food item logged by a user at a time
users/         registration / auth
graphql_api/   Graphene schema: allFoodItems, allMealLogs (scoped to request.user)
nutriscan/     project settings, Celery app
```

## Run with Docker

```bash
docker compose up --build
```

## Run locally

```bash
python -m venv .venv && .venv\Scripts\activate      # macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate

# terminal 1
python manage.py runserver
# terminal 2 (needs Redis running)
celery -A nutriscan worker -l info
```

## API surface

- REST: `food/` endpoints for food items, `meal/` endpoints for meal logs, JWT auth on `users/`
- GraphQL: `POST /graphql/` â€” `allFoodItems`, `allMealLogs` (returns only the authenticated user's data)

## Status

Prototype. Model weights/inference wiring and dataset are not included; `.gitignore` present but
`db.sqlite3` is committed and should be removed.
