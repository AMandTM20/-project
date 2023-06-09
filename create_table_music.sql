--Создание таблиц для базы music
CREATE TABLE IF NOT EXISTS Genre(
	id SERIAL PRIMARY KEY,
	name_g VARCHAR(40) NOT NULL
);
CREATE TABLE IF NOT EXISTS Performer(
	id SERIAL PRIMARY KEY,
	name_g VARCHAR(40) NOT NULL
);
CREATE TABLE IF NOT EXISTS Album(
	id SERIAL  PRIMARY KEY,
	name_a VARCHAR(100) NOT NULL,
	year_creat INTEGER  NOT NULL
);
CREATE TABLE IF NOT EXISTS Track(
	id SERIAL  PRIMARY KEY,
	name_t VARCHAR(100) NOT NULL,
	duration INTEGER NOT NULL,
	album_id INTEGER REFERENCES Album(id)
);
CREATE TABLE IF NOT EXISTS Collection(
	id SERIAL PRIMARY KEY,
	name_c VARCHAR(100) NOT NULL,
	year_creat INTEGER NOT NULL
 );
CREATE TABLE IF NOT EXISTS GenrePerformer(
	genre_id INTEGER REFERENCES Genre(id),
	performer_id INTEGER REFERENCES Performer(id),
	CONSTRAINT pk6 PRIMARY KEY (genre_id, performer_id)
);
CREATE TABLE IF NOT EXISTS PerformerAlbum(
	performer_id INTEGER REFERENCES Performer(id),
	album_id INTEGER REFERENCES Album(id),
	CONSTRAINT pk7 PRIMARY KEY (performer_id, album_id)
);
CREATE TABLE IF NOT EXISTS CollectionTrack (
	collection_id INTEGER REFERENCES Collection(id),
	track_id INTEGER REFERENCES Track(id),
	CONSTRAINT pk8 PRIMARY KEY (collection_id, track_id)
);

