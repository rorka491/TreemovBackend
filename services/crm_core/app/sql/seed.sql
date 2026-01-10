BEGIN;

INSERT INTO roles (code, title)
VALUES
    ('administrator', 'Администратор'),
    ('student', 'Студент'),
    ('teacher', 'Учитель')
ON CONFLICT (code) DO NOTHING;



INSERT INTO permissions (code, name)
VALUES
    ('create.lesson','Создание события'),
    ('create.period_lesson','Создание периодического занятия'),
    ('create.subject','Создание предмета'),
    ('create.profile','Создание профиля'),
    ('create.classrom','Создание аудитории'),
    ('create.techer','Создание учителя'),
    ('create.student','Создание студента'),
    ('create.accrual','Начисление баллов'),
    ('create.attendances','Создание посещения занятий'),
    ('create.student_group','Создание группы'),
    ('create.student_group_member','Добавление участника в группу'),
    ('create.organization.member','Добавление члена организации'),
    ('create.role_profile','Создание роли профиля'),

    ('read.lesson','Чтение событий'),
    ('read.periode_lesson','Чтение периодических занятий'),
    ('read.subject','Чтение предметов'),
    ('read.organization','Чтение организаций'),
    ('read.profile','Чтение профиля'),
    ('read.audience','Чтение аудиторий'),
    ('read.teacher','Чтение учителей'),
    ('read.student','Чтение студентов'),
    ('read.accrual','Чтение начислений баллов'),
    ('read.attendances','Чтение посещений занятий'),
    ('read.student_group','Чтение групп'),
    ('read.student_group_member','Чтение участников группы'),
    ('read.organization_mebmer','Чтение участников организации')
ON CONFLICT (code) DO NOTHING;


INSERT INTO role_permissions (role_id, permission_id)
SELECT
    r.id,
    p.id
FROM roles r
CROSS JOIN permissions p
WHERE r.code = 'administrator'
ON CONFLICT DO NOTHING;

COMMIT;
