# syntax=docker/dockerfile:1
FROM python:3
# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PORT=8000

# Set work directory
WORKDIR /code
COPY requirements.txt /code/

# Install dependencies
RUN pip install -r requirements.txt
# Copy project
COPY . /code/
CMD python manage.py runserver 0.0.0.0:8000