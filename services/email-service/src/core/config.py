from dotenv import load_dotenv
import os
from passlib.hash import argon2


hasher = argon2.using(
    memory_cost=65536,
    time_cost=3,
    parallelism=4,
    salt_len=16,
    hash_len=32
)



load_dotenv()

DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_USER = os.getenv('DB_USER')
DB_NAME = os.getenv('DB_NAME')
HOST_ADRESS = os.getenv('HOST_ADRESS')
