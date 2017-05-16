FROM continuumio/miniconda3

MAINTAINER ops@dojomadness.com

# RUN wget "https://repo.continuum.io/archive/Anaconda3-4.3.1-Linux-x86_64.sh"
# RUN bash Anaconda3-4.3.1-Linux-x86_64.sh
RUN conda install numpy pandas scikit-learn matplotlib seaborn

EXPOSE 80
