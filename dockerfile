from python:3.10-slim-buster

COPY ./requierements.txt /


RUN pip install -r requierements.txt


RUN mkdir /app
WORKDIR /app

COPY Service1_Aizhana.py /app
COPY Service2_Aizhana.py /app
COPY Service3_Aizhana.py /app
COPY Service4_Aizhana.py /app
COPY sqlQueries.py /app
CMD ["python", "app/Service1_Aizhana.py"]
