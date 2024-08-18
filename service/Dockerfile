# Use the Python 3.11 slim base image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

COPY . ./

# Install Python dependencies from requirements file
RUN pip install -r requirements.txt

# Keep the container running
ENTRYPOINT [ "/app/scripts/entrypoint.sh" ]