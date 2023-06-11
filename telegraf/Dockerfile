FROM telegraf:1.25-alpine

USER root

RUN apk add --no-cache python3 py3-pip
COPY telegraf/requirements.txt /var/tmp
RUN pip3 install -r /var/tmp/requirements.txt

USER telegraf
