FROM alpine:latest

ENV DB_HOST=192.168.100.118
ENV DB_PORT=9200
ENV SLEEP=60
ENV TRIES=5

RUN apk update && apk --no-cache add \
    python3 &&\
    pip3 install -U pip && pip3 install requests

WORKDIR /home/docker-class/

COPY sample.py .
RUN chmod +x sample.py

CMD ["./sample.py"]
