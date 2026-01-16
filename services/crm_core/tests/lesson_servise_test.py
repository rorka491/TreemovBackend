from itertools import count
import pytest
from tortoise.transactions import in_transaction
from datetime import date, time, timedelta, timezone
from app.models.lessons import Lesson, PeriodLesson
from app.services.lesson import PeriodLessonServise
from app.schemas.lesson import PeriodLessonCreate, PeriodLessonUpdate, PeriodLessonDelete

@pytest.mark.asyncio
async def test_period_lesson_creation_success():
    lesson = PeriodLessonCreate(
        title="Test Lesson",
        start_time=time(10, 0, tzinfo=timezone.utc),
        end_time=time(11, 0, tzinfo=timezone.utc),
        teacher_id=1,
        classroom_id=1,
        student_group_id=1,
        subject_id=1,
        period=7,
        repeat_lessons_until_date=date(2026, 1, 31),
        start_date=date(2025, 12, 29),
        duration=60,
        org_id=1
    )
    
    created = await PeriodLessonServise.create(lesson)
    count = await Lesson.all().count()
    assert count == 5 
    period_lesson = await PeriodLesson.get(id=created.id)
    assert period_lesson.title == "Test Lesson"
    
    lessons = await Lesson.filter(period_lesson_id=created.id)
    for lesson in lessons:
        assert lesson.period_lesson_id == created_period_lesson.id
        assert lesson.id is not None

@pytest.mark.asyncio
async def test_period_lesson_creation_collision_date():
    lesson1 = PeriodLessonCreate(
        title="Test Lesson",
        start_time=time(10, 0, tzinfo=timezone.utc),
        end_time=time(11, 0, tzinfo=timezone.utc),
        teacher_id=1,
        classroom_id=1,
        student_group_id=1,
        subject_id=1,
        period=7,
        repeat_lessons_until_date=date(2026, 1, 31),
        start_date=date(2025, 12, 29),
        duration=60,
        org_id=1
    )

    lesson2 = PeriodLessonCreate(
        title="Test Lesson",
        start_time=time(10, 0, tzinfo=timezone.utc),
        end_time=time(11, 0, tzinfo=timezone.utc),
        teacher_id=1,
        classroom_id=2,
        student_group_id=2,
        subject_id=1,
        period=7,
        repeat_lessons_until_date=date(2026, 1, 31),
        start_date=date(2025, 12, 29),
        duration=60,
        org_id=1
    )

    await PeriodLessonServise.create(lesson1)

    with pytest.raises(ValueError):
        await PeriodLessonServise.create(lesson2)


@pytest.mark.asyncio
async def test_period_lesson_creation_collision_teacher():
    lesson1 = PeriodLessonCreate(
        title="Test Lesson",
        start_time=time(10, 0, tzinfo=timezone.utc),
        end_time=time(11, 0, tzinfo=timezone.utc),
        teacher_id=1,
        classroom_id=1,
        student_group_id=1,
        subject_id=1,
        period=7,
        repeat_lessons_until_date=date(2026, 1, 31),
        start_date=date(2025, 12, 29),
        duration=60,
        org_id=1
    )

    lesson2 = PeriodLessonCreate(
        title="Test Lesson",
        start_time=time(10, 0, tzinfo=timezone.utc),
        end_time=time(11, 0, tzinfo=timezone.utc),
        teacher_id=1,
        classroom_id=2,
        student_group_id=2,
        subject_id=1,
        period=7,
        repeat_lessons_until_date=date(2026, 1, 31),
        start_date=date(2025, 12, 29),
        duration=60,
        org_id=1
    )

    await PeriodLessonServise.create(lesson1)

    with pytest.raises(ValueError):
        await PeriodLessonServise.create(lesson2)
        
        
@pytest.mark.asyncio
async def test_period_lesson_creation_collision_student_group():
    lesson1 = PeriodLessonCreate(
        title="Test Lesson",
        start_time=time(10, 0, tzinfo=timezone.utc),
        end_time=time(11, 0, tzinfo=timezone.utc),
        teacher_id=1,
        classroom_id=1,
        student_group_id=1,
        subject_id=1,
        period=7,
        repeat_lessons_until_date=date(2026, 1, 31),
        start_date=date(2025, 12, 29),
        duration=60,
        org_id=1
    )

    lesson2 = PeriodLessonCreate(
        title="Test Lesson",
        start_time=time(10, 0, tzinfo=timezone.utc),
        end_time=time(11, 0, tzinfo=timezone.utc),
        teacher_id=2,
        classroom_id=2,
        student_group_id=1,
        subject_id=1,
        period=7,
        repeat_lessons_until_date=date(2026, 1, 31),
        start_date=date(2025, 12, 29),
        duration=60,
        org_id=1
    )

    await PeriodLessonServise.create(lesson1)

    with pytest.raises(ValueError):
        await PeriodLessonServise.create(lesson2)
        
