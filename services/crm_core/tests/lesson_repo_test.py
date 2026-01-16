import pytest
from tortoise import Tortoise
from tortoise.transactions import in_transaction
from datetime import date, time, timedelta
from app.models.lessons import Lesson



@pytest.mark.skip(reason="Пока не нужно прогонять этот тест")
async def test_create_lesson():

    async with in_transaction() as conn:
        lesson = Lesson(
            org_id=1,
            title="1",
            start_time=time(1, 0),
            end_time=time(2, 0),
            teacher_id=1,
            classroom_id=1,
            student_group_id=1,
            subject_id=1,
            date=date.today(),
            week_day=1,
            is_canceled=False,
            is_completed=False,
            duration=timedelta(hours=1),
            comment="1"
        )
        await lesson.save(using_db=conn) 

        lesson_in_db = await Lesson.get(id=lesson.id, using_db=conn)
        assert lesson_in_db.title == "1"

    await Tortoise.close_connections()
