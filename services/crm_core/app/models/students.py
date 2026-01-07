from typing import Any
from app.models.base import BaseModelPK, BaseModelTenant
from tortoise import fields 


class Student(BaseModelTenant):
    name = fields.CharField(max_length=100)
    surname = fields.CharField(max_length=100)
    progress = fields.DecimalField(max_digits=5, decimal_places=2, default=0)
    birthday = fields.DateField()
    score = fields.IntField(default=0)

    class Meta: 
        table = 'student'

    def __str__(self):
        return self.name


class StudentGroup(BaseModelTenant):
    title = fields.CharField(max_length=255)
    students: fields.ManyToManyRelation[Student] = fields.ManyToManyField("models.Student", related_name='groups')

    class Meta:
        table = 'student_group'

    def __str__(self) -> str:
        return self.title
