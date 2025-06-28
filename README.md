# Kunuz Clone Backend

A minimal Django backend for a news portal, featuring CRUD APIs, JWT authentication, email verification, admin customization, translation, and scheduled publishing.

## Features
- **CRUD APIs** for News, Category, Tag, Comment, and MediaFile (Django REST Framework)
- **JWT Authentication** (login, registration, email confirmation)
- **Email Verification** (console backend for dev)
- **Admin Panel** customized with Jazzmin
- **Static & Media Files** support
- **Translations**: Admin and error messages via Rosetta, .po files for Uzbek and Russian
- **Celery & Redis**: For async tasks and scheduled news publishing
- **Logging**: Console and file logging for debugging and task tracking
- **Scheduled News**: News can be published at a future time via Celery periodic task

## API Overview
- All main models have CRUD endpoints (see Swagger UI)
- JWT endpoints: `/api/token/`, `/api/token/refresh/`, `/api/register/`, `/api/confirm/`
- News endpoints support scheduling via `publish_at` field

## Admin Panel
- Jazzmin theme, improved usability for all main models
- Fieldsets, filters, and read-only fields for clarity
- Manage scheduled news, users, categories, tags, comments, and media

## Translations
- Rosetta UI at `/rosetta/` for managing translations
- Uzbek and Russian .po files generated

## Celery & Redis
- Celery worker and beat required for scheduled tasks:
  ```sh
  celery -A core worker --beat --loglevel=info
  ```
- Redis must be running on `localhost:6379`

## Logging
- Logs to both console and `logs/debug.log`
- Celery tasks log their execution

## Setup
1. Install dependencies:
   ```sh
   uv pip install -r requirements.txt
   ```
2. Run migrations:
   ```sh
   python manage.py migrate
   ```
3. Create superuser:
   ```sh
   python manage.py createsuperuser
   ```
4. Run development server:
   ```sh
   python manage.py runserver
   ```
5. Start Redis and Celery as above

## API Docs
- Swagger UI: `/swagger/`
- ReDoc: `/redoc/`

---

**Note:**
- News modeltranslation is not available due to Django 5.x incompatibility.
- For production, configure proper email backend and secure settings.