from enum import Enum

class BaseEnum(Enum):

    @classmethod
    def return_list(cls):
        return [el.value for el in cls]

    @classmethod
    def return_choices(cls):
        return [(el.name, el.value) for el in cls]


class UserRole(BaseEnum):
    ADMIN = 'Admin'
    MANAGER = 'Manager'
    TEACHER = 'Teacher'


