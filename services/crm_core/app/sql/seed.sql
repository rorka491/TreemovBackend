BEGIN;

INSERT INTO roles(code, title) VALUES
('administrator', 'Администратор'),
('student', 'Студент'),
('teacher', 'Учитель');


INSERT INTO permissions(code, name) VALUES
('create.event','Создание события'),
('create.periodlesson','Создание переодического занятия'),
('create.subject','Создание события'),
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
('read.event','Чтение событий'),
('read.periodic_lesson','Чтение переоридеских занятий'),
('read.subject','Чтение событий'),
('read.organization','Чтений организаций'),
('read.profile','Чтений профиля'),
('read.audience','Чтений аудиторий'),
('read.teacher','Чтений учителей'),
('read.student','Чтений студентов'),
('read.accrual','Чтение начислений баллов'),
('read.attendances','Чтение посещений занятий'),
('read.group','Чтение групп'),
('read.group_member','Чтение участников группы'),
('read.organization_mebmer','Чтений участников группы');


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
(26,1);

COMMIT;