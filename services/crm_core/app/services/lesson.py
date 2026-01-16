from app.models.lessons import Lesson, PeriodLesson
from app.services.base import BaseService
from app.repositories.tortoise import PeriodLessonRepository, LessonRepository
from datetime import date, timedelta, datetime 
from app.schemas.lesson import PeriodLessonCreate, PeriodLessonUpdate, PeriodLessonDelete
from tortoise.transactions import in_transaction



class PeriodLessonServise(BaseService):
    period_lesson_repo = PeriodLessonRepository
    lesson_repo = LessonRepository
    
    
    async def create(period_lesson: PeriodLessonCreate) -> PeriodLesson:
        lesson_repo: LessonRepository = LessonRepository(period_lesson.org_id)
        period_lesson_repo: PeriodLessonRepository = PeriodLessonRepository(period_lesson.org_id)
        current_date = period_lesson.start_date
        lessons = []
        while current_date <= period_lesson.repeat_lessons_until_date:
            lessons.append({
                "title": period_lesson.title,
                "start_time": period_lesson.start_time, 
                "end_time": period_lesson.end_time,
                "teacher_id": period_lesson.teacher_id,
                "classroom_id": period_lesson.classroom_id,
                "student_group_id": period_lesson.student_group_id,
                "subject_id": period_lesson.subject_id,
                "date": current_date,
                "week_day": current_date.weekday(),
                "duration": period_lesson.duration,
                "org_id": period_lesson.org_id
            })
            current_date += timedelta(days=period_lesson.period)
            
        await lesson_repo.bulk_create(lessons)
            
        period_lesson_data = {
                "title": period_lesson.title,
                "start_time": period_lesson.start_time,
                "end_time": period_lesson.end_time,
                "teacher_id": period_lesson.teacher_id,
                "classroom_id": period_lesson.classroom_id,
                "student_group_id": period_lesson.student_group_id,
                "subject_id": period_lesson.subject_id,
                "period": period_lesson.period,
                "repeat_lessons_until_date": period_lesson.repeat_lessons_until_date,
                "start_date": period_lesson.start_date,
                "org_id": period_lesson.org_id
        }        
        created_period_lesson = await period_lesson_repo.create(**period_lesson_data)
        return created_period_lesson
    
    
    async def update(period_lesson: PeriodLessonCreate):
        lesson_repo = LessonRepository(period_lesson.org_id)
        period_lesson_repo = PeriodLessonRepository(period_lesson.org_id)

        period_lesson_obj = await period_lesson_repo.get(id=period_lesson.id)

        updated_period_lesson = await period_lesson_repo.update(
            period_lesson_obj,
            **period_lesson.dict(exclude_unset=True)
        )

        lessons = await Lesson.filter(period_lesson_id=updated_period_lesson.id)

        lessons_data = [
            {**lesson.dict(exclude_unset=True), "id": lesson.id}
            for lesson in lessons
        ]

        updated_lessons = await lesson_repo.bulk_update(lessons_data)

        await updated_period_lesson.fetch_related("lessons")

        return {
            "period_lesson": updated_period_lesson,
            "lessons": updated_lessons
        }

    async def delete(period_lesson: PeriodLessonDelete):
        lesson_repo = LessonRepository(period_lesson.org_id)
        period_lesson_repo = PeriodLessonRepository(period_lesson.org_id)
        
        await period_lesson_repo.delete(period_lesson.id)
        
        await lesson_repo.bulk_delete(period_lesson.id)
