--ДЗ № 4
---------------------------------------------
-- 1 задание 
-- посчитаем, сколько исполнителей поют в каждом жанре
SELECT	 	g.name_g, 	   COUNT(performer_id) performer FROM genre g
    LEFT JOIN	genreperformer gp  ON g.id = gp.genre_id
    GROUP BY 	g.name_g
    ORDER BY 	performer; 
--добавлял вручную (в программе DBeaver)новый жанр, в котором нет исполнителей , cработало

-----------------------------------------------------------------------------------------------------
--2 задание 
--Количество треков, вошедших в альбомы 2019–2020 годов.

SELECT COUNT(t.id) количество_треков_в_2019_2020_г FROM track t/* Количество айди треков из таблицы треков */
   JOIN album a ON t.album_id  = a.id  /* Делаем объединение от таблицы треков к альбомам */
   WHERE a.year_creat BETWEEN 2019 and 2020; /* Где год альбома находится в требуемом промежутке */


------------------------------------------------------------------------------------------------------------------
--3 задание 
--Средняя продолжительность треков по каждому альбому.

SELECT name_a Название_альбома, AVG(t.duration) Средняя_продолжительность_трека FROM album a
	JOIN track t 				ON a.id = t.album_id 
	GROUP BY a.name_a;

------------------------------------------------------------------
--4 задание 
--Все исполнители, которые не выпустили альбомы в 2020 году.

SELECT performer.name_p, performer.id id_исполнителей_не_вып_альбомы_в_2020  /* Получаем имена исполнителей */
FROM performer  /* Из таблицы исполнителей */
WHERE performer.name_p NOT IN ( /* Где имя исполнителя не входит во вложенную выборку */
    SELECT performer.name_p  /* Получаем имена исполнителей */
    FROM performer /* Из таблицы исполнителей */
    JOIN performeralbum ON performer.id = performeralbum.performer_id /* Объединяем с промежуточной таблицей */
    JOIN album	        ON performeralbum.album_id = album.id /* Объединяем с таблицей альбомов */
    WHERE album.year_creat = 2020); /* Где год альбома равен 2020 */
);
-----------------------------------------------------------------------
--5 задание 
--Названия сборников, в которых присутствует конкретный исполнитель (выберите его сами) 
--Исполнитель Eva Austin (id = 7 ) 

SELECT c.name_c сборник, p.name_p исполн_присутствует_в_сборнике, p.id id_исполнителя FROM collection c
	JOIN 	collectiontrack ct 	ON c.id = ct.collection_id 
	JOIN 	track t 			ON ct.track_id = t.id
	JOIN 	performeralbum pa 	ON t.album_id = pa.album_id 
	JOIN 	performer p 		ON pa.performer_id = p.id 
	WHERE 	p.name_p = 'Eva Austin';

------------------------------------------------------------------------------------------------------	
--6 задание
--Названия альбомов, в которых присутствуют исполнители более чем одного жанра

SELECT 	a.name_a альбом FROM album a
    JOIN      performeralbum pa ON a.id  = pa.album_id 
    JOIN      performer p       ON pa.performer_id = p.id
    JOIN      genreperformer gp ON p.id  = gp.performer_id 
    JOIN      genre g 		ON gp.genre_id = g.id 
    GROUP BY  a.name_a, p.name_p
    HAVING    COUNT(gp.genre_id) > 1
    ORDER BY  a.name_a;

---------------------------------------------------------------------------------------------------	
--7 задание 
--Наименования треков, которые не входят в сборники.
 
SELECT 	name_t, t.id id_в_таблице_треков/*, ct.collection_id */FROM track t 
LEFT JOIN collectiontrack ct ON t.id = ct.track_id /* Делаем левый джойн с промежуточной таблицей между треками и сборниками */
WHERE ct.track_id  is NULL; /* Где id трека из промежуточной таблицы является NULL */

-------------------------------------------------
--8 задание 
--Исполнитель или исполнители, написавшие самый короткий по продолжительности трек,теоретически таких треков может быть несколько.

SELECT p.name_p 
FROM performer p
JOIN performeralbum pa  ON p.id = pa.performer_id
JOIN 	 album a 	    ON pa.album_id = a.id
JOIN 	 track t 	    ON a.id  = t.album_id
WHERE    t.duration = (
    SELECT MIN(t.duration) FROM track t
    JOIN performeralbum pa  ON t.album_id  = pa.album_id 
);

----------------------------------------------------------------------
--9 задание 
--Названия альбомов, содержащих наименьшее количество треков.

SELECT a.name_a альбом FROM album a /* Названия альбомов */
    JOIN     track t ON a.id = t.album_id /* Объединяем альбомы и треки */
    GROUP BY a.id /* Группируем по айди альбомов */
    HAVING   COUNT(t.id) =  /* Где количество треков равно вложенному запросу, */
    (
    	SELECT COUNT(track.id) FROM track /* Получаем поличество айди треков из таблицы треков*/
    	GROUP by track.album_id   --a.id /* Группируем по айди альбомов */
        ORDER BY 1 /* Сортируем по первому столбцу */
    	LIMIT 1 /* Получаем первую запись */
    );

