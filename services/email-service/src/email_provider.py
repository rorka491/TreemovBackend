from abc import ABC, abstractmethod
import aiosmtplib
import ssl, certifi
from email.message import EmailMessage

ssl_context = ssl.create_default_context(cafile=certifi.where())


class EmailProvider(ABC):

    @abstractmethod
    async def send(
        self,
        to: str,
        subject: str,
        body: str,
    ) -> None:
        ...


class SMTPEmailProvider(EmailProvider):
    def __init__(
        self,
        host: str,
        port: int,
        username: str,
        password: str,
        use_tls: bool = True,
    ):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.use_tls = use_tls

    async def send(self, to: str, subject: str, body: str) -> None:
        message = EmailMessage()
        message["From"] = self.username
        message["To"] = to
        message["Subject"] = subject
        message.set_content(body)


        await aiosmtplib.send(
            message,
            hostname=self.host,
            port=self.port,
            username=self.username,
            password=self.password,
            start_tls=self.use_tls,
            timeout=10,
            tls_context=ssl_context
        )
