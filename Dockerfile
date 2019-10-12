FROM python:3.6.3-alpine
LABEL Name=gcloud-functions-params Version=0.0.1

WORKDIR /app

COPY requirements.txt /app/
RUN pip install -r requirements.txt
RUN python3 -m pip install --upgrade twine

ADD . /app