@pytest.mark.asyncio
async def test_period_lesson_creation_collision_classroom():
    lesson1 = PeriodLessonCreate(
        title="Test Lesson",
        start_time=time(10, 0, tzinfo=timezone.utc),
        end_time=time(11, 0, tzinfo=timezone.utc),
        teacher_id=1,
        classroom_id=1,
        student_group_id=1,
        subject_id=1,
        period=7,
        repeat_lessons_until_date=date(2026, 1, 31),
        start_date=date(2025, 12, 29),
        duration=60,
        org_id=1
    )

    lesson2 = PeriodLessonCreate(
        title="Test Lesson",
        start_time=time(10, 0, tzinfo=timezone.utc),
        end_time=time(11, 0, tzinfo=timezone.utc),
        teacher_id=2,
        classroom_id=1,
        student_group_id=2,
        subject_id=1,
        period=7,
        repeat_lessons_until_date=date(2026, 1, 31),
        start_date=date(2025, 12, 29),
        duration=60,
        org_id=1
    )

    await PeriodLessonServise.create(lesson1)

    with pytest.raises(ValueError):
        await PeriodLessonServise.create(lesson2)
        
        
@pytest.mark.asyncio
async def test_period_lesson_update():
    lesson_create = PeriodLessonCreate(
        title="Test Lesson",
        start_time=time(10, 0, tzinfo=timezone.utc),
        end_time=time(11, 0, tzinfo=timezone.utc),
        teacher_id=1,
        classroom_id=1,
        student_group_id=1,
        subject_id=1,
        period=7,
        repeat_lessons_until_date=date(2026, 1, 31),
        start_date=date(2025, 12, 29),
        duration=60,
        org_id=1
    )
    created_period_lesson = await PeriodLessonServise.create(lesson_create)

    lesson_update = PeriodLessonUpdate(
        id=created_period_lesson.id,
        title="Updated Lesson Title",
        start_time=time(10, 0, tzinfo=timezone.utc),
        end_time=time(11, 0, tzinfo=timezone.utc),
        teacher_id=1,
        classroom_id=1,
        student_group_id=1,
        subject_id=1,
        period=7,
        repeat_lessons_until_date=date(2026, 1, 31),
        start_date=date(2025, 12, 29),
        duration=60,
        org_id=1
    )
    updated_result = await PeriodLessonServise.update(lesson_update)

    await updated_result["period_lesson"].fetch_related("lessons")

    assert updated_result["period_lesson"].title == "Updated Lesson Title"

    for lesson in updated_result["period_lesson"].lessons:
        assert lesson.period_lesson_id == updated_result["period_lesson"].id
        assert lesson.id is not None
        assert lesson.title is not None
        
        

@pytest.mark.asyncio
async def test_period_lesson_update_collision_teacher():
    lesson_create = PeriodLessonCreate(
        title="Test Lesson",
        start_time=time(10, 0, tzinfo=timezone.utc),
        end_time=time(11, 0, tzinfo=timezone.utc),
        teacher_id=1,
        classroom_id=1,
        student_group_id=1,
        subject_id=1,
        period=7,
        repeat_lessons_until_date=date(2026, 1, 31),
        start_date=date(2025, 12, 29),
        duration=60,
        org_id=1
    )
    lesson_create_collision = PeriodLessonCreate(
        title="Test Lesson",
        start_time=time(10, 0, tzinfo=timezone.utc),
        end_time=time(11, 0, tzinfo=timezone.utc),
        teacher_id=2,
        classroom_id=1,
        student_group_id=1,
        subject_id=1,
        period=7,
        repeat_lessons_until_date=date(2026, 1, 31),
        start_date=date(2025, 12, 29),
        duration=60,
        org_id=1
    )
    created_period_lesson = await PeriodLessonServise.create(lesson_create)
    with pytest.raises(ValueError):
        created_period_lesson = await PeriodLessonServise.create(lesson_create_collision)
    lesson_update = PeriodLessonUpdate(
        id=created_period_lesson.id,
        title="Updated Lesson Title",
        start_time=time(10, 0, tzinfo=timezone.utc),
        end_time=time(11, 0, tzinfo=timezone.utc),
        teacher_id=2,
        classroom_id=1,
        student_group_id=1,
        subject_id=1,
        period=7,
        repeat_lessons_until_date=date(2026, 1, 31),
        start_date=date(2025, 12, 29),
        duration=60,
        org_id=1
    )
    updated_result = await PeriodLessonServise.update(lesson_update)

    await updated_result["period_lesson"].fetch_related("lessons")

    assert updated_result["period_lesson"].title == "Updated Lesson Title"

    for lesson in updated_result["period_lesson"].lessons:
        assert lesson.period_lesson_id == updated_result["period_lesson"].id
        assert lesson.id is not None
        assert lesson.title is not None

