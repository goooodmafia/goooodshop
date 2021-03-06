FROM python:3.9-alpine

ENV APP_ROOT /app

WORKDIR ${APP_ROOT}
ADD ./app/ ${APP_ROOT}

RUN apk add --no-cache --virtual .build-deps \
    build-base \
    linux-headers \
    ca-certificates \
    git \
    gcc \
    musl-dev \
    python3-dev \
    libffi-dev \
    openssl-dev \
    cargo \
    jpeg-dev \
    zlib-dev \
#    gcc postgresql-dev linux-headers musl-dev \
#    libffi-dev jpeg-dev zlib-dev \
    && pip install -r requirements.txt \
    && find /usr/local \
        \( -type d -a -name test -o -name tests \) \
        -o \( -type f -a -name '*.pyc' -o -name '*.pyo' \) \
        -exec rm -rf '{}' + \
    && runDeps="$( \
        scanelf --needed --nobanner --recursive /usr/local \
                | awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \
                | sort -u \
                | xargs -r apk info --installed \
                | sort -u \
    )" \
    && apk add --virtual .rundeps $runDeps \
    && apk del .build-deps

CMD sh -c "./manage.py collectstatic --no-input && gunicorn --config ${APP_ROOT}/gunicorn.conf.py app.wsgi"