FROM python:3.10.4

WORKDIR /app

LABEL org.opencontainers.image.source="https://github.com/apinanyogaratnam/flask-proxy-server"

COPY requirements.txt .
COPY proxy.py .

RUN pip3 install -r requirements.txt

CMD ["python3", "proxy.py"]
