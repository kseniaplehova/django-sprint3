# Blogicum — Sprint 3: models, admin and ORM

A Django blog whose posts, categories and locations are stored in a database and managed through a customised admin site.

Educational project — Yandex Practicum, Python Developer course. This is **stage 2 of 3** of the Blogicum project (stage 1: `django-sprint1`, stage 3: `django-sprint4`).

## Features

- Models `Post`, `Category` and `Location`, built on abstract base models (`PublishedModel` with `is_published`, `TimeStampedModel` with `created_at`).
- Delayed publishing: a post is shown only if it and its category are published and `pub_date` is not in the future.
- Custom `QuerySet` / `Manager` for posts (`published()`, `with_related()`, `ordered()`) using `select_related` to avoid extra queries.
- Function-based views: home page (latest 5 posts), post detail and category page, with `get_object_or_404`.
- Customised admin for all three models: list display, filters, search, `date_hierarchy`, fieldsets, slug prepopulation, editable publish flag.
- Russian locale, static pages "About" and "Rules", two migrations, demo data in `db.json`.

## Tech stack

Python, Django 5.1.1, SQLite, pytest, pytest-django, mixer, flake8 (see `requirements.txt`).

## Getting started

```bash
git clone https://github.com/kseniaplehova/django-sprint3.git
cd django-sprint3
python -m venv venv
source venv/Scripts/activate   # Windows (Git Bash); on Linux/macOS: source venv/bin/activate
pip install -r requirements.txt
cd blogicum
python manage.py migrate
python manage.py loaddata ../db.json   # optional demo data
python manage.py createsuperuser       # optional, for /admin/
python manage.py runserver
```

## Tests

From the repository root:

```bash
pytest
```

Tests in `tests/` cover the models, admin, URLs, views of posts, categories and static pages, and localization.

## Author

Ksenia Plehova — [GitHub](https://github.com/kseniaplehova)
