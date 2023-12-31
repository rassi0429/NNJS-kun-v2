FROM python:3.9
WORKDIR /app
COPY . .
COPY requirements.txt .
RUN pip install -r requirements.txt
CMD ["python", "-u", "nnjskun.py"]