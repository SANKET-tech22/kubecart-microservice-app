FROM python:3.11-slim

# Step 1: root working dir
WORKDIR /app

# Step 2: copy requirements
COPY requirements.txt .

# Step 3: install deps
RUN pip install --no-cache-dir -r requirements.txt

# Step 4: copy full code
COPY . .

# Step 5: move into app folder
WORKDIR /app/app

# Step 6: run app
EXPOSE 5000
CMD ["python3", "app.py"]