@pytest.mark.asyncio
async def test_period_lesson_update_collision_classroom():
    lesson_create = PeriodLessonCreate(
        title="Test Lesson",
        start_time=time(10, 0, tzinfo=timezone.utc),
        end_time=time(11, 0, tzinfo=timezone.utc),
        teacher_id=1,
        classroom_id=1,
        student_group_id=1,
        subject_id=1,
        period=7,
        repeat_lessons_until_date=date(2026, 1, 31),
        start_date=date(2025, 12, 29),
        duration=60,
        org_id=1
    )
    lesson_create_collision = PeriodLessonCreate(
        title="Test Lesson",
        start_time=time(10, 0, tzinfo=timezone.utc),
        end_time=time(11, 0, tzinfo=timezone.utc),
        teacher_id=1,
        classroom_id=2,
        student_group_id=1,
        subject_id=1,
        period=7,
        repeat_lessons_until_date=date(2026, 1, 31),
        start_date=date(2025, 12, 29),
        duration=60,
        org_id=1
    )
    created_period_lesson = await PeriodLessonServise.create(lesson_create)
    with pytest.raises(ValueError):
        created_period_lesson = await PeriodLessonServise.create(lesson_create_collision)
    lesson_update = PeriodLessonUpdate(
        id=created_period_lesson.id,
        title="Updated Lesson Title",
        start_time=time(10, 0, tzinfo=timezone.utc),
        end_time=time(11, 0, tzinfo=timezone.utc),
        teacher_id=1,
        classroom_id=1,
        student_group_id=1,
        subject_id=1,
        period=7,
        repeat_lessons_until_date=date(2026, 1, 31),
        start_date=date(2025, 12, 29),
        duration=60,
        org_id=1
    )
    updated_result = await PeriodLessonServise.update(lesson_update)

    await updated_result["period_lesson"].fetch_related("lessons")

    assert updated_result["period_lesson"].title == "Updated Lesson Title"

    for lesson in updated_result["period_lesson"].lessons:
        assert lesson.period_lesson_id == updated_result["period_lesson"].id
        assert lesson.id is not None
        assert lesson.title is not None
        


@pytest.mark.asyncio
async def test_period_lesson_update_collision_student_group():
    lesson_create = PeriodLessonCreate(
        title="Test Lesson",
        start_time=time(10, 0, tzinfo=timezone.utc),
        end_time=time(11, 0, tzinfo=timezone.utc),
        teacher_id=1,
        classroom_id=1,
        student_group_id=1,
        subject_id=1,
        period=7,
        repeat_lessons_until_date=date(2026, 1, 31),
        start_date=date(2025, 12, 29),
        duration=60,
        org_id=1
    )
    lesson_create_collision = PeriodLessonCreate(
        title="Test Lesson",
        start_time=time(10, 0, tzinfo=timezone.utc),
        end_time=time(11, 0, tzinfo=timezone.utc),
        teacher_id=1,
        classroom_id=1,
        student_group_id=2,
        subject_id=1,
        period=7,
        repeat_lessons_until_date=date(2026, 1, 31),
        start_date=date(2025, 12, 29),
        duration=60,
        org_id=1
    )
    created_period_lesson = await PeriodLessonServise.create(lesson_create)
    with pytest.raises(ValueError):
        created_period_lesson = await PeriodLessonServise.create(lesson_create_collision)
    lesson_update = PeriodLessonUpdate(
        id=created_period_lesson.id,
        title="Updated Lesson Title",
        start_time=time(10, 0, tzinfo=timezone.utc),
        end_time=time(11, 0, tzinfo=timezone.utc),
        teacher_id=1,
        classroom_id=1,
        student_group_id=2,
        subject_id=1,
        period=7,
        repeat_lessons_until_date=date(2026, 1, 31),
        start_date=date(2025, 12, 29),
        duration=60,
        org_id=1
    )
    updated_result = await PeriodLessonServise.update(lesson_update)

    await updated_result["period_lesson"].fetch_related("lessons")

    assert updated_result["period_lesson"].title == "Updated Lesson Title"

    for lesson in updated_result["period_lesson"].lessons:
        assert lesson.period_lesson_id == updated_result["period_lesson"].id
        assert lesson.id is not None
        assert lesson.title is not None
        
        
@pytest.mark.asyncio
async def test_period_lesson_delete():
    lesson = PeriodLessonCreate(
        title="Test Lesson",
        start_time=time(10, 0, tzinfo=timezone.utc),
        end_time=time(11, 0, tzinfo=timezone.utc),
        teacher_id=1,
        classroom_id=1,
        student_group_id=1,
        subject_id=1,
        period=7,
        repeat_lessons_until_date=date(2026, 1, 31),
        start_date=date(2025, 12, 29),
        duration=60,
        org_id=1
    )
    
    created = await PeriodLessonServise.create(lesson)
    count = await Lesson.all().count()
    assert count == 5 

    period_lesson_delete = PeriodLessonDelete(
        id=created.id,
        org_id=created.org_id
    )

    await PeriodLessonServise.delete(period_lesson_delete)

    period_lessons = await PeriodLesson.filter(id=created.id)
    assert len(period_lessons) == 0

    remaining_lessons = await Lesson.filter(period_lesson_id=created.id)



