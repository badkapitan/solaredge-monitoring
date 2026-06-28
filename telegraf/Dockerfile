FROM telegraf:1.39.0-alpine

USER root

ENV TZ=Europe/Warsaw

RUN apk add --no-cache bash python3 py3-uv curl

COPY telegraf/pyproject.toml .

ENV VIRTUAL_ENV=/opt/venv
ENV PATH="/opt/venv/bin:$PATH"
ENV UV_PROJECT_ENVIRONMENT=/opt/venv
RUN uv venv --clear && uv sync

USER telegraf
