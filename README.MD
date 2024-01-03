# MICROSERVICE-TEMPLATE

This repository contains the template for a microservice. It is based on the Google Cloud Functions Framework.

## Steps to setup the project:

1. Install python3 (Version 3.12) and pip3 
2. In your terminal run: `python3 -m venv env`
3. In your terminal run: `source env/bin/activate` (Should be done every time you open a new terminal or a new instance)
4. In your terminal run: `python3 -m pip install -r requirements.txt`
5. Copy the .env.example file and rename it to .env: `cp .env.example .env`
6. Change the name of the database in the .env file and docker-compose.yml file (Default is: microservice-db)
7. Install and open the Docker Desktop App
8. In your terminal run: `docker-compose up -d` to start the database
9. Update / Add the database models in the schema.prisma file
10. In your terminal run: `prisma db push` to create the database schema

## Run the project:

Things you should do before you run the project:

1. Enter the virtual environment: `source env/bin/activate`
2. Start the database: `docker-compose up -d`

You can run the project in two ways:

1. Run the cloud function -> In your terminal run: `functions-framework --target=http_function`
2. Run the main.py file -> In your terminal run: `python3 main.py`
   The second option is during development more convenient, because you don't have to restart the cloud function every time you change something.
   Please note that you should ONLY run the second option during development, because the environment is a little bit different than the cloud function runtime.
   So if you want to test the cloud function, you should use the first option.

## How to update the database schema:

1. Update the schema.prisma file
2. In your terminal run: `prisma db push` (This will delete all data in the database; If you don't want to delete the data, have a look at the prisma documentation: https://www.prisma.io/docs/orm/prisma-migrate/getting-started)

## Further information

- Official Prisma Website: https://www.prisma.io
- Python Prisma Client: https://prisma-client-py.readthedocs.io/en/stable/
- Google Cloud Functions Framework: https://cloud.google.com/functions/docs/concepts/overview
- HTTP Methods Types in Google Cloud Functions: https://cloud.google.com/functions/docs/samples/functions-http-method#functions_http_method-python

If you need further help or information, you can contact Christian
