FROM python:3.11-slim-bullseye

WORKDIR /store_project/

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV CONFIG_PATH='../config/config.yml'

ENV PYTHONPATH="${PYTHONPATH}:/store_project"

COPY ./poetry.lock ./pyproject.toml /store_project/

RUN python -m pip install --upgrade pip
RUN pip install poetry
RUN poetry config virtualenvs.create false

COPY ./src /store_project/src

ARG POETRY_DEP_GROUP=dev
RUN poetry install --with ${POETRY_DEP_GROUP}
