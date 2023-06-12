FROM telegraf:1.26-alpine

USER root

ENV TZ=Europe/Warsaw

RUN apk add --no-cache python3 py3-pip tzdata

COPY telegraf/requirements.txt /var/tmp
RUN pip3 install -r /var/tmp/requirements.txt

USER telegraf
