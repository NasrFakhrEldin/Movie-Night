FROM python:3.10-alpine

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_CONFIGURATION Dev
ENV DJANGO_OMDB_KEY '3430a519'
ENV DJANGO_SECRET_KEY 'django-insecure-32je!ye&zl5p-gr^bi$r+_np^b$ntc%66sr#b6@g&3(tgwd^0('
ENV DJANGO_EMAIL_HOST_USER 'movienight.team.ad@gmail.com'
ENV DJANGO_EMAIL_HOST_PASSWORD 'nrmferwzjxujzaul'

RUN apk add -u zlib-dev jpeg-dev gcc musl-dev

RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt