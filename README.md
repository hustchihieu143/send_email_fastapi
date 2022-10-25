# FastAPI SendEmail

## Instructions

### Run locally on your machine

1. Copy `.env.example` to `.env` by running `cp .env.example .env`.
2. Change variables in the `.env` file to your requirements.
3. Create your modules in the `src` folder. It typically consists of router (`router.py`), data transfer objects (`dtos.py`), database models (`models.py`), and a service (`<module_name>_service.py`) to handle business logic.
4. Create database migration files by running `poetry run alembic revision -m "create account table"`.
5. Apply the migrations by running `poetry run alembic upgrade head`.
6. Run the app in dev mode: `poetry run task dev`

7. Browse to [http://localhost:8080/docs](http://localhost:8080/docs)

## Packages

- Package mangement: `poetry`
- Task runner (like `npm run ...` in Node.js): `taskipy`
- ORM: `sqlalchemy`
- Database migrations: `alembic`
- Unit testing: `pytest`
- ASGI server: `uvicorn`
- Process manager: `gunicorn`

---

## Built-in scripts

### dev

Running FastAPI app with `uvicorn` and watch for files changes.

```bash
poetry run task dev
```

### start

Running FastAPI app with `gunicorn` in production environment.

```bash
poetry run task start
```

### test

Running tests

```bash
poetry run task test
```

---

## Future features

### Code generator

---

## Links that might be useful
