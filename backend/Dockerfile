FROM python:3.11-slim

# Set working directory (IMPORTANT)
WORKDIR /app

# Copy requirements first
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy full code
COPY . .

# Expose port
EXPOSE 5000

# Run as module (VERY IMPORTANT FIX)
CMD ["python", "-m", "app.app"]