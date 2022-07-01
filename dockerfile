FROM python:3

EXPOSE 12345

ADD server.py /

CMD [ "python", "./server.py" ]