from python:3.10-slim-buster

COPY requirements.txt /

RUN pip install -r requirements.txt

RUN mkdir /app
WORKDIR /app

COPY Service1_Aizhana.py /app

CMD ["python", "app/Service1_Aizhana.py"]
