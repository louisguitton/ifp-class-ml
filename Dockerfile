FROM jupyter/datascience-notebook

MAINTAINER louisguitton93@gmail.com

RUN pip install --upgrade pip
RUN pip install tensorflow keras

COPY . code/
WORKDIR code/

EXPOSE 80
