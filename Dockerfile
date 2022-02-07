FROM python:3.9-buster

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install fastapi
RUN poetry install uvicorn

COPY ./pyproject.toml ./pyproject.toml
COPY ./poetry.lock ./poetry.lock

RUN poetry install --no-dev --no-ansi

COPY . .

EXPOSE 8000

CMD uvicorn main:app --host=0.0.0.0 --port=8000
