FROM telegraf:1.32.1-alpine

USER root

ENV TZ=Europe/Warsaw

RUN apk add --no-cache python3 py3-requests py3-tz tzdata

USER telegraf
