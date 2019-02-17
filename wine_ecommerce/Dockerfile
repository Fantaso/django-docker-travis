FROM python:3.6

ENV PYTHONUNBUFFERED = 1
ENV APP_DIR=/wine_ecommerce

WORKDIR $APP_DIR

ADD requirements.txt $APP_DIR/

RUN pip install -r requirements.txt

ADD . $APP_DIR/
