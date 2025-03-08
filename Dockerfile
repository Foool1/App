FROM python:3.9

LABEL maintainer="foool1"
ENV PYTHONUNBUFFERED 1

# Kopiowanie plików wymagań i aplikacji
COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt
COPY ./app /app
WORKDIR /app
EXPOSE 8000

ARG DEV=false

# Instalacja zależności systemowych, w tym Tesseracta
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        postgresql-client \
        libzbar0 \
        build-essential \
        libpq-dev \
        libzbar-dev \
        tesseract-ocr \
        libtesseract-dev \
        libjpeg-dev \
        zlib1g-dev \
        libpng-dev && \
    # Tworzenie środowiska wirtualnego i instalacja zależności Pythona
    python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    # Warunkowa instalacja dev-zależności
    if [ "$DEV" = "true" ]; then /py/bin/pip install -r /tmp/requirements.dev.txt; fi && \
    # Usuwanie niepotrzebnych pakietów deweloperskich
    apt-get purge -y --auto-remove \
        build-essential \
        libpq-dev \
        libzbar-dev \
        libjpeg-dev \
        zlib1g-dev \
        libpng-dev && \
    # Czyszczenie
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    # Tworzenie użytkownika django-user
    adduser \
        --disabled-password \
        --no-create-home \
        django-user

# Aktualizacja PATH dla środowiska wirtualnego
ENV PATH="/py/bin:$PATH"
USER django-user