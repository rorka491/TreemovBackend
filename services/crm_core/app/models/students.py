from typing import Any
from app.models.base import BaseModelPK, BaseModelTenant
<<<<<<< HEAD
from tortoise import fields 
=======
from tortoise import fields
>>>>>>> dima


class Student(BaseModelTenant):
    name = fields.CharField(max_length=100)
    surname = fields.CharField(max_length=100)
    progress = fields.DecimalField(max_digits=5, decimal_places=2, default=0)
    birthday = fields.DateField()
    score = fields.IntField(default=0)
<<<<<<< HEAD

    class Meta: 
        table = 'student'
=======
    class Meta: 
        table = 'students'
>>>>>>> dima

    def __str__(self):
        return self.name


<<<<<<< HEAD
class StudentGroup(BaseModelTenant):
    title = fields.CharField(max_length=255)
    students: fields.ManyToManyRelation[Student] = fields.ManyToManyField("models.Student", related_name='groups')

    class Meta:
        table = 'student_group'
=======
class StudentGroupMember(BaseModelTenant):
    student = fields.ForeignKeyField(
        "models.Student",
        related_name="students"
    )
    group = fields.ForeignKeyField(
        "models.Group",
        related_name="groups"
    )

    class Meta:
        table = 'student_group_members'
>>>>>>> dima

    def __str__(self) -> str:
        return self.title
