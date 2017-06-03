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

3. Open the notebook in a browser

**If you're on Mac or Linux**: follow the link in hte console that starts with http://localhost:8888 + token

example: http://localhost:8888/?token=30491c22aab05ff61757c9d59d911fd2150247e520ff9283

 
**If you're on Windows**, first run 
```bash
docker-machine ip
```
This will give you the IP address of the notebook. Combine this to the adress given by the console

example: http://178.5.158.196:8888/?token=30491c22aab05ff61757c9d59d911fd2150247e520ff9283

## Demo 1 : Flower Classification

## Demo 2 : Simplest Neural Network

## Demo 3 : Cats vs Dogs