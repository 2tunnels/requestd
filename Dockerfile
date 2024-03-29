FROM python:3.8

ENV PYTHONUNBUFFERED 1

RUN pip install -U pip setuptools poetry --no-cache-dir
RUN poetry config settings.virtualenvs.create false

WORKDIR /usr/src/app

COPY pyproject.toml .
COPY poetry.lock .
RUN poetry install --no-dev

COPY . .

EXPOSE 8080

CMD ["./run.py"]
