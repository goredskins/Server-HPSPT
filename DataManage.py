import sqlite3
import json, urllib
import datetime
import time
	
def deleteFromDatabase(id):
	conn = sqlite3.connect('hotspotdatabase.db')
	c = conn.cursor()
	c.execute('DELETE FROM User WHERE id= ?', id)
	conn.commit()
	
# def getBoard(typeP, hotspot, city):
# 	conn = sqlite3.connect('hotspotdatabase.db')
# 	c = conn.cursor()
# 	toReturn = "";
# 	if typeP == "city":
# 		doSomething
# 	if typeP == "hotspot":
# 		doSomething
# 	c.execute('INSERT INTO Posts(content,city)')
	
	
def postToHopSpot(content, hopspot_id, region_id, user_id):
	conn = sqlite3.connect('hotspotdatabase.db')
	c = conn.cursor()
	#ts = time.time()
	#st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
	c.execute('INSERT INTO Posts(hopspot_id, content, user_id, region_id) VALUES(?,?,?,?,?)', [hopspot_id, content, user_id, region_id])
	conn.commit()
	
def getPostsByRegion(region_id):
	conn = sqlite3.connect('hotspotdatabase.db')
	c = conn.cursor()
	toReturn = "";
	c.execute("SELECT content, Users.gender as gender FROM Posts INNER JOIN Users ON Posts.user_id = Users.id  WHERE region_id = ? and time > datetime('now','-1 day') order by time DESC", [region_id])
	Posts = c.fetchall()
	for(item,) in Posts:
		toReturn = toReturn + item.content + "/@$/ "
	return toReturn
	
def getHopSpotBoard(hopspot_id):
	conn = sqlite3.connect('hotspotdatabase.db')
	c = conn.cursor()
	toReturn = "";
	c.execute("SELECT content, Users.gender as gender FROM Posts INNER JOIN Users ON Posts.user_id = Users.id  FROM Posts WHERE hotspot=? and posttime > datetime('now','-1 day') order by posttime DESC", [city,hopspot])
	Posts = c.fetchall()
	if(len(Posts) == 0):
		toReturn = "Start the conversation!";
	for(item,) in Posts:
		toReturn = toReturn + item.content + "/@$/ "
	return toReturn

def addUser(gender, region_id):
	conn = sqlite3.connect('hotspotdatabase.db')
	c = conn.cursor()
	c.execute('INSERT INTO Users(gender, region_id) VALUES(?,?)', [gender, region_id])
	conn.commit()
	return conn.last_insert_rowid()

# def updateLocation(position, id):
# 	conn = sqlite3.connect('hotspotdatabase.db')
# 	c = conn.cursor()
# 	c.execute('UPDATE Login SET location = ? WHERE phoneID = ?', [position, id])
# 	conn.commit()
	
def addHotspot(name, gps_location, region_id): #should probably add beacon_id as well
	conn = sqlite3.connect('hotspotdatabase.db')
	c = conn.cursor()
	c.execute('INSERT INTO Hotspots(name, gps_location, region_id) VALUES(?,?,?)', [name, gps_location, region_id])
	conn.commit()
	
def addRegion(name, gps_center, radius):
	conn = sqlite3.connect('hotspotdatabase.db')
	c = conn.cursor()
	c.execute('INSERT INTO Regions(name, gps_center, radius) VALUES(?,?,?)', [name, gps_center, radius])
	conn.commit()
	
def fillTestData():
	user_id = addUser(1, 1) #male in Charlottesville
	addUser(0, 1)
	addUser(1, 1) #male in Charlottesville
	addUser(0, 1)
	addUser(1, 1) #male in Charlottesville
	addUser(0, 1)
	addUser(1, 1) #male in Charlottesville
	addUser(0, 1)
	
