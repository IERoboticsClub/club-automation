# needs to have crone up and running, needs python 3.11, needs to install requirements.txt and run the dashboard.py streamlit app on an open port:
# Dockerfile
FROM python:3.11
RUN apt-get update && apt-get install -y cron
RUN pip install --upgrade pip
COPY requirements.txt /tmp/
RUN pip install --requirement /tmp/requirements.txt
COPY . /app
WORKDIR /app
CMD ["streamlit", "run", "dashboard.py"]
# setup commands:
# docker build -t dashboard .
# docker run -p 8501:8501 dashboard
# open browser and go to http://localhost:8501