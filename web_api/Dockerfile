# Dockerfile, Image, Contianer
From alpine:latest 

RUN apk add --no-cache python3 py3-pip curl 

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY ./* /usr/src/app/

RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE 3001

CMD ["python3", "/usr/src/app/tor_connection.py"]