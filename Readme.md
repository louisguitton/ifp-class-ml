# Introduction to Machine Learning
IFP School - 30 Juin 2017


Louis GUITTON,
Data Scientist, Dojo Madness

Twitter: [@louis_guitton](https://twitter.com/louis_guitton)

## Present slides
```bash
jupyter nbconvert part1/demo1/Example\ Machine\ Learning\ Notebook.ipynb --to slides --post serve
```

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
This will give you the IP address of the notebook. Combine this to the address given by the console

example: http://178.5.158.196:8888/?token=30491c22aab05ff61757c9d59d911fd2150247e520ff9283

## Part 1: Introduction to Machine Learning - Louis Guitton

Slides: http://bit.ly/log-ifpschool

* Demo 1 : Flower Classification

* Demo 2 : Simplest Neural Network

* Demo 3 : Cats vs Dogs

## Part 2: Flexibility, the Challenge of the Power System - Basile Bouquet

## Part 3: Building Energy Demand Prediction - Louis Guitton

## Part 4: PV Forecast at Rueil Malmaison - Basile Bouquet
