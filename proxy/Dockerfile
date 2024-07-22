FROM fsouza/docker-ssl-proxy:latest

USER root

ENV TZ=Europe/Warsaw

RUN apk add --no-cache tzdata

ADD proxy/nginx.conf.template /
ADD proxy/configure_and_start.sh /

ADD proxy/cert/* /etc/nginx/certs/
