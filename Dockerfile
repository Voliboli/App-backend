FROM python:3.12-slim

ENV PROJECT_DIR /usr/src/backend_api

WORKDIR ${PROJECT_DIR}

RUN apt-get install libpq-dev python-dev

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

ARG PORT
EXPOSE $PORT

CMD ["python", "wsgi.py"]
