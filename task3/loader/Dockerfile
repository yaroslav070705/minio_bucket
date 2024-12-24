FROM python:3.9-slim

WORKDIR ./minio_py_test

COPY data_sender.py .
COPY requirements.txt . 

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3", "data_sender.py"]

