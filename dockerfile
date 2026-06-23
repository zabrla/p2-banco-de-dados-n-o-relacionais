FROM python:3.11-slim
WORKDIR /the/workdir/path /app
ENV pythondontwritebytecode=1
ENV pythonunbuffered=1
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY app ./app
COPY test_main.py .
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]