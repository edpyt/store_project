FROM python:3.11-slim-bullseye

WORKDIR /app/

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV CONFIG_PATH='../config/'

ENV PYTHONPATH='${PYTHONPATH}:/app/src'

COPY ./poetry.lock ./pyproject.toml /app/

RUN python -m pip install --upgrade pip
RUN pip install poetry
RUN poetry config virtualenvs.create false

COPY ./src /app/src

ARG POETRY_DEP_GROUP=dev
RUN poetry install --with ${POETRY_DEP_GROUP}
