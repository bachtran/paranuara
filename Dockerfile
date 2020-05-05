FROM python:3

ENV APP /paranuara
RUN mkdir $APP
WORKDIR $APP

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ENV FLASK_APP=paranuara.py
ENV FLASK_CONFIG=development

CMD flask run --host="0.0.0.0"
