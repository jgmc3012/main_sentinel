FROM python:3.7-buster

# Python
ENV PYTHONUNBUFFERED 1

# Poetry
# https://python-poetry.org/docs/configuration/#using-environment-variables
ENV POETRY_VERSION=1.0.10 \
    # do not ask any interactive question
    POETRY_NO_INTERACTION=1

RUN apt-get update -y
# psycopg2 dependencies
RUN apt-get install -y python3-dev libpq-dev postgresql-contrib

# Install poetry - respects $POETRY_VERSION & $POETRY_HOME
RUN pip install "poetry==$POETRY_VERSION"

# Copy project requirement files here to ensure they will be cached.
WORKDIR /app
COPY poetry.lock pyproject.toml ./

# Project initialization:
RUN poetry install --no-interaction --no-ansi

COPY ./compose/production/telegram/entrypoint /entrypoint
RUN sed -i 's/\r//' /entrypoint
RUN chmod +x /entrypoint

COPY ./compose/local/telegram/start /start
RUN sed -i 's/\r//' /start
RUN chmod +x /start

ENTRYPOINT ["/entrypoint"]
