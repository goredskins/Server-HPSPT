CREATE TABLE Users(id int, hopspot_id int, last_hopspot_id int, region_id int, gender int, PRIMARY KEY (id));
CREATE TABLE Regions(id int, name varchar(50), gps_center varchar(30),  radius int, PRIMARY KEY (id));
CREATE TABLE Hotspots(id int, name varchar(50), gps_location varchar(30), females int, males int, beacon_id int, PRIMARY KEY (id));
CREATE TABLE Posts(id int, time timestamp, hotspot_id int, content varchar(140), user_id int, region_id int, PRIMARY KEY (id));