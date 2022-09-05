# Run Microservice

	DATABASE_IP=172.34.1.2 docker-compose up

## Install dependecies

In the root of the repository, first run:

	pipenv install
	
then you can run tests:

	pipenv run python api_test.py

## Sync database

In order to synchronize with the changes of databases, run:

	DATABASE_IP=172.34.1.2 pipenv run flask db upgrade

To apply the new changes to the database run (while the microservice is running):

	DATABASE_IP=172.34.1.2 pipenv run flask db migrate -m "<commit message>"
	DATABASE_IP=172.34.1.2 pipenv run flask db upgrade 
	
