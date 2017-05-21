# Introduction to Machine Learning
IFP School - 30 Juin 2017


Louis GUITTON, 
Data Scientist, Dojo Madness

Slides: http://bit.ly/log-ifpschool 

Twitter: [@laguittemh](https://twitter.com/LaGuitteMH) 

## Initial Setup

1. Docker build (recommended)
```bash
docker pull louisguitton/log-ifpschool
```

1bis. Manual Build (if no other solution)
```bash
git clone git@github.com:louisguitton/log-ifpschool.git
docker build . -t louisguitton/log-ifpschool:latest
```

2. Start the notebook server
```bash
docker run -it --rm -p 8888:8888 louisguitton/log-ifpschooldd
```

## Demo 1 : Flower Classification

## Demo 2 : Simplest Neural Network

## Demo 3 : 