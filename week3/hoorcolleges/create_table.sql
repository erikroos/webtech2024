create table users (
 --id integer primary key autoincrement, --niet nodig want SQLite geeft je standaard al een kolom "rowid"
 username varchar(64),
 password varchar(64)
);

insert into users (username, password) values ("erik", "geheim"); --als dit niet werkt: probeer single quotes (')
insert into users (username, password) values ("bart", "geheimer");