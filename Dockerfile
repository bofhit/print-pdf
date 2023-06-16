FROM ubuntu:22.04

RUN apt update \
    && apt install -yq cups \
        pip

COPY cupsd.conf /etc/cups/cupsd.conf
COPY . /app

WORKDIR /app

RUN     pip install -r requirements.txt

ENTRYPOINT ["./startup.sh"]