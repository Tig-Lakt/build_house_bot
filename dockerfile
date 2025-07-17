FROM python:3.10-slim-bullseye  

WORKDIR /build_house_bot  

COPY requirements.txt .  
RUN python -m pip install --upgrade pip && \  
    pip install --no-cache-dir -r requirements.txt  

# Установка vim и очистка кеша apt  
RUN apt-get update && \  
    apt-get install -y --no-install-recommends vim && \  
    apt-get clean && \  
    rm -rf /var/lib/apt/lists/*  

COPY . .  

CMD ["python", "src/main.py"]  
~                              
