--Добавление ограничений в таблицы

--ограничение на год выпуска альбома
ALTER TABLE Album ADD CHECK (year_creat >= 2018);

--ограничение на год выпуска сборника
ALTER TABLE Collection ADD CHECK (year_creat >= 2019);

--ограничение на уникальность названия жанра
ALTER TABLE Genre ADD CONSTRAINT dif1 UNIQUE (name_g);

--ограничение на продолжение трека
ALTER TABLE Track ADD CHECK (duration between 3 AND  8);

-- Дата изменений 26.04.2023

