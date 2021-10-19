create database if not exists delete_duplicate_emails;
use delete_duplicate_emails;

drop table if exists Person;
create table if not exists Person(
    Id int not null auto_increment,
    Email varchar(100) not null,
    primary key (Id)
);

insert into Person (Email)
values ('john@example.com'), 
('bob@example.com'), 
('john@example.com');

select * from Person;