CREATE TABLE Login(phoneID int, location varchar(30), gender varchar(10), city varchar(30), PRIMARY KEY (phoneID));
CREATE TABLE Locations(location varchar(30), zipcode varchar(5), college varchar(30),  PRIMARY KEY (college));
CREATE TABLE Hotspots(establishment varchar(30), location varchar(30), college varchar(30), PRIMARY KEY (establishment));
CREATE TABLE Posts(posttime varchar(30), content varchar(120), hotspot varchar(30), city varchar(30), phoneID varchar(15), PRIMARY KEY (posttime, phoneID));