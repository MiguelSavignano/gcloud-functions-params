FROM python:3.6.3-alpine
LABEL Name=gcloud-functions-params Version=0.0.1
RUN python3 -m pip install --upgrade twine
WORKDIR /app
ADD . /app

# docker build -t gcloud-functions-params .
# docker run -it gcloud-functions-params sh
# ./deploy.sh
