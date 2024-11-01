# Stage 1: Base stage
FROM python:3.9-slim AS base

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    FLASK_APP=challenge/app.py \
    FLASK_ENV=production

# Install dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Stage 2: Builder stage
FROM base AS builder

# Create working directory
WORKDIR /app

# Copy requirements file and install dependencies
COPY challenge/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Stage 3: Final stage
FROM base AS final

# Set up application directory and copy app code
WORKDIR /app
COPY --from=builder /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages
COPY challenge /app/challenge

# Expose the Flask port
EXPOSE 5000
COPY ./flag.txt /flag.txt
# Run Flask application
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0", "--port=5000"]
