FROM python:last

COPY ./ /catchiorrineo

WORKDIR /catchiorrineo

RUN pip install -r requirements.txt

CMD [ "python", "api/main.py" ]

