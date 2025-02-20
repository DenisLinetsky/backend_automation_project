# Base image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Define environment variables
ENV FLASK_APP=worker.py

# Expose port
EXPOSE 5001

# Run the command to start the Flask app
CMD ["flask", "run", "--host=0.0.0.0", "--port=5001"]
