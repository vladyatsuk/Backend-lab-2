# Prerequisites

1.  Install [Python](https://www.python.org/downloads/)
2.  Install [Docker](https://www.docker.com/products/docker-desktop/)

# How to use

1.  Clone repository:
    ```
    $ git clone https://github.com/vladyatsuk/Backend-lab-1.git
    ```
2.  Run in project directory:
    ```
    $ python -m venv env
    ```
    ```
    $ ./env/Scripts/activate   # for Windows
    $ source /env/bin/activate # for Linux
    ```
    ```
    $ python -m pip install -r requirements.txt
    ```
    ## Run app manually:
    ```
    $ flask --app my_app run -h 0.0.0.0 -p <your_port>
    ```
    ## Run with Docker
    Build the image:
    ```
    $ docker build -t <image_name>:latest . 
    ```
    Run the container:
    ```
    $ docker run -it --rm -e PORT=<your_port> <image_name>:latest
    ```
    ## Run with Docker Compose
    Build the image:
    ```
    $ docker compose build
    ```
    Run the container:
    ```
    $ docker compose up
    ```
    
    ## Check the result
    Visit [127.0.0.1](127.0.0.1):<your_port>/healthcheck to see the response