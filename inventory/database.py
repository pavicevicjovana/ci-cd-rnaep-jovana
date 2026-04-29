import os
from dotenv import load_dotenv
from redis_om import get_redis_connection

# Učitavamo promenljive iz .env fajla
load_dotenv()
# Izvlačimo podatke koristeći os.getenv
REDIS_HOST=os.getenv("REDIS_HOST","localhost")
REDIS_PORT=os.getenv("REDIS_PORT","6379")
REDIS_PASSWORD=os.getenv("REDIS_PASSWORD",None)

#Kreiranje konekcije
redis = get_redis_connection(
    host = REDIS_HOST,
    port=int(REDIS_PORT),
    password=REDIS_PASSWORD,
    decode_responses=True
    )