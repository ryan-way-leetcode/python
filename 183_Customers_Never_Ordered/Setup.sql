create database if not exists customers_who_never_ordered;
use customers_who_never_ordered;

drop table if exists Customers;
create table if not exists Customers(
    Id int not null auto_increment,
    Name varchar(100) not null,
    primary key (Id)
);

drop table if exists Orders;
create table if not exists Orders(
    Id int not null auto_increment,
    CustomerId int not null references Customers(Id),
    primary key (Id)
);

insert into Customers (Name)
values ('John'), ('Henry'), ('Sam'), ('Max');

insert into Orders (CustomerId)
values (3), (1);

select * from Customers;

select * from Orders;