# Voliboli backend

## Install dependecies

In the root of the repository, first run:

	pipenv install
	
then you can run tests:

	pipenv run python api_test.py
	
## Backend

Since the amount of retrieved data can be quite large, depending upon the request we utilize GraphQL protocol to already prefilter data on the server side and only retrieve the requested data to the client. GraphQL is used with the Flask server that stored data to a Postgres database and awaits the requests from the frontend. 
	
