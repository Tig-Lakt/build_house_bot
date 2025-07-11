FROM python:3.10-slim-buster

WORKDIR /build_house_bot

COPY requirements.txt .
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

RUN apt-get update && apt-get install -y \
    vim \
    --no-install-recommends

COPY . .
CMD ["python", "src/main.py"]