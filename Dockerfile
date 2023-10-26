# Use the Python 3.8 image as the base image (FROM python:3.8-slim-buster)
FROM python:3.11-slim-buster

# Update the package repository and install the AWS CLI
RUN apt update -y && apt install awscli -y

# Set the working directory inside the container to /app
WORKDIR /app

# Copy the contents of the local directory to the /app directory in the container
COPY . /app

# Install Python dependencies from the requirements.txt file
RUN pip install -r requirements.txt

# Install and upgrade the "accelerate" Python package
RUN pip install --upgrade accelerate

# Uninstall any existing "transformers" and "accelerate" packages
RUN pip uninstall -y transformers accelerate

# Install the "transformers" and "accelerate" packages
RUN pip install transformers accelerate

# Specify the command to run when the container is started (app.py)
CMD ["python3", "app.py"]
