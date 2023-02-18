# Assignment

## Setup
To get this repository, run the following command inside your git enabled terminal

$ git clone https://github.com/RishikeshOps/Assignment.git

Once you Cloned repo then run the following command `cd Task-1/` 

# Task-1
## For Python Server 
1) Build the Docker image using the following command: `docker build -t python-server .`

2) Start a Docker container using the following command: `
docker run -p 8080:8080 python-server`

3) Access the web server by opening a web browser and navigating to http://localhost:8080.

## PHP Server

1) Build the Docker image using the following command: `docker build -t php-server -f Dockerfile_php .`

2) Start a Docker container using the following command: `docker run -p 80:80 php-server`

3) Access the web server by opening a web browser and navigating to http://localhost.
