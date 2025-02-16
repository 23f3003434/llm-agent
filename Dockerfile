FROM ubuntu:latest

WORKDIR /app

COPY . ./

RUN pip install requirements.txt


CMD ["python3", "app.py"]