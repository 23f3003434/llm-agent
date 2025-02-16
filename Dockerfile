FROM python:3.12-slim-bookworm

# Prevent Python from writing pyc files to disk and enable unbuffered logging
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Upgrade pip
RUN pip install --upgrade pip

# Copy only the requirements file first to leverage Docker cache
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
# (Files/folders excluded via .dockerignore won't be copied)
COPY . /app
# Expose the port that uvicorn will run on
EXPOSE 8000

# Command to run the application with uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]