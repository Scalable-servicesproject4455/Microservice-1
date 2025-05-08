# s1/Dockerfile
FROM python:3.10-slim

WORKDIR /app
COPY serviceOne.py .

RUN pip install flask

EXPOSE 5000
CMD ["python", "serviceOne.py"]
