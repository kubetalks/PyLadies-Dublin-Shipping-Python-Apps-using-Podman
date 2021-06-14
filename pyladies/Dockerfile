FROM python:3-slim-buster

LABEL maintainer="Elif Samedin <elif.samedin@gmail.com>"

# Set build-time variables


# Set environment variables
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
# Prevent Python from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE 1
# Prevent Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED 1

# Define the working directory of the container
WORKDIR /usr/src/app

# Copy requirements.txt to container image
COPY ./requirements.txt ./

# Install the required dependencies
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copy source code to container image
COPY . .

CMD ["/usr/local/bin/gunicorn pyladies.wsgi:application -b :8000 -w 2"]