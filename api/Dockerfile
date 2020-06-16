FROM python:3.7

RUN apt-get update -y

# We copy just the requirements.txt first to leverage Docker cache 
WORKDIR /app  

COPY requirements.txt /app/
COPY api.py /app/  
COPY pg_config.py /app/
COPY pgqueries /app/pgqueries

RUN pip install -r requirements.txt  

ENTRYPOINT [ "python" ]  
CMD [ "api.py" ]

