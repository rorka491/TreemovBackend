from enum import StrEnum

class QueueEnum(StrEnum):
    EMAIL_REGISTER_VERIFIED = "email.register.verified"
    EMAIL_LOGIN_VERIFIED = 'email.login.verified'
    USER_CREATED = 'user.created'
    TEST_QUEUE = 'test.queue'