from tortoise import fields
from app.models.base import BaseModelTenant, BaseModelPK


    
# class ProfileRole(BaseModelPK):
#     profile = fields.ForeignKeyField('models.Profile', on_delete=fields.CASCADE)
#     role = fields.ForeignKeyField('models.Role', on_delete=fields.CASCADE)

class Profile(BaseModelPK):
    user_id = fields.IntField(uniquenique=True, null=False)
    name = fields.CharField(max_length=255, null=True)
    surname = fields.CharField(max_length=255, null=True)
    pathronamic = fields.CharField(max_length=255, null=True)
    role = fields.ForeignKeyField('models.Role', on_delete=fields.CASCADE)

    class Meta:
        table = 'profiles'


# class ManagerProfile(BaseModelTenant):
#     user_id = fields.IntField(uniquenique=True, null=False)
#     employee = fields.OneToOneField("models.Employee", related_name="profile")
    
#     first_name = fields.CharField(max_length=200)
#     surname = fields.CharField(max_length=200)
#     patronymic = fields.CharField(max_length=200, null=True)

#     class Meta:
#         table = "manager_profiles"
    

# class TeacherProfile(BaseModelTenant):
#     user_id = fields.IntField(uniquenique=True, null=False)
#     teacher = fields.OneToOneField("models.Teacher", related_name="profile")

#     first_name = fields.CharField(max_length=200)
#     surname = fields.CharField(max_length=200)
#     patronymic = fields.CharField(max_length=200, null=True)

#     class Meta:
#         table = "teacher_profiles"


# class StudentProfile(BaseModelTenant):
#     user_id = fields.IntField(uniquenique=True, null=False)
#     student = fields.OneToOneField("models.Student", related_name="profile")

#     first_name = fields.CharField(max_length=200)
#     surname = fields.CharField(max_length=200)
#     patronymic = fields.CharField(max_length=200, null=True)

#     class Meta:
#         table = "student_profiles"
