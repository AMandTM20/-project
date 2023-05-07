ДЗ № 4
---------------------------------------------
-- 1 задание 

-- посчитаем, сколько исполнителей поют в каждом жанре
SELECT	 	g.name_g, 	   COUNT(performer_id) performer FROM genre g
    JOIN	genreperformer gp  ON g.id = gp.genre_id
    GROUP BY 	g.name_g 
    ORDER BY 	performer;

-----------------------------------------------------------------------------------------------------
--2 задание 

--Количество треков, вошедших в альбомы 2019–2020 годов.
SELECT name_a 	 AS Название_альбома, a.year_creat AS год_выпуска, COUNT(name_t) AS количество_треков FROM album a
    JOIN track t        ON a.id = t.album_id 
    WHERE a.year_creat 	BETWEEN 2019 AND 2020
    GROUP BY a.name_a, a.year_creat;
------------------------------------------------------------------------------------------------------------------
--3 задание 

--Средняя продолжительность треков по каждому альбому.
SELECT name_a Название_альбома, AVG(t.duration) Средняя_продолжительность_трека FROM album a
    JOIN track t    ON a.id = t.album_id 
    GROUP BY a.name_a;

------------------------------------------------------------------
--4 задание 
--Все исполнители, которые не выпустили альбомы в 2020 году.
--Здесь все исполнители,которые выпустили альбомы в 2020 году

SELECT p.name_p, p.id  исполнители_вып_альбомы_в_2020_г FROM performer p
    JOIN performeralbum pa  ON p.id = pa.performer_id
    JOIN album a 	    ON pa.album_id = a.id 
    WHERE 	a.year_creat = 2020
    GROUP BY 	p.id, p.name_p
    ORDER BY 	p.id;

--Все исполнители,которые не выпустили альбомы в 2020 году

SELECT performer.name_p, performer_id исполнители_не_вып_альбомы_в_2020_г FROM performer
    JOIN performeralbum     ON performer.id = performeralbum.performer_id
    JOIN album  	    ON performeralbum.album_id = album.id  
    WHERE performer.name_p  NOT IN (select performer.name_p FROM performer
			    JOIN performeralbum ON performer.id = performeralbum.performer_id
			    JOIN album	        ON performeralbum.album_id = album.id  
			    WHERE album.year_creat = 2020)
    GROUP BY 	performer.name_p, performer_id
    ORDER BY 	performer_id;
 	  
-----------------------------------------------------------------------
--5 задание 
--Названия сборников, в которых присутствует конкретный исполнитель (выберите его сами) 
--Исполнитель Eva Austin (id = 7 ) 

SELECT c.name_c сборник, p.name_p исполнитель, p.id id_исполнителя FROM collection c
    JOIN 	collectiontrack ct 	ON c.id = ct.collection_id 
    JOIN 	track t 		ON ct.track_id = t.id
    JOIN 	performeralbum pa 	ON t.album_id = pa.album_id 
    JOIN 	performer p 		ON pa.performer_id = p.id 
    WHERE 	p.name_p = 'Eva Austin';

------------------------------------------------------------------------------------------------------	
--6 задание	
--Названия альбомов, в которых присутствуют исполнители более чем одного жанра
	
SELECT a.name_a альбом, p.name_p исполнитель, COUNT(gp.genre_id) кол_жанров_исполнителя FROM album a
    JOIN      performeralbum pa ON a.id  = pa.album_id 
    JOIN      performer p       ON pa.performer_id = p.id
    JOIN      genreperformer gp ON p.id  = gp.performer_id 
    JOIN      genre g 		ON gp.genre_id = g.id 
    GROUP BY  p.name_p, a.name_a, p.name_p 
    HAVING    COUNT(gp.genre_id)  > 1
    ORDER BY  a.name_a, p.name_p ;
	 
---------------------------------------------------------------------------------------------------	
--7 задание 
--Наименования треков, которые не входят в сборники.
--треки, не входящие в сборники, находятся вверху таблицы

SELECT 	name_t, t.id id_в_таблице_треков, ct.collection_id FROM collectiontrack ct
    RIGHT JOIN  track t ON ct.track_id = t.id 
    ORDER BY 	collection_id DESC;

----------------------------------------------------------
--8 задание 
--Исполнитель или исполнители, написавшие самый короткий по продолжительности трек,теоретически таких треков может быть несколько.

-- с ошибкой (непонятной)-не понятно, почему в результатирующей таблице оказался не только самый короткий трек(3 минуты), но и трек продолжительностью 4 минуты.

SELECT p.name_p, MIN(t.duration) min_track FROM performer p 
    JOIN	 performeralbum pa  ON p.id = pa.performer_id 
    JOIN 	 album a 	    ON pa.album_id = a.id 
    JOIN 	 track t 	    ON a.id  = t.album_id  
    GROUP BY p.name_p 
    ORDER BY MIN(t.duration);

----------------------------------------------------------------------
--9 задание
--Названия альбомов, содержащих наименьшее количество треков.

SELECT a.name_a альбом, COUNT(t.id) кол_во_треков FROM album a 
    JOIN     track t ON a.id = t.album_id 
    GROUP BY name_a
    HAVING   COUNT(t.id) = 2--?Здесь сомнения
    ORDER BY COUNT(t.id);

------------------------------------------------------------------------------------------	
