# Use an official Python runtime as a parent image
FROM python:slim-buster

WORKDIR /app

ADD . /app

RUN pip install --trusted-host pypi.python.org Flask

#the port number that our container should expose
EXPOSE 4000

CMD ["python", "app.py"]