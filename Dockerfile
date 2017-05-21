FROM jupyter/datascience-notebook

MAINTAINER louisguitton93@gmail.com

COPY . code/
WORKDIR code/

EXPOSE 80
