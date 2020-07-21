FROM python:3.7

# set work directory
WORKDIR /usr/src/app/

# set environment variables
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .

# Django service
EXPOSE 8000