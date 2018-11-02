# Build on a complete production ready nginx image
FROM tiangolo/uwsgi-nginx-flask:python3.7

# Copy the application to our docker image
# it will start automatically since it has the default name main.py
ADD . /app

# Install dependencies into docker image
RUN pip install -r requirements.txt

# we need to specify the mongo server when running in docker compose
ENV MONGOHOST mongodb

# To build using "docker-compose build"
# To run "docker-compoes up"
# To reset run "docker-compose down"
