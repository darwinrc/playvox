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
The recommended way to start all of the applications together is executing the `./start.sh` script in the root project folder. 
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


## Endpoint definitions
### Users resource

| Method        | Url           | Description  | Example |
| ------------- | ------------- | ----- | ------------- |
| GET | http://localhost:5000/v1/users | Returns all users | Response body: <pre>[{<br>"_id":"5d14df84f3bd7bafe4359e89",<br>"first_name": "Carl",<br>"last_name": "Sagan",<br>"age": 62,<br>"sex": "M",<br>"email": "carl@sagan.com",<br>"registration_date":"1934-11-04"},<br>{<br>"_id":"5d14df84f3bd7bafe4359e89",<br>"first_name": "Cecilia",<br>"last_name": "Payne",<br>"age": 79,<br>"sex": "F",<br>"email": "cecilia@payne.com",<br>"registration_date":"1900-05-10"<br>}]</pre> |
| POST| http://localhost:5000/v1/users | Creates a user | Request body: <pre>{<br>"first_name": "Margaret",<br>"last_name": "Hamilton",<br>"age": 82,<br>"sex": "F",<br>"email": "margaret@hamilton.com",<br>"registration_date":"1936-08-17"<br>}</pre> Response body: <pre>{<br>"_id":"5d16121a60833f8fc1f53e41",<br>"first_name": "Margaret",<br>"last_name": "Hamilton",<br>"age": 82,<br>"sex": "F",<br>"email": "margaret@hamilton.com",<br>"registration_date":"1936-08-17"<br>}</pre> |
| PUT | http://localhost:5000/v1/users/5d14df84f3bd7bafe4359e89 | Updates the user with the id `5d14df84f3bd7bafe4359e89` | Request body: <pre>{<br>"first_name": "Cecilia",<br>"last_name": "Payne",<br>"age": 99,<br>"sex": "F",<br>"email": "cecilia@payne.com",<br>"registration_date":"1990-05-10"<br>}</pre>Response body: <pre>{<br>"_id":"5d14df84f3bd7bafe4359e89",<br>"first_name": "Cecilia",<br>"last_name": "Payne",<br>"age": 99,<br>"sex": "F",<br>"email": "cecilia@payne.com",<br>"registration_date":"1990-05-10"<br>}</pre> |
| DELETE | http://localhost:5000/v1/users/5d14df84f3bd7bafe4359e89 | Deletes the user with the id hash `5d14df84f3bd7bafe4359e89` | Response body: <pre>{"message": "succesfully deleted the user."}</pre> |
| GET | http://localhost:5000/v1/users/5d16121a60833f8fc1f53e41 | Gets the user with the id `5d16121a60833f8fc1f53e41` | Response body: <pre>{<br>"_id":"5d16121a60833f8fc1f53e41",<br>"first_name": "Margaret",<br>"last_name": "Hamilton",<br>"age": 82,<br>"sex": "F",<br>"email": "margaret@hamilton.com",<br>"registration_date":"1936-08-17"<br>}</pre> |
| GET | http://localhost:5000/v1/users?query={"first_name": "Margaret", "sex": "F"} | Gets the users with the first name `Margaret` and sex `F`. Filter properties can be any combination of `first_name`, `last_name`, `email`, or `sex` | Response body: <pre>{<br>"_id":"5d16121a60833f8fc1f53e41",<br>"first_name": "Margaret",<br>"last_name": "Hamilton",<br>"age": 82,<br>"sex": "F",<br>"email": "margaret@hamilton.com",<br>"registration_date":"1936-08-17"<br>}</pre> |

### Notes resource

| Method        | Url           | Description  | Example |
| ------------- | ------------- | ----- | ------------- |
| GET | http://localhost:5001/v1/users/5d16163860833f8fc1f53e42/notes | Returns all notes for the user with the hash id `5d16163860833f8fc1f53e42` | Response body: <pre>[{<br>"_id": "5d1616793254b41f013151c2",<br>"user_id": "5d16163860833f8fc1f53e42",<br>"title": "The Cosmos Awaits",<br>"body": "At the edge of forever decipherment laws of physics the ash of stellar alchemy tingling of the spine across the centuries.",<br>"note_date": "2019-06-27T18:25:43"<br>},<br>{<br>"_id": "5d1616d53254b41f013151c3",<br>"user_id": "5d16163860833f8fc1f53e42",<br>"title": "Pale Blue Dot",<br>"body": "The only home we've ever known gathered by gravity a very small stage in a vast cosmic arena the sky calls to us.",<br>"note_date": "2019-06-28T08:25:43"<br>}]</pre> |
| POST| http://localhost:5001/v1/users/5d16163860833f8fc1f53e42/notes | Creates a note for the user with the hash id `5d16163860833f8fc1f53e42` | Request body: <pre>{<br>"user_id": "5d16163860833f8fc1f53e42",<br>"title": "Shadows of Forgotten Ancestors",<br>"body": "Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur and billions upon billions upon billions upon billions upon billions upon billions upon billions.",<br>"note_date": "2019-06-28T08:25:43"}</pre> Response body: <pre>{<br>"_id": "5d1616d53254b41f013151c3",<br>"user_id": "5d16163860833f8fc1f53e42",<br>"title": "Shadows of Forgotten Ancestors",<br>"body": "Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur and billions upon billions upon billions upon billions upon billions upon billions upon billions.",<br>"note_date": "2019-06-28T08:25:43"<br>}</pre> |
