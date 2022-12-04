# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /job-analyzer

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "flask","--app=src.app", "run", "--host=0.0.0.0"]

#docker run -d -p 5000:5000 job-analyzer