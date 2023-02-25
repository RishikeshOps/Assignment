# Assignment

To get this repository, run the following command inside your git enabled terminal

$ git clone https://github.com/RishikeshOps/Assignment.git

# Task-1
## Setup

Once you Cloned repo then run the following command for Task-1 `cd Task-1/` 

## For Python Server 
1) Build the Docker image using the following command: `docker build -t python-server .`

2) Start a Docker container using the following command: `
docker run -p 8080:8080 python-server`

3) Access the web server by opening a web browser and navigating to http://localhost:8080.

## PHP Server

1) Build the Docker image using the following command: `docker build -t php-server -f Dockerfile_php .`

2) Start a Docker container using the following command: `docker run -p 80:80 php-server`

3) Access the web server by opening a web browser and navigating to http://localhost.

# Task-3

## Unit Test for atg.world Website ( You can use any website URL for testing )
This repository contains a unit test that checks whether the atg.world website is loading properly. If the website loads correctly, the unit test should pass. If the website fails to load, the unit test should fail.

Once you Cloned repo then run the following command for Task-1 `cd Task-3/`

### Prerequisites
Before running the unit test, make sure that you have the following software installed:

- Python 3.x
- pytest (a Python testing framework)
- requests (a Python library for making HTTP requests)

### Running the Unit Test
To run the unit test, follow these steps:

1) Clone this repository to your local machine.

2) Open the terminal and navigate to the Task-3 Folder.

3) Open the *loadind_test.py* file in a text editor and replace the `url` variable with the URL of the any website.
example: url = "https://jenkins.rushikesh.me/" "https://rushikesh.me/" "https://www.google.com/Save the changes to the file.

4) Save the changes to the file.

5) Run the following command to execute the unit test: `pytest`

You should see the results of the unit test in the terminal. If the website loads correctly, the test should pass. If the website fails to load, the test should fail.
