from typing import TypeVar, Optional, List, Type
from tortoise import Model
from tortoise.queryset import QuerySet, QuerySetSingle
from abc import ABC, abstractmethod
from app.models.base import BaseModelPK
from app.decorators import handle_relations
from app.repositories.base import AbstractRepository, M

from app.models.employee import Employee, Teacher, Department
from app.models.lessons import Lesson, Subject, Classroom, PeriodLesson
from app.models.organization import Organization, OrganizationMember
from app.models.students import Student, StudentGroupMember
from app.models.group import StudentGroup
from app.models.grade import Grade
from app.models.invite import Invite
from app.models.permission import Permission, RolePermission
from app.models.role import Role, ProfileRole
from app.models.score_transaction import Accrual
from app.models.attendance import Attendance
from app.models.profile import Profile




class TortoiseRepository(AbstractRepository):    
    model: type[M]
    tenant_aware: bool = False

    def __init__(self):
        assert hasattr(self, "model"), "Repository must define model"

        if self.tenant_aware:
            assert "org" in self.model._meta.fields_map, (
                f"{self.model.__name__} must have org field"
            )
        self.m2m_fields: list = self.get_m2m_fields()
        self.fk_fields: list  = self.get_fk_fields()


    def base_qs(self, **filters) -> QuerySet[M]:
        return self.model.all().filter(**filters)
    

    async def prefetch_obj(self, obj: M) -> M:
        if self.m2m_fields:
            for field_name in self.m2m_fields:
                await obj.fetch_related(field_name)
        return obj
    

    async def prefetch_queryset(self, qs: QuerySet[M]) -> QuerySet[M]:
        if self.m2m_fields:
            return qs.prefetch_related(*self.m2m_fields)
        return qs
    

    async def get_all(self, **filters) -> QuerySet[M]:
        return self.base_qs(**filters)
    
    
    async def paginate_get_all(
        self,
        *,
        limit: int = 20,
        offset: int = 0,
        **filters
    ) -> QuerySet[M]:
        return (
            self.base_qs(**filters)
            .limit(limit)
            .offset(offset)
        )


    async def get(self, **filters) -> M:
        return await self.model.get_or_none(**filters)
    

    @handle_relations
    async def create(self, **data) -> M:
        return await self.model.create(**data)
    

    @handle_relations
    async def update(self, obj: M, **data) -> M:
        await obj.update_from_dict(data)
        await obj.save()
        return obj


    def get_m2m_fields(self) -> set:
        return self.model._meta.m2m_fields
    
    
    def get_fk_fields(self) -> set:
        return self.model._meta.fk_fields
    

    def extract_relation_fields(self, **data) -> tuple[dict, dict, dict]:
        m2m_relation_data = {field: data.pop(field) for field in list(data.keys()) if field in self.m2m_fields}
        fk_relation_data = {field: data.pop(field) for field in list(data.keys()) if field in self.fk_fields}

        return m2m_relation_data, fk_relation_data, data
    

    async def delete(self, obj: M):
        return await obj.delete()
    
    
    async def handle_fk_relations(self, obj: M, fk_data: dict[str, int]):
        if not fk_data:
            return
        for field, value in fk_data.items():
            if value is not None:
                setattr(obj, f"{field}_id", value)
        await obj.save()

class TenantRepository(TortoiseRepository):
    tenant_aware = True

    def __init__(self, org):
        super().__init__()
        self.org = org

    def base_qs(self, **filters):
        return super().base_qs(org=self.org, **filters)
    
    @handle_relations
    async def create(self, **data):
        return await super().create(org=self.org, **data)
    
    @handle_relations
    async def update(self, obj: M, **data):
        data.pop("org", None)
        return await super().update(obj, **data)
    
    async def transfer_to_org(self, obj: M, new_org):
        obj.org = new_org
        await obj.save(update_fields=("org",))
        return obj


class EmployeeRepository(TenantRepository):
    model = Employee

class TeacherRepository(TenantRepository):
    model = Teacher

class DepartamentRepository(TenantRepository):
    model = Department

class AttendanceRepository(TenantRepository):
    model = Attendance

class GradeRepository(TenantRepository):
    model = Grade

class StudentGroupRepository(TenantRepository):
    model = StudentGroup

class InviteRepository(TenantRepository):
    model = Invite

class ClassroomRepository(TenantRepository):
    model = Classroom

class SubjectRepository(TenantRepository):
    model = Subject

class PeriodLessonRepository(TenantRepository):
    model = PeriodLesson

class LessonRepository(TenantRepository):
    model = Lesson

class OrganizationMemberRepository(TenantRepository):
    model = OrganizationMember

class OrganizationRepository(TortoiseRepository):
    model = Organization

class PermissionRepository(TortoiseRepository):
    model = Permission

class RolePermissionRepository(TortoiseRepository):
    model = RolePermission

class ProfileRepository(TenantRepository):
    model = Profile

class RoleRepository(TortoiseRepository):
    model = Role

class ProfileRoleRepository(TortoiseRepository):
    model = ProfileRole

class AccrualRepository(TenantRepository):
    model = Accrual

class StudentRepository(TenantRepository):
    model = Student

class StudentGroupMemberRepository(TenantRepository):
    model = StudentGroupMember

