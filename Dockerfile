FROM python:3.10.5-slim
RUN apt-get update && apt-get -y install git libmagic-dev

ENV POETRY_VIRTUALENVS_CREATE false
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH .
ENV SECRET_KEY 123456
ENV DJANGO_SETTINGS_MODULE "tempracatao.settings.base"

# Get pip extra-index-url from pipeline to install private dependencies
ARG INDEX_URL
ENV PIP_EXTRA_INDEX_URL $INDEX_URL

COPY poetry.lock pyproject.toml ./

RUN pip install --no-cache-dir -U pip poetry
RUN poetry export -f requirements.txt > requirements.txt
RUN pip install -r requirements.txt

# Unset pip extra-index-url
ENV PIP_EXTRA_INDEX_URL ""

COPY src/ .

EXPOSE 8000

RUN ["./manage.py", "collectstatic", "--no-input"]

CMD $DOCKER_CMD
