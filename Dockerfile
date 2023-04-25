FROM python:3.11

ENV PYTHONUNBUFFERED 1

COPY requirements.txt /src/requirements.txt
COPY . /src
WORKDIR /src
EXPOSE 8000
EXPOSE 5434

RUN python -m pip install --upgrade pip setuptools wheel
RUN pip install -r requirements.txt

RUN adduser --disabled-password src-user

USER src-user



