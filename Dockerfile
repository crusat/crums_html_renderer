FROM python:3.6-alpine

RUN mkdir -p /code

WORKDIR /code

COPY main.py /code/
COPY requirements.txt /code/

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["gunicorn", "main:app", "-b", "0.0.0.0:5000"]
