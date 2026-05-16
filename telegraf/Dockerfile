FROM telegraf:1.38.4-alpine

USER root

ENV TZ=Europe/Warsaw

RUN apk add --no-cache bash python3 py3-uv

COPY telegraf/pyproject.toml .

ENV VIRTUAL_ENV=/opt/venv
ENV PATH="/opt/venv/bin:$PATH"
ENV UV_PROJECT_ENVIRONMENT=/opt/venv
RUN uv venv && uv sync

USER telegraf
