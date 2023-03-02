FROM python:3.10-slim-buster

RUN pip install pipenv

ENV PROJECT_DIR /usr/src/backend_api

WORKDIR ${PROJECT_DIR}

COPY Pipfile .
COPY Pipfile.lock .
RUN pipenv install --deploy --ignore-pipfile

COPY . .

ARG PORT
EXPOSE $PORT

CMD ["pipenv", "run", "python", "wsgi.py"]
