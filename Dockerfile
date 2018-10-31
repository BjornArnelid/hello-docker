# Build on a complete production ready nginx image
FROM tiangolo/uwsgi-nginx-flask:python3.6

# Copy the application to our docker image
# it will start automatically since it has the default name main.py
COPY . /app