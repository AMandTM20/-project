-- Заполнение таблицы genre
insert into genre(name_g)
VALUES('blues');

insert into genre(name_g)
VALUES('jazz');

insert into genre(name_g)
VALUES('сountry');

insert into genre(name_g)
VALUES('chanson');

insert into genre(name_g)
VALUES('rock');


--Заполнение таблицы performer
insert into performer(name_p)
VALUES('Nancy');

insert into performer(name_p)
VALUES('Barbara Dyson');

insert into performer(name_p)
VALUES('Joan Backer');

insert into performer(name_p)
VALUES('Jack Tracey');

insert into performer(name_p)
VALUES('Harry Milton');

insert into performer(name_p)
VALUES('Charles Kelly');

insert into performer(name_p)
VALUES('Eva Austin');

insert into performer(name_p)
VALUES('Simon Pass');

delete from performer 
where id = 1;

insert into performer(id,name)
VALUES(1,'Nancy');



--Заполнение таблицы track

insert into track(name_t,duration,album_id)
VALUES('my foal',7,1);

insert into track(name_t,duration,album_id)
VALUES('blooming',6,6);

insert into track(name_t,duration,album_id)
VALUES('invasion',4,3);

insert into track(name_t,duration,album_id)
VALUES('graffiti',5,1);

insert into track(name_t,duration,album_id)
VALUES('this mist',2,2);

insert into track(name_t,duration,album_id)
VALUES('always',8,4);

insert into track(name_t,duration,album_id)
VALUES('my friend',6,5);

insert into track(name_t,duration,album_id)
VALUES('waiting',7,4);

insert into track(name_t,duration,album_id)
VALUES('fair',4,4);

insert into track(name_t,duration,album_id)
VALUES('only so',9,1);

insert into track(name_t,duration,album_id)
VALUES('evil silence',5,2);

insert into track(name_t,duration,album_id)
VALUES('sails',6,6);

insert into track(name_t,duration,album_id)
VALUES('heather',3,2);

insert into track(name_t,duration,album_id)
VALUES('fakes',7,3);

insert into track(name_t,duration,album_id)
VALUES('overtones',6,5);

insert into track(name_t,duration,album_id)
VALUES('rosehip hedge',5,7);

insert into track(name_t,duration,album_id)
VALUES('parting',4,6);

insert into track(name_t,duration,album_id)
VALUES('horizon',6,8);

insert into track(name_t,duration,album_id)
VALUES('steps',7,7);

insert into track(name_t,duration,album_id)
VALUES('carousel',8,7);

insert into track(name_t,duration,album_id)
VALUES('once',6,8);

insert into track(name_t,duration,album_id)
VALUES('storm',5,3);

insert into track(name_t,duration,album_id)
VALUES('Imagine',4,8);

insert into track(name_t,duration,album_id)
VALUES('one',3,5);



--Заполнение таблицы collection
insert into collection(name_c,year_creat)
VALUES('lawn games',2018);

insert into collection (name_c,year_creat)
VALUES('like before',2019);

insert into collection (name_c,year_creat)
VALUES('nostalgia',2020);

insert into collection (name_c,year_creat)
VALUES('Tomorrow',2021);

insert into collection (name_c,year_creat)
VALUES('picnic',2021);

insert into collection (name_c,year_creat)
VALUES('this way',2021);

insert into collection (name_c,year_creat)
values('meet',2022);

insert into collection (name_c,year_creat)
VALUES('dreams',2022);



--Заполнение таблицы album
insert into album (name_a,year_creat)
VALUES('spring again',2018);

insert into album (name_a,year_creat)
VALUES('you and me',2019);

insert into album (name_a,year_creat)
VALUES('eternity',2020);

insert into album (name_a,year_creat)
VALUES('the wall',2020);

insert into album (name_a,year_creat)
VALUES('new songs',2021);

insert into album (name_a,year_creat)
VALUES('morning trains',2021);

insert into album (name_a,year_creat)
VALUES('expectation',2022);

insert into album (name_a,year_creat)
VALUES('other worlds',2022);



-- Заполнение таблицы performeralbum
insert into performeralbum (performer_id,album_id)
VALUES(1,2);

