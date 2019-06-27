# Playvox Users Hub


## Requirements:

### Docker
Download and install Docker. 
If you are on a Mac (see https://docs.docker.com/docker-for-mac/install).
If you are on Ubuntu (https://docs.docker.com/install/linux/docker-ce/ubuntu/). 

### Foreman (task runner)
Foreman is optional but the recommended way to run all of the microservices and
applications together. Install from https://github.com/ddollar/foreman. 


## Running the development environment

The local development environment consists of 3 docker containers. 
- The first container includes a python server with flask and a mongodb server which communicates using `docker-compose`, and it hosts the `users` microservice.
- The second container includes a python server with flask and a mongodb server which communicates using `docker-compose`, and it hosts the `notes` microservice.
- The third container includes a node http server, and it hosts the `vuejs` frontend application.

#### Running the application
The recommended way to start all of the applications together is executing the `./up.sh` script in the root project folder. 
This will use Foreman to execute the three docker containers. 

- Access the front-end site with the following URLs: `http://localhost:8080`
- Access the users microservice API endpoints with the following URLs: `http://localhost:5000/v1/users`
- Access the notes microservice API endpoints with the following URLs: `http://localhost:5001/v1/users/<user_id>/notes`, being `<user_id>` the hash id for a user.

#### Running Users Microservice Separately
The users microservice can be started executing the `make users` command, which in turn executes `cd ./playvox_users && docker-compose build && docker-compose up`.

#### Running Notes Microservice Separately
The users microservice can be started executing the `make notes` command, which in turn executes `cd ./playvox_notes && docker-compose build && docker-compose up`.

#### Running Frontend Application Separately
The vuejs frontend application can be started executing the `make ui` command, which in turn executes `cd ./playvox_ui && docker-compose build && docker-compose up`.
