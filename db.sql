#Titill - Sena - Gefið-út - Rating - Director - lýsing - lengd - aldurstakmark - framleiðandi - myndarskjal
drop database if exists 1501002670_kvikmyndir;
create database 1501002670_kvikmyndir;
use 1501002670_kvikmyndir;

create table biomyndir(
	myndID int primary key auto_increment,
    titill varchar(150),
    aldurstakmark varchar(5),
    gefidUt date,
    rating int(2),
    lengd int,
    framleidandi varchar(100),
    myndarskjal varchar(60),
    lysing varchar(255)
);
create table directors(
    dirID int primary key auto_increment,
    dirName varchar(100)
);
create table bioDir(
	myndID int,
    foreign key (myndID) references biomyndir(myndID),
	dirID int,
    foreign key (dirID) references directors(dirID)
);
create table senur(
	senID int primary key auto_increment,
    sena varchar(100)
);
create table bioSen(
	myndID int,
    foreign key (myndID) references biomyndir(myndID),
	senID int,
    foreign key (senID) references senur(senID)
);

insert into senur(sena) values
	('Documentary'),
	('Short'),
	('Animation'),
	('Comedy'),
	('Romance'),
	('Sport'),
	('News'),
	('Drama'),
	('Fantasy'),
	('Horror'),
	('Biography'),
	('Music'),
	('War'),
	('Crime'),
	('Western'),
	('Family'),
	('Adventure'),
	('History'),
	('Sci-Fi'),
	('Action'),
	('Mystery'),
	('Thriller'),
	('Musical'),
	('Film-Noir'),
	('Game-Show'),
	('Talk-Show'),
	('Reality-TV'),
	('Adult'),
	('2010')
;

insert into biomyndir(titill,aldurstakmark,gefidUt,rating,lengd,framleidandi,myndarskjal,lysing) 
values('Avengers: Infinity War','PG-13','2018-04-27',9,149,'Marvel Studios','infinity-war.png','The Avengers and their allies must be willing to sacrifice all in an attempt to defeat the powerful Thanos before his blitz of devastation and ruin puts an end to the universe.');

insert into bioSen(myndID,senID) values 
	((select myndID from biomyndir where titill = 'Avengers: Infinity War'),(select senID from senur where sena = 'Action')),
	((select myndID from biomyndir where titill = 'Avengers: Infinity War'),(select senID from senur where sena = 'Adventure')),
	((select myndID from biomyndir where titill = 'Avengers: Infinity War'),(select senID from senur where sena = 'Fantasy'))
;
insert into directors(dirName) values
	('Anthony Russo'),
    ('Joe Russo')
;
insert into bioDir(myndID,dirID) values
	((select myndID from biomyndir where titill = 'Avengers: Infinity War'),(select dirID from directors where dirName = 'Anthony Russo')),
	((select myndID from biomyndir where titill = 'Avengers: Infinity War'),(select dirID from directors where dirName = 'Joe Russo'))
;
