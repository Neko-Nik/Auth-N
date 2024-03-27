# official Debian 12 base image
FROM python:3.12-bookworm

# No user intraction for this 
ENV DEBIAN_FRONTEND noninteractive

## Set them as environment variables so that they can be used in the gunicorn command
ENV GUNICORN_ARG_WORKERS 6
ENV GUNICORN_ARG_THREADS 6
ENV GUNICORN_ARG_TIMEOUT 2500
ENV GUNICORN_ARG_BIND_PORT 8086
ENV LOG_LEVEL 20
ENV NUMBER_OF_LOGS_TO_DISPLAY 100

# Update the package lists
RUN apt-get update

# Install essential packages
RUN apt-get install -y gcc python3.11-dev

# Copy requirements files to do pip install
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Create direcotry for FastAPI
RUN mkdir -p /app/src
RUN mkdir -p /app/templates
RUN mkdir -p /var/log/api

# Set the working directory
WORKDIR /app

# Copy the source code to the working directory
COPY src/ src/
COPY templates/ templates/
COPY app/ .
COPY entry_point.sh .

CMD ["chmod", "+x", "/app/entry_point.sh"]

# Health check for the image
HEALTHCHECK --interval=30s --timeout=7s --start-period=5s --retries=2 \
    CMD ["sh", "-c", "curl --fail http://localhost:${GUNICORN_ARG_BIND_PORT}/logs?passwd=neko-nik || exit 1"]

# Run the application using gunicorn
ENTRYPOINT ["sh", "/app/entry_point.sh"]
