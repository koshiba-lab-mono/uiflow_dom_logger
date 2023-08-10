FROM python:3.9-slim
ARG WKDIR=app

WORKDIR ${WKDIR}
COPY . /app
RUN pip install -r requirements.txt