insert into performeralbum (performer_id,album_id)
VALUES(1,7);

insert into performeralbum (performer_id,album_id)
VALUES(1,8);

insert into performeralbum (performer_id,album_id)
VALUES(2,1);

insert into performeralbum (performer_id,album_id)
VALUES(2,5);

insert into performeralbum (performer_id,album_id)
VALUES(3,3);

insert into performeralbum (performer_id,album_id)
VALUES(3,4);

insert into performeralbum (performer_id,album_id)
VALUES(4,6);

insert into performeralbum (performer_id,album_id)
VALUES(4,7);

insert into performeralbum (performer_id,album_id)
VALUES(5,1);

insert into performeralbum (performer_id,album_id)
VALUES(5,5);

insert into performeralbum (performer_id,album_id)
VALUES(6,2);

insert into performeralbum (performer_id,album_id)
VALUES(6,8);

insert into performeralbum (performer_id,album_id)
VALUES(7,1);

insert into performeralbum (performer_id,album_id)
VALUES(7,6);

insert into performeralbum (performer_id,album_id)
VALUES(8,4);


--Заполнение таблицы collectiontrack

insert into collectiontrack (collection_id,track_id)
VALUES(1,1);

insert into collectiontrack (collection_id,track_id)
VALUES(1,9);

insert into collectiontrack (collection_id,track_id)
VALUES(1,16);

insert into collectiontrack (collection_id,track_id)
VALUES(2,3);

insert into collectiontrack (collection_id,track_id)
VALUES(2,5);

insert into collectiontrack (collection_id,track_id)
VALUES(2,12);

insert into collectiontrack (collection_id,track_id)
VALUES(2,20);

insert into collectiontrack (collection_id,track_id)
VALUES(3,4);

insert into collectiontrack (collection_id,track_id)
VALUES(3,6);

insert into collectiontrack (collection_id,track_id)
VALUES(3,7);

insert into collectiontrack (collection_id,track_id)
VALUES(4,2);

insert into collectiontrack (collection_id,track_id)
VALUES(4,8);

insert into collectiontrack (collection_id,track_id)
VALUES(4,21);

insert into collectiontrack (collection_id,track_id)
VALUES(5,3);

insert into collectiontrack (collection_id,track_id)
VALUES(5,11);

insert into collectiontrack (collection_id,track_id)
VALUES(5,18);

insert into collectiontrack (collection_id,track_id)
VALUES(6,9);

insert into collectiontrack (collection_id,track_id)
VALUES(6,10);

insert into collectiontrack (collection_id,track_id)
VALUES(6,13);

insert into collectiontrack (collection_id,track_id)
VALUES(6,22);

insert into collectiontrack (collection_id,track_id)
VALUES(7,3);

insert into collectiontrack (collection_id,track_id)
VALUES(7,8);

insert into collectiontrack (collection_id,track_id)
VALUES(7,18);

insert into collectiontrack (collection_id,track_id)
VALUES(7,19);

insert into collectiontrack (collection_id,track_id)
VALUES(8,1);

insert into collectiontrack (collection_id,track_id)
VALUES(8,5);

insert into collectiontrack (collection_id,track_id)
VALUES(8,16);

insert into collectiontrack (collection_id,track_id)
VALUES(8,17);



--Заполнение таблицы genreperformer
insert into genreperformer (genre_id,performer_id)
VALUES(1,1);--не прошло

insert into genreperformer (genre_id,performer_id)
VALUES(1,6);

insert into genreperformer (genre_id,performer_id)
VALUES(2,1); -- не прошло

insert into genreperformer (genre_id,performer_id)
VALUES(2,3);

insert into genreperformer (genre_id,performer_id)
VALUES(3,2);

insert into genreperformer (genre_id,performer_id)
VALUES(3,5);

insert into genreperformer (genre_id,performer_id)
VALUES(3,7);

insert into genreperformer (genre_id,performer_id)
VALUES(4,4);

insert into genreperformer (genre_id,performer_id)
VALUES(4,7);

insert into genreperformer (genre_id,performer_id)
VALUES(5,3);

insert into genreperformer (genre_id,performer_id)
VALUES(5,8);





