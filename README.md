# Web scrapping & Api

## About the project

A FastApi application that retrieve articles from https://techcrunch.com/ according to their category

## Prerequisites

Windows environment

Docker

Python

## Installation

1. Setups
```
    pip install -r requirements.txt
    git clone https://github.com/AtoutPillard/Web_Scrapping.git
    docker pull mongo
    docker build . --file Dockerfile --tag webscrapping_api
    docker-compose up --build -d
```

2. Web Scrapping
```
    python web_scrapping.py   
```

The app runs on http://127.0.0.1:8000/docs#/

