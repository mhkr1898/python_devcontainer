# fetch image from microsoft
FROM mcr.microsoft.com/devcontainers/python:0-3.11

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /app 

# Install Debian updates and packages
RUN apt-get update && apt-get upgrade -y && apt-get install -y \
    && apt-get clean



