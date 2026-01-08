import os
import logging
from dotenv import load_dotenv
from passlib.context import CryptContext
from pathlib import Path

load_dotenv()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

DB_NAME = os.getenv("DB_NAME", 'crm_core')
DB_USER = os.getenv("DB_USER", 'postgres')
DB_PASSWORD = os.getenv("DB_PASSWORD", 'postgres')
PUBLIC_KEY = Path(os.getenv("PUBLIC_KEY_PATH", "None")).read_text()


SECRET_AGENT_KEY = os.getenv("SECRET_AGENT_KEY", "1234")


RABBIT_URL = os.getenv("RABBIT_URL", "amqp://guest:guest@localhost/")
EXCHANGE_NAME = "events"
