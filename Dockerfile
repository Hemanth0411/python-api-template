# Phase 1: Use an official, lean Python runtime as a parent image
FROM python:3.11-slim AS base

# Set environment variables using the modern key=value format
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Create a non-root user for enhanced security
RUN addgroup --system app && adduser --system --group app

# Phase 2: Install dependencies
# Copy only the requirements file to leverage Docker's build cache.
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Phase 3: Copy source code
# Switch to the non-root user before copying the application code
USER app
COPY ./src .

# Expose the port the app will run on
EXPOSE 8000

# Define the command to run the application
# --host 0.0.0.0 is required to make it accessible from outside the container.
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]