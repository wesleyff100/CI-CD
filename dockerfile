# Use Python 3.11 slim image as base
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install "fastapi[standard]"

COPY . .

EXPOSE 80

# Command to run the application
CMD ["fastapi", "run", "main.py", "--port", "80"]