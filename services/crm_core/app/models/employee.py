from app.models.base import BaseModelPK, BaseModelTenant
from tortoise import fields


class Department(BaseModelTenant):
    name = fields.CharField(max_length=100)
    code = fields.IntField()

    class Meta: 
        table ="department"


class Employee(BaseModelTenant):
    name = fields.CharField(max_length=100)
    surname = fields.CharField(max_length=100)
    patronymic = fields.CharField(max_length=100, null=True)
    department: fields.ForeignKeyNullableRelation[Department] = fields.ForeignKeyField(
        "models.Department", related_name="employees", null=True
    )
    email = fields.CharField(max_length=255, null=True)

    class Meta:
        table = "employee"

    def __str__(self):
        return f"Сотрудник {self.name} {self.surname}"


class Teacher(BaseModelTenant):
    name = fields.CharField(max_length=100)
    surname = fields.CharField(max_length=100)
    patronymic = fields.CharField(max_length=100, null=True)
    department: fields.ForeignKeyNullableRelation[Department] = fields.ForeignKeyField(
        "models.Department", related_name="employees", null=True
    )
    email = fields.CharField(max_length=255, null=True)
    
    class Meta:
        table = "teacher"

    def __str__(self):
        return f"{self.employee.name} {self.employee.surname}"
