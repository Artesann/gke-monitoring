FROM python:3.11.2

RUN pip3 install flask prometheus-flask-exporter

WORKDIR /app

COPY main.py /app/main.py

CMD ["python3", "main.py"]