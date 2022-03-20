FROM python:3.8-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
    apt-get install -y libpq-dev gcc python3.8-dev

#================================================================
# pip install required modules
#================================================================

RUN pip install --upgrade setuptools pip
COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

#==================================================
# Copy the latest code
#==================================================

RUN mkdir -p /events-scraper
WORKDIR /events-scraper
COPY . /events-scraper

# Expose server port
EXPOSE 8000

CMD /bin/bash run.sh