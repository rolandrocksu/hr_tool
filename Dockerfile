# pull the official base image
FROM python:3.11-slim

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# upgrade system, install required packages for pip
# remove unused packages, clean apt cache
#RUN apt update \
# && apt upgrade -y \
# && apt install -y libpq-dev gcc procps \
# && apt autoremove -y \
# && apt clean -y \
# && rm -rf /var/lib/apt/lists/* \

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app
RUN pip install -r requirements.txt

# copy project
COPY . /usr/src/app

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]