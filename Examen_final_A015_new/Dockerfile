FROM python:3.11
LABEL maintainer="Genia<eugenie_montreal@hotmail.com>"
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
COPY . /app
CMD ["python","./service.py"]