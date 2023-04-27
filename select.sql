--Создание запросов для базы данных

--Название и год выхода альбомов, вышедших в 2018 году.
SELECT name_a, year_creat FROM album
WHERE year_creat <= 2018; --в таблице нет альбомов, вышедших раньше 2018 года ( ALTER TABLE Album ADD CHECK (year_creat >= 2018);)

--Название и продолжительность самого длительного трека.
--Эта информация будет вверху таблицы
SELECT name_t, duration FROM track
ORDER BY duration DESC;

--Название треков, продолжительность которых не менее 3,5 минут.
SELECT name_t, duration FROM track
WHERE duration >= 3.5;

--Названия сборников, вышедших в период с 2018 по 2020 год включительно.
SELECT name_c , year_creat FROM collection 
WHERE year_creat >= 2018 and year_creat <= 2020;

--Исполнители, чьё имя состоит из одного слова.
SELECT name_p , name_p FROM performer
WHERE name_p not like '% %';

--Название треков, которые содержат слово «мой» или «my».
SELECT name_t , name_t FROM track
WHERE name_t  like '%my%';
