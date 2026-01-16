from pydantic import Field
from app.schemas.base import BaseModelCreate, BaseModelRead
from datetime import time, date


class PeriodLessonCreate(BaseModelCreate):
    title: str
    start_time: time
    end_time: time
    teacher_id: int
    classroom_id: int
    student_group_id: int
    subject_id: int
    period: int
    repeat_lessons_until_date: date
    start_date: date
    duration: int
    org_id: int
    

class PeriodLessonUpdate(BaseModelCreate):
    id: int
    title: str
    start_time: time
    end_time: time
    teacher_id: int
    classroom_id: int
    student_group_id: int
    subject_id: int
    period: int
    repeat_lessons_until_date: date
    start_date: date
    duration: int
    org_id: int
    
class PeriodLessonDelete(BaseModelCreate):
    id: int
    org_id: int