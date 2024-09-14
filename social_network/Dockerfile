FROM python:3.12-slim
ENV PYTHONUNBUFFERED 1
RUN echo "Installing Dependencies"
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev build-essential pkg-config\
    && apt-get clean
RUN echo "*****creating app folder*****"
RUN mkdir /app
RUN echo "*****assigning app folder as root folder*****"
WORKDIR /app
RUN echo "*****copy requirements.txt file*****"
COPY requirements.txt /app
RUN echo "*****upgrading pip*****"
RUN python -m pip install --upgrade pip setuptools
RUN echo "*****instaliing requirements_docker*****"
RUN pip install --no-deps ruamel.yaml -r requirements.txt
RUN echo "*****copy all files to root app folder*****"
COPY . /app