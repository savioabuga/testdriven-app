FROM docker:dind
RUN apk add -U --no-cache \
    git \
    py3-pip \
    musl-dev \
    openssl-dev \
    gcc \
    python3-dev

RUN pip3 install awscli docker-compose