# addHotspot("119B Appletree", "38.028259 -78.520009", "University of Virginia")
# addLocation("Springfield", "22153", "Springfield")
# addLocation("Charlottesville", "22903", "University of Virginia")
# addHotspot("Boylan Heights", "38.034291 -78.499328", "University of Virginia")
# addHotspot("The Virginian", "38.035323 -78.500607", "University of Virginia")
# addHotspot("Coupe's", "38.035822 -78.500275", "University of Virginia")
# addHotspot("Trinity", "38.034667 -78.500451", "University of Virginia")
# addHotspot("Biltmore", "38.036222 -78.500483", "University of Virginia")
# addHotspot("Mellow Mushroom", "38.033711 -78.498658", "University of Virginia")
# addHotspot("Mock Location", "38.756863 -77.257808", "University of Virginia")
# addModDatabase('1', '38.034667 -78.500451', 'female', 'Charlottesville');
# addModDatabase('1', '38.034073 -78.499510', 'female', 'Charlottesville');
# addModDatabase('2', '38.034080 -78.500499', 'female', 'Charlottesville');
# addModDatabase('3', '38.034078 -78.500495', 'female', 'Charlottesville');
# addModDatabase('4', '38.034069 -78.500493', 'male', 'Charlottesville');
# addModDatabase('5', '38.034074 -78.500491', 'male', 'Charlottesville');
# addModDatabase('6', '38.034070 -78.500492', 'male', 'Charlottesville');
# addModDatabase('7', '38.034077 -78.499432', 'female', 'Charlottesville');
# addModDatabase('8', '38.035332 -78.500607', 'female', 'Charlottesville');                     """ the virginian """
# addModDatabase('9', '38.035333 -78.500603', 'female', 'Charlottesville');
# addModDatabase('10', '38.035330 -78.500608', 'male', 'Charlottesville');
# addModDatabase('11', '38.035428 -78.500610', 'male', 'Charlottesville');
# addModDatabase('12', '38.035430 -78.500604', 'male', 'Charlottesville');
# addModDatabase('13', '38.035328 -78.500451', 'female', 'Charlottesville');
# addModDatabase('14', '38.034667 -78.500451', 'female', 'Charlottesville');
# addModDatabase('15', '38.034667 -78.500451', 'female', 'Charlottesville');                   """ Coupe's """
# addModDatabase('16', '38.034667 -78.500451', 'male', 'Charlottesville');
# addModDatabase('17', '38.034667 -78.500451', 'male', 'Charlottesville');
# addModDatabase('18', '38.034667 -78.500451', 'male', 'Charlottesville');
# addModDatabase('19', '38.034667 -78.500451', 'female', 'Charlottesville');
# addModDatabase('20', '38.034667 -78.500451', 'female', 'Charlottesville');
# addModDatabase('21', '38.034667 -78.500451', 'female', 'Charlottesville');
# addModDatabase('22', '38.034667 -78.500451', 'male', 'Charlottesville');                     """ Trinity """
# addModDatabase('23', '38.034664 -78.500453', 'male', 'Charlottesville');
# addModDatabase('24', '38.034669 -78.500457', 'male', 'Charlottesville');
# addModDatabase('25', '38.034667 -78.500453', 'female', 'Charlottesville');
# addModDatabase('26', '38.034668 -78.500453', 'female', 'Charlottesville');
# addModDatabase('27', '38.034677 -78.500456', 'female', 'Charlottesville');
# addModDatabase('28', '38.034663 -78.500441', 'male', 'Charlottesville');
# addModDatabase('29', '38.036222 -78.500483', 'male', 'Charlottesville');                     """ Biltmore """
# addModDatabase('30', '38.036232 -78.500480', 'male', 'Charlottesville');
# addModDatabase('31', '38.036227 -78.500481', 'female', 'Charlottesville');
# addModDatabase('32', '38.036223 -78.500491', 'female', 'Charlottesville');
# addModDatabase('33', '38.036221 -78.500481', 'female', 'Charlottesville');
# addModDatabase('34', '38.036231 -78.500485', 'male', 'Charlottesville');
# addModDatabase('35', '38.033711 -78.498658', 'male', 'Charlottesville');                    """ mellow mushroom """
# addModDatabase('36', '38.033722 -78.498663', 'male', 'Charlottesville');
# addModDatabase('37', '38.033715 -78.499000', 'female', 'Charlottesville');
# addModDatabase('37', '38.034231 -78.498662', 'female', 'Charlottesville');
# addModDatabase('37', '38.034241 -78.499010', 'female', 'Charlottesville');
	
def fillTestBoardData():
	postToHopSpot("post content", 1, 1, 1)
	postToHopSpot("post content", 1, 1, 1)

# getCityData('Louisville')
# updateLocation('28.033983 -78.4993632', '000000004')

	