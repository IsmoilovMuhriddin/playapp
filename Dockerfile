FROM python:3.7-alpine

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN pip install pipenv

 
#RUN pip install -r /requirements.txt

# Set work directory.
RUN mkdir /code
WORKDIR /code
COPY ./Pipfile /code/Pipfile
COPY . /code/
RUN pipenv install --system --skip-lock
