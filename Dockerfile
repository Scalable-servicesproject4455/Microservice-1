FROM python:3.10-slim
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000  # change to 8080 for microservice-2
CMD ["python", "app.py"]