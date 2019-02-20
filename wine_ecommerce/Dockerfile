FROM python:3.7

ENV PYTHONUNBUFFERED = 1
ENV APP_DIR=/django-app

WORKDIR $APP_DIR

ADD requirements.txt $APP_DIR/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000

ADD . $APP_DIR/

# RUN ["python", "manage.py", "runserver", "0.0.0.0:8000"]
# RUN ["python", "manage.py", "makemigrations"]
# RUN ["python", "manage.py", "migrate"]

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
