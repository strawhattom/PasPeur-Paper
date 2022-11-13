DROP DATABASE IF EXISTS paspeur_paper; 
CREATE DATABASE IF NOT EXISTS paspeur_paper;
use paspeur_paper;

drop table if exists addresses;
create table if not exists addresses(
	addressID int primary key,
    number int,
    street varchar(30),
    city varchar(30)
);
drop table if exists users;
create table if not exists users(
	userID int primary key auto_increment,
    email varchar(20),
    pwd varchar(100),
    role enum('client','admin') default 'client',
    address varchar(50),
    firstName varchar(20),
    lastName varchar(20),
    phone varchar(10)
);
drop table if exists products;
create table if not exists products(
	productID int primary key,
    nameP varchar(20),
	format varchar(20),
	style varchar(20),
	type varchar(20),
	colour varchar(20),
	stock int,
	price float,
	image blob
);

drop table if exists orders;
create table if not exists orders(
	orderID int,
    userID int,
    dateOrder date,
    dateDelivery date,
    primary key(orderID,userID),
	foreign key (userID)
		references users (userID)
);

drop table if exists quantityOrder;
create table if not exists quantityOrder(
	productID int,
    orderID int,
    quantity int,
	primary key(productID,orderID),
    foreign key(productID)
		references products (productID)
        on delete cascade
        on update no action,
	foreign key(orderID)
		references orders (orderID)
        on delete cascade
        on update no action
);