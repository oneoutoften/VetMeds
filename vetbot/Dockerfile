FROM python:3.9-slim

RUN apt-get update && apt-get install -y locales \
    && sed -i -e 's/# ru_RU.UTF-8 UTF-8/ru_RU.UTF-8/' /etc/locale.gen \
    && dpkg-reconfigure --frontend=noninteractive locales

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app .

CMD ["python", "main.py"]