FROM ubuntu:22.04

RUN apt-get update && apt-get install -y \
    openvpn \
    python3 \
    python3-pip \
    curl \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

COPY app.py .
COPY vpn_service/ ./vpn_service/
COPY entrypoint.sh .
RUN chmod +x entrypoint.sh

VOLUME /app/configs

EXPOSE 5000

CMD ["/app/entrypoint.sh"]