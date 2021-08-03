# Docker pipeline with ETL, sentiment analysis and posting on Slack
 

## Table of Contents
- [General info](#general-info)
- [Technologies and Libraries](#technologies-and-libraries)
- [Setup](#setup)
- [Status](#status)

### General info
This project is about how to built a docker-pipeline which consists of a tweet collector, its sentiment analysis and posting them via slack bot.  
Every 10 minutes the last tweet about Covid is collected, saved into a database and shared in Slack.  
The following steps are applied:
- Docker Image, Container, Compose
- Twitter API
- Slack API
- Logging
- .env -> key protection
- polling method

### Technologies and Libraries
- Python 3.8
	- requests
	- pandas
	- logging
	- tweepy
	- vaderSentiment
	- sqlalchemy
	- dotenv
	- time
- PostgreSQL
- docker 

### Setup
The main reason of using docker-container is to make setup easy and applyable on any machine.
Before creating Docker-Containers, you need a Twitter Developer Account to get `API KEY`, `API SECRET` and `access token`, `access token secret`.  
You can apply twitter dev-acc [here](https://developer.twitter.com/en/apply).  
After you've got the API-key and the API-secret, you are ready to create Docker-Compose using Docker commands:
- For running these commands you need to `cd` into the folder that contains the `docker-compose.yml` file.

- (re-)build images of services 
    ```
    docker-compose build
    ```

- run/start containers in the background
    ```
    docker-compose run -d
    ```

- list all running containers/ services
    ```
    docker-compose ps
    ```

- view the output of individual services
    ```
    docker-compose logs <servicename>
    ```


