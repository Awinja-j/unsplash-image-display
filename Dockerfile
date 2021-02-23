FROM python:3.9.1-alpine3.12

ENV PYTHONUNBUFFERED 1

RUN mkdir /display_website

WORKDIR /display_website

ADD . /display_website

COPY . /app

COPY . /website/display/management/commands/photos.tsv000 /website/display/management/commands/

RUN apk add --no-cache postgresql-dev gcc python3-dev musl-dev linux-headers

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

CMD ["echo", "Hello"]

COPY . .