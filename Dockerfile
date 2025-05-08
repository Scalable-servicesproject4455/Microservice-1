# s1/Dockerfile
FROM python:3.10-slim

WORKDIR /app
COPY ServiceOne.py .

RUN pip install flask

EXPOSE 5000
CMD ["python", "ServiceOne.py"]
