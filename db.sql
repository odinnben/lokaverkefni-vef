#Titill - Sena - Gefið-út - Rating - Director - lýsing - lengd - aldurstakmark - framleiðandi - myndarskjal
drop database if exists 1501002670_kvikmyndir;
create database 1501002670_kvikmyndir;
use 1501002670_kvikmyndir;

create table biomyndir(
	myndID int primary key auto_increment,
    titill varchar(150),
    aldurstakmark varchar(5),
    gefidUt date,
    rating int(3),
    lengd int,
    framleidandi varchar(100),
    myndarskjal varchar(60),
    trailerYT varchar(150),
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
create table admin(
    notandi varchar(40) primary key,
    lykilord varchar(40) not null,
    Fname varchar(60) not null,
    Lname varchar(60),
    email varchar(80)
);

insert into admin(notandi,lykilord,Fname,Lname,email) values
('Matti','12345','Matti',null,null),
('Óðinn','12345','Óðinn','Ben','odinn@gmail.com')
;

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

insert into biomyndir(titill,aldurstakmark,gefidUt,rating,lengd,framleidandi,myndarskjal,trailerYT,lysing) 
values('Avengers: Infinity War','PG-13','2018-04-27',9,149,'Marvel Studios','infinity-war.png','QwievZ1Tx-8','The Avengers and their allies must be willing to sacrifice all in an attempt to defeat the powerful Thanos before his blitz of devastation and ruin puts an end to the universe.');

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
