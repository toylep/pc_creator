FROM python:3.12-slim-bullseye


RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    ca-certificates \
    git \
    default-libmysqlclient-dev \
    build-essential \
    libpq-dev \
    libldap2-dev \
    libsasl2-dev \
    libzbar-dev \
    ldap-utils \
    curl \
    openssh-server \
    apt-utils \
    && apt-get clean && \
    rm -rf /var/lib/apt/lists/*e~

# configure ssh server
RUN passwd -d root
RUN echo "PermitRootLogin yes" >> /etc/ssh/sshd_config
RUN echo "PermitEmptyPasswords yes" >> /etc/ssh/sshd_config

COPY ./pc_builder2 /srv/app

WORKDIR /srv/app

RUN python -m venv /srv/app/.venv
ENV PATH="/srv/app/.venv/bin:$PATH"
RUN pip install uv

RUN pwd

RUN uv pip install -r /srv/app/requirements.txt
