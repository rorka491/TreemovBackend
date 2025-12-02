import os
import logging
from dotenv import load_dotenv
from passlib.context import CryptContext

load_dotenv()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


SECRET_KEY = os.getenv("SECRET_KEY", '12345')
ALGORITHM = os.getenv("ALGORITHM")
BASE_URL_ACCOUNTS_SERVICE = os.getenv("BASE_URL_ACCOUNTS_SERVICE")
SECRET_AGENT_KEY = os.getenv("SECRET_AGENT_KEY")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))
