FROM python:3.10-slim

ENV PROJECT_DIR /usr/src/backend_api

WORKDIR ${PROJECT_DIR}

RUN apt-get update
RUN apt-get install libpq-dev python-dev-is-python3 build-essential -y

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# PORT from .env
ARG PORT
EXPOSE $PORT

CMD ["python", "wsgi.py"]
