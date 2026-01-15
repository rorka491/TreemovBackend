import pytest
from tortoise import Tortoise
from tortoise.transactions import in_transaction
from datetime import date, time, timedelta
from app.models.lessons import Lesson
from app.core.db import TORTOISE_ORM

@pytest.mark.asyncio
async def test_create_lesson():
    # инициализация ORM
    await Tortoise.init(config=TORTOISE_ORM)
    await Tortoise.generate_schemas()

    # создаём транзакцию
    async with in_transaction() as conn:
        # создаём запись через транзакцию
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
        await lesson.save(using_db=conn)  # обязательно через транзакцию

        # проверка внутри транзакции
        lesson_in_db = await Lesson.get(id=lesson.id, using_db=conn)
        assert lesson_in_db.title == "1"

    # После выхода из блока in_transaction() изменения откатываются
    # в реальной базе запись не сохраняется

    await Tortoise.close_connections()
