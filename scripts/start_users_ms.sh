#!/bin/bash
# this script starts the users microservice from the docker container

cd ./playvox_users && docker-compose build && docker-compose up
