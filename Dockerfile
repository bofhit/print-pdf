FROM ubuntu:22.04

RUN apt update \
    && apt install -yq cups

COPY cupsd.conf /etc/cups/cupsd.conf

ENTRYPOINT exec bash   