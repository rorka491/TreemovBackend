BEGIN;

INSERT INTO roles(code, title) VALUES
('administrator', 'Администратор'),
('student', 'Студент'),
('teacher', 'Учитель');


INSERT INTO permissions(code, name) VALUES
--Создание объектов--
('create.event','Создание события'),
('create.periodlesson','Создание переодического занятия'),
('create.subject','Создание предмета'),
('create.profile','Создание профиля'),
('create.audience','Создание аудитории'),
('create.techer','Создание учителя'),
('create.student','Создание студента'),
('create.accrual','Начиление баллов'),
('create.attendances','Создание посещения занятий'),
('create.group','Создание группы'),
('create.group_member','Добовление участника в группу'),
('create.organization.member','Добавление члена огранизации'),
('create.role_profile','Создание роли профиля'),
('create.grades','Создание оценки'),
--Обновление объектов--
('update.event','Обновление события'),
('update.periodlesson','Обновление переодического занятия'),
('update.subject','Обновление предмета'),
('update.profile','Обновление профиля'),
('update.audience','Обновление аудитории'),
('update.techer','Обновление учителя'),
('update.student','Обновление студента'),
('update.accrual','Обновление баллов'),
('update.attendances','Обновление посещения занятий'),
('update.group','Обновление группы'),
('update.group_member','Обновление участника в группу'),
('update.organization.member','Обновление члена огранизации'),
('update.role_profile','Обновление роли профиля'),
('update.grades','Обновление оценки'),
--Удаление объектов--
('delete.event','Удаление события'),
('delete.periodlesson','Удаление переодического занятия'),
('delete.subject','Удаление предмета'),
('delete.profile','Удаление профиля'),
('delete.audience','Удаление аудитории'),
('delete.techer','Удаление учителя'),
('delete.student','Удаление студента'),
('delete.accrual','Удаление баллов'),
('delete.attendances','Удаление посещения занятий'),
('delete.group','Удаление группы'),
('delete.group_member','Удаление участника в группу'),
('delete.organization.member','Удаление члена огранизации'),
('delete.role_profile','Удаление роли профиля'),
('delete.grades','Удаление оценки'),
--Чтение всех объектов--
('read.event.all','Чтение всех событий'),
('read.periodic_lesson.all','Чтение всех переоридеских занятий'),
('read.subject.all','Чтение всех предметов'),
('read.organization.all','Чтений всех организаций'),
('read.profile.all','Чтений всех профиля'),
('read.audience.all','Чтений всех аудиторий'),
('read.teacher.all','Чтений всех учителей'),
('read.student.all','Чтений всех студентов'),
('read.accrual.all','Чтение всех начислений баллов'),
('read.attendances.all','Чтение всех посещений занятий'),
('read.group.all','Чтение всех групп'),
('read.group_member.all','Чтение всех участников группы'),
('read.organization_mebmer.all','Чтений всех участников группы'),
('read.grade.all','Чтение всех оценок'),
--Чтение своих объектов--
('read.event.self', 'Чтение своих событий'),
('read.organization.self','Чтений своей организации'),
('read.profile.self','Чтений своего профиля'),
('read.student.self','Чтений своих студентов'),
('read.accrual.self','Чтение своих начислений баллов'),
('read.attendances.self','Чтение своих посещений занятий'),
('read.grade.self','Чтение своих оценок'),
('read.periodic_lesson.self','Чтение своих переоридеских занятий'),
('read.audience.self','Чтений своих аудиторий'),
('read.teacher.self','Чтений своих учителей'),
('read.group.self','Чтение своих групп'),
('read.group_member.self','Чтение своих участников группы'),
('read.organization_mebmer.self','Чтений своих участников группы'),
--Создание своих объектов--
('create.event.self','Создание своих событий'),
('update.event.self','Обновление своих событий'),
('delete.event.self','Удаление своих событий'),
('create.periodlesson.self','Создание своих переодических занятий'),
('update.periodlesson.self','Обновление своих переодических занятий'),
('delete.periodlesson.self','Удаление своих переодических занятий'),
('create.accrual.self','Начиление баллов'),
('update.accrual.self','Обновление начилений баллов'),
('delete.accrual.self','Удаление начилений баллов'),
('create.attendances.self','Создание своих посещений занятий'),
('update.attendances.self','Обновление своих посещений занятий'),
('delete.attendances.self','Удаление своих посещений занятий'),
('create.group_member.self','Добовление своих участников в группу'),
('update.group_member.self','Обновление своих участников в группу'),
('delete.group_member.self','Удаление своих участников в группу'),
('create.grades.self','Создание оценки'),
('update.grades.self','Обновление оценки'),
('delete.grades.self','Удаление оценки');


--Добавление ролей для администратора--
INSERT INTO rolepermission(permission_id, role_id) VALUES
(1,1),
(2,1),
(3,1),
(4,1),
(5,1),
(6,1),
(7,1),
(8,1),
(9,1),
(10,1),
(11,1),
(12,1),
(13,1),
(14,1),
(15,1),
(16,1),
(17,1),
(18,1),
(19,1),
(20,1),
(21,1),
(22,1),
(23,1),
(24,1),
(25,1),
(26,1),
(27,1),
(28,1),
(29,1),
(30,1),
(31,1),
(32,1),
(33,1),
(34,1),
(35,1),
(36,1),
(37,1),
(38,1),
(39,1),
(40,1),
(41,1),
(42,1),
(43,1),
(44,1),
(45,1),
(46,1),
(47,1),
(48,1),
(49,1),
(50,1),
(51,1),
(52,1),
(53,1),
(54,1),
(55,1),
(56,1);


--Добавление прав для студента--
INSERT INTO rolepermission(permission_id, role_id) VALUES
((SELECT id FROM permissions WHERE code = 'read.event.self' ), 2),
((SELECT id FROM permissions WHERE code = 'read.organization.self' ), 2),
((SELECT id FROM permissions WHERE code = 'read.profile.self' ), 2),
((SELECT id FROM permissions WHERE code = 'read.student.self' ), 2),
((SELECT id FROM permissions WHERE code = 'read.accrual.self' ), 2),
((SELECT id FROM permissions WHERE code = 'read.attendances.self' ), 2),
((SELECT id FROM permissions WHERE code = 'read.grade.self' ), 2);


--Добавление прав для учителя--
INSERT INTO rolepermission(permission_id, role_id) VALUES
((SELECT id FROM permissions WHERE code = 'read.event.self' ), 3),
((SELECT id FROM permissions WHERE code = 'read.periodic_lesson.self' ), 3),
((SELECT id FROM permissions WHERE code = 'read.organization.self' ), 3),
((SELECT id FROM permissions WHERE code = 'read.profile.self' ), 3),
((SELECT id FROM permissions WHERE code = 'read.audience.self' ), 3),
((SELECT id FROM permissions WHERE code = 'read.teacher.self' ), 3),
((SELECT id FROM permissions WHERE code = 'read.student.self' ), 3),
((SELECT id FROM permissions WHERE code = 'read.accrual.self' ), 3),
((SELECT id FROM permissions WHERE code = 'read.attendances.self' ), 3),
((SELECT id FROM permissions WHERE code = 'read.grade.self' ), 3),
((SELECT id FROM permissions WHERE code = 'read.group.self' ), 3),
((SELECT id FROM permissions WHERE code = 'read.group_member.self' ), 3),
((SELECT id FROM permissions WHERE code = 'read.organization_mebmer.self' ), 3),
((SELECT id FROM permissions WHERE code = 'create.event.self' ), 3),
((SELECT id FROM permissions WHERE code = 'update.event.self' ), 3),
((SELECT id FROM permissions WHERE code = 'delete.event.self' ), 3),
((SELECT id FROM permissions WHERE code = 'create.periodlesson.self' ), 3),
((SELECT id FROM permissions WHERE code = 'update.periodlesson.self' ), 3),
((SELECT id FROM permissions WHERE code = 'delete.periodlesson.self' ), 3),
((SELECT id FROM permissions WHERE code = 'create.accrual.self' ), 3),
((SELECT id FROM permissions WHERE code = 'update.accrual.self' ), 3),
((SELECT id FROM permissions WHERE code = 'delete.accrual.self' ), 3),
((SELECT id FROM permissions WHERE code = 'create.attendances.self' ), 3),
((SELECT id FROM permissions WHERE code = 'update.attendances.self' ), 3),
((SELECT id FROM permissions WHERE code = 'delete.attendances.self' ), 3),
((SELECT id FROM permissions WHERE code = 'create.group_member.self' ), 3),
((SELECT id FROM permissions WHERE code = 'update.group_member.self' ), 3),
((SELECT id FROM permissions WHERE code = 'delete.group_member.self' ), 3),
((SELECT id FROM permissions WHERE code = 'create.grades.self' ), 3),
((SELECT id FROM permissions WHERE code = 'update.grades.self' ), 3),
((SELECT id FROM permissions WHERE code = 'delete.grades.self' ), 3);



<<<<<<< HEAD
COMMIT;
=======
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
>>>>>>> e0247679c087cdcd028440948d8d2e77ab38ad25
