from tortoise import fields
from tortoise.exceptions import ValidationError 
from app.models.base import BaseModelPK, BaseModelTenant
from app.fields import TimeDurationField
from app.utils.time_utils import time_diff


class Classroom(BaseModelTenant):
    title = fields.CharField(max_length=100)
    floor = fields.IntField(null=True, blank=True)
    building = fields.CharField(max_length=100, null=True, blank=True)

    class Meta:
        table = "classroom"

    def __str__(self):
        return f"Аудитория {self.title}"


class Subject(BaseModelTenant):
    title = fields.CharField(max_length=100)
    color = fields.CharField(max_length=7)


class AbstractLesson(BaseModelTenant):
    title = fields.CharField(max_length=200)
    start_time = fields.TimeField(
        null=True,
        description="Please use the following format: <em>YYYY-MM-DD</em>.",
    )
    end_time = fields.TimeField(
        null=True,
        description="Please use the following format: <em>YYYY-MM-DD</em>.",
    )
    teacher = fields.ForeignKeyField(
        'models.Teacher',
        on_delete=fields.CASCADE,
        null=True
    )
    classroom = fields.ForeignKeyField(
        'models.Classroom',
        on_delete=fields.SET_NULL,
        null=True
    )
    student_group = fields.ForeignKeyField(
        'models.StudentGroup',
        on_delete=fields.CASCADE,
        null=True
    )
    subject = fields.ForeignKeyField(
        'models.Subject',
        on_delete=fields.CASCADE,
        null=True
    )

    class Meta:
        abstract = True
        

class PeriodLesson(AbstractLesson):
    period = fields.SmallIntField(null=True)
    repeat_lessons_until_date = fields.DateField(null=True)
    start_date = fields.DateField(null=True)

    class Meta:
        table = "period_lesson"


class Lesson(AbstractLesson):
    date = fields.DateField()
    week_day = fields.IntField()
    is_canceled = fields.BooleanField(default=False)
    is_completed = fields.BooleanField(default=False)
    duration = TimeDurationField()
    comment = fields.CharField(max_length=200, null=True)

    class Meta:
        table = "lesson"
        ordering = ["date", "start_time"]

    def __str__(self):
        return f"{self.teacher} {self.title} {self.date}"

    async def clean(self):
        if self.start_time >= self.end_time:
            raise ValidationError('start_time cant be after end_time')

    def _set_week_day(self):
        if self.date:
            self.week_day = self.date.isoweekday()

    def _set_time_duration(self):
        if self.start_time and self.end_time:
            self.duration = time_diff(self.start_time, self.end_time)
