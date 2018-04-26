FROM alpine

COPY requirements.txt /tmp/requirements.txt

RUN apk update && \
	apk add --no-cache \
    python3 \
    bash \
    nginx \
    uwsgi \
    python3-dev \
    musl-dev \
    uwsgi-python3 \
    chromium \
    udev \
    xvfb \
    chromium-chromedriver \
    supervisor && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    pip3 install -r /tmp/requirements.txt && \
    rm /etc/nginx/conf.d/default.conf && \
    rm -r /root/.cache && \ 
    chmod -R 777 /usr/lib/python3.6/site-packages/selenium/
    
COPY nginx.conf /etc/nginx/
COPY flask-site-nginx.conf /etc/nginx/conf.d/
# Copy the base uWSGI ini file to enable default dynamic uwsgi process number
COPY uwsgi.ini /etc/uwsgi/
# Custom Supervisord config
COPY supervisord.conf /etc/supervisord.conf

COPY ./app /app
WORKDIR /app

CMD ["/usr/bin/supervisord"]