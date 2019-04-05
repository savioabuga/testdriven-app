FROM docker:dind
RUN apk add -U --no-cache \
    curl \
    git \
    py3-pip \
    musl-dev \
    openssl-dev \
    gcc \
    python3-dev \
    libffi-dev \
    py3-pynacl \
    neovim \
    openssh-client \
    mdocml-apropos


RUN pip3 install awscli docker-compose

