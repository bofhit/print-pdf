FROM ubuntu:22.04

RUN apt update \
    && apt install -yq cups \
        pip

COPY cupsd.conf /etc/cups/cupsd.conf
COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

# CUPS user.
RUN adduser admcups && \
    echo "admcups:bacon-88" | chpasswd && \
    usermod -aG lpadmin admcups

# Resolve permissions error when running on Linux.
RUN chmod +x ./startup.sh

ENTRYPOINT ["./startup.sh"]
