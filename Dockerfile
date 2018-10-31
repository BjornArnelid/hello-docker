# Build on a complete production ready nginx image
FROM tiangolo/uwsgi-nginx-flask:python3.7

# Copy the application to our docker image
# it will start automatically since it has the default name main.py
ADD . /app

# To build using "docker build . -t hello-docker"
# To run "docker run hello-docker"
