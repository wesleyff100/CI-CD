# FastAPI Hello World

A simple API using FastAPI that returns "Hello World" with timestamp.

## 🚀 Features

- `/` endpoint that returns a greeting message with timestamp
- Auto-reload during development
- Automatic API documentation

## 🛠️ Technologies

- **FastAPI** - Modern and fast web framework
- **Uvicorn** - ASGI server for Python applications
- **Python 3.11+**

## 📋 Prerequisites

- Python 3.11 or higher
- pip (Python package manager)

## ⚙️ Installation

1. Clone the repository:
```bash
git clone https://github.com/wesleyff100/CI-CD.git
cd CI-CD
```

2. Create a virtual environment:
```bash
python -m venv .venv
```

3. Activate the virtual environment:
```bash
# Windows
.\.venv\Scripts\Activate.ps1

# Linux/Mac
source .venv/bin/activate
```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

## 🏃‍♂️ How to run

```bash
uvicorn main:app --reload
```

The API will be available at: http://127.0.0.1:8000

## 📖 Documentation

- **Swagger UI**: http://127.0.0.1:8000/docs
- **ReDoc**: http://127.0.0.1:8000/redoc

## 🧪 Testing the API

Access http://127.0.0.1:8000/ and you will receive a response like:

```json
{
  "message": "Hello World",
  "timestamp": "2025-09-08T14:30:45.123456"
}
```

## 🔍 CI/CD

The project includes GitHub Actions for:
- **Lint**: Code quality checking with pylint

## 📝 Project Structure

```
├── main.py              # Main API file
├── requirements.txt     # Project dependencies
├── dockerfile          # Docker container
├── README.md           # This file
└── .github/
    └── workflows/
        └── python-lint.yml  # Lint workflow
```