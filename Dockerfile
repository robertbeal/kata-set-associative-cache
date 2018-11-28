FROM alpine:3.7

WORKDIR /tmp
COPY requirements.txt .

RUN apk add --no-cache \
    python3 \
  && python3 -m pip install -r requirements.txt \
  && rm -rf /tmp/*

WORKDIR /data
COPY . .
