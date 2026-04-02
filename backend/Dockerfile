#BASE IMAGE
FROM python:3.11-slim

#Set working Directory
WORKDIR /app/app

#Copy dependencies first
COPY requirements.txt .

#Install Dependencies
RUN pip install --no-cache-dir -r requirements.txt

#Copy App Code
COPY . .

#Expose port
EXPOSE 5000

#Run Application
CMD ["python3", "app.py"]
