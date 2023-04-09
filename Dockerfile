FROM python:3.11.3-buster
COPY main.py /app/main.py
CMD ["python", "/app/main.py"]