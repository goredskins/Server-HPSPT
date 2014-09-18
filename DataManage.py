import sqlite3
import json, urllib
import datetime
import time
	
def deleteFromDatabase(phoneID):
	conn = sqlite3.connect('hotspotdatabase.db')
	c = conn.cursor()
	c.execute('DELETE FROM Login WHERE phoneID=?')
	conn.commit()
	
def getBoard(typeP, hotspot, city):
	conn = sqlite3.connect('hotspotdatabase.db')
	c = conn.cursor()
	toReturn = "";
	if typeP == "city":
		doSomething
	if typeP == "hotspot":
		doSomething
	c.execute('INSERT INTO Posts(content,city)')
	
	
def addToHopSpot(content, hopspot, city, phoneID):
	conn = sqlite3.connect('hotspotdatabase.db')
	c = conn.cursor()
	ts = time.time()
	st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
	c.execute('INSERT OR REPLACE INTO Posts(posttime,content,hotspot,city,phoneID) VALUES(?,?,?,?,?)', [st,content,hopspot,city,phoneID])
	conn.commit()
	

def addToGeneral(content, city, phoneID):
	conn = sqlite3.connect('hotspotdatabase.db')
	c = conn.cursor()
	ts = time.time()
	st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
	c.execute('INSERT OR REPLACE INTO Posts(posttime,content,hotspot,city,phoneID) VALUES(?,?,?,?,?)', [st,content, "general",city,phoneID])
	conn.commit()
	
def getCollegeBoard(city):
	conn = sqlite3.connect('hotspotdatabase.db')
	c = conn.cursor()
	toReturn = "";
	c.execute("SELECT content FROM Posts WHERE city=? and posttime > datetime('now','-1 day') order by posttime DESC", [city])
	Posts = c.fetchall()
	for(item,) in Posts:
		toReturn = toReturn + item + "/@$/ "
	return toReturn
	
def getHopSpotBoard(city,hopspot):
	conn = sqlite3.connect('hotspotdatabase.db')
	c = conn.cursor()
	toReturn = "";
	c.execute("SELECT content FROM Posts WHERE city=? and hotspot=? and posttime > datetime('now','-1 day') order by posttime DESC", [city,hopspot])
	Posts = c.fetchall()
	if(len(Posts) == 0):
		toReturn = "Start the conversation!";
	for(item,) in Posts:
		toReturn = toReturn + item + "/@$/ "
	return toReturn

def addModDatabase(phoneID, location, gender, city):
	conn = sqlite3.connect('hotspotdatabase.db')
	c = conn.cursor()
	c.execute('INSERT OR REPLACE INTO Login(phoneID,location,gender, city) VALUES(?,?,?,?)', [phoneID, location, gender, city])
	conn.commit()
	
def addNewID(gender, location, city):
	conn = sqlite3.connect('hotspotdatabase.db')
	c = conn.cursor()
	toReturn = "";
	c.execute('SELECT * from Login order by phoneID DESC LIMIT 1')
	newID = c.fetchone()[0] + 1
	c.execute('INSERT OR REPLACE INTO Login(phoneID,location,gender,city) VALUES(?,?,?,?)', [newID, location, gender, "Charlottesville"])
	conn.commit()
	return newID;
	
def getCityData(city):
	conn = sqlite3.connect('hotspotdatabase.db')
	c = conn.cursor()
	c.execute('SELECT Location FROM Login WHERE city = ?', [city])
	Locations = c.fetchall()
	toReturn = ""
	for (item,) in Locations:
			toReturn = toReturn + item + ", "
	return toReturn
	
def getHotspots(city):
	conn = sqlite3.connect('hotspotdatabase.db')
	c = conn.cursor()
	c.execute('SELECT college FROM Locations WHERE location = ? LIMIT 1', [city])
	College = c.fetchone()[0]
	c.execute('SELECT establishment FROM Hotspots WHERE college = ?', [College])
	Hotspots = c.fetchall()
	jsondict = {}
	toReturn = ""
	for (item,) in Hotspots:
		c.execute('SELECT location FROM Hotspots WHERE establishment = ?', [item])
		Establishment = c.fetchone()[0]
		jsondict[item] = Establishment
	return json.JSONEncoder().encode(jsondict)
	

def updateLocation(position, id):
	conn = sqlite3.connect('hotspotdatabase.db')
	c = conn.cursor()
	c.execute('UPDATE Login SET location = ? WHERE phoneID = ?', [position, id])
	conn.commit()
	
	
def addHotspot(establishment, location, college):
	conn = sqlite3.connect('hotspotdatabase.db')
	c = conn.cursor()
	c.execute('INSERT OR REPLACE INTO Hotspots(establishment,location,college) VALUES(?,?,?)', [establishment, location, college])
	conn.commit()
	
def addLocation(location, zipcode, college):
	conn = sqlite3.connect('hotspotdatabase.db')
	c = conn.cursor()
	c.execute('INSERT OR REPLACE INTO Locations(location,zipcode,college) VALUES(?,?,?)', [location, zipcode, college])
	conn.commit()
	
def fillTestData():
	addModDatabase('000000001', '38.034066 -78.499442', 'male', 'Charlottesville')
	addModDatabase('000000002', '38.035323 -78.500607', 'female', 'Charlottesville')
	addModDatabase('000000003', '38.035822 -78.500607', 'male', 'Charlottesville')
	addModDatabase('000000004', '38.343667 -78.500451', 'female', 'Charlottesville')
	addModDatabase('000000005', '38.036222 -78.500483', 'female', 'Charlottesville')
	addModDatabase('000000006', '38.033711 -78.498658', 'female', 'Charlottesville')
	addModDatabase('000000007', '28.033983 -78.4993642', 'male', 'Springfield')
	addModDatabase('000000008', '28.033983 -78.4993642', 'female', 'Louisville')
	
addHotspot("119B Appletree", "38.028259 -78.520009", "University of Virginia")
addLocation("Springfield", "22153", "Springfield")
addLocation("Charlottesville", "22903", "University of Virginia")
addHotspot("Boylan Heights", "38.034291 -78.499328", "University of Virginia")
addHotspot("The Virginian", "38.035323 -78.500607", "University of Virginia")
addHotspot("Coupe's", "38.035822 -78.500275", "University of Virginia")
addHotspot("Trinity", "38.034667 -78.500451", "University of Virginia")
addHotspot("Biltmore", "38.036222 -78.500483", "University of Virginia")
addHotspot("Mellow Mushroom", "38.033711 -78.498658", "University of Virginia")
addHotspot("Mock Location", "38.756863 -77.257808", "University of Virginia")
addModDatabase('1', '38.034667 -78.500451', 'female', 'Charlottesville');
addModDatabase('1', '38.034073 -78.499510', 'female', 'Charlottesville');
addModDatabase('2', '38.034080 -78.500499', 'female', 'Charlottesville');
addModDatabase('3', '38.034078 -78.500495', 'female', 'Charlottesville');
addModDatabase('4', '38.034069 -78.500493', 'male', 'Charlottesville');
addModDatabase('5', '38.034074 -78.500491', 'male', 'Charlottesville');
addModDatabase('6', '38.034070 -78.500492', 'male', 'Charlottesville');
addModDatabase('7', '38.034077 -78.499432', 'female', 'Charlottesville');
addModDatabase('8', '38.035332 -78.500607', 'female', 'Charlottesville');                     """ the virginian """
addModDatabase('9', '38.035333 -78.500603', 'female', 'Charlottesville');
addModDatabase('10', '38.035330 -78.500608', 'male', 'Charlottesville');
addModDatabase('11', '38.035428 -78.500610', 'male', 'Charlottesville');
addModDatabase('12', '38.035430 -78.500604', 'male', 'Charlottesville');
addModDatabase('13', '38.035328 -78.500451', 'female', 'Charlottesville');
addModDatabase('14', '38.034667 -78.500451', 'female', 'Charlottesville');
addModDatabase('15', '38.034667 -78.500451', 'female', 'Charlottesville');                   """ Coupe's """
addModDatabase('16', '38.034667 -78.500451', 'male', 'Charlottesville');
addModDatabase('17', '38.034667 -78.500451', 'male', 'Charlottesville');
addModDatabase('18', '38.034667 -78.500451', 'male', 'Charlottesville');
addModDatabase('19', '38.034667 -78.500451', 'female', 'Charlottesville');
addModDatabase('20', '38.034667 -78.500451', 'female', 'Charlottesville');
addModDatabase('21', '38.034667 -78.500451', 'female', 'Charlottesville');
addModDatabase('22', '38.034667 -78.500451', 'male', 'Charlottesville');                     """ Trinity """
addModDatabase('23', '38.034664 -78.500453', 'male', 'Charlottesville');
addModDatabase('24', '38.034669 -78.500457', 'male', 'Charlottesville');
addModDatabase('25', '38.034667 -78.500453', 'female', 'Charlottesville');
addModDatabase('26', '38.034668 -78.500453', 'female', 'Charlottesville');
addModDatabase('27', '38.034677 -78.500456', 'female', 'Charlottesville');
addModDatabase('28', '38.034663 -78.500441', 'male', 'Charlottesville');
addModDatabase('29', '38.036222 -78.500483', 'male', 'Charlottesville');                     """ Biltmore """
addModDatabase('30', '38.036232 -78.500480', 'male', 'Charlottesville');
addModDatabase('31', '38.036227 -78.500481', 'female', 'Charlottesville');
addModDatabase('32', '38.036223 -78.500491', 'female', 'Charlottesville');
addModDatabase('33', '38.036221 -78.500481', 'female', 'Charlottesville');
addModDatabase('34', '38.036231 -78.500485', 'male', 'Charlottesville');
addModDatabase('35', '38.033711 -78.498658', 'male', 'Charlottesville');                    """ mellow mushroom """
addModDatabase('36', '38.033722 -78.498663', 'male', 'Charlottesville');
addModDatabase('37', '38.033715 -78.499000', 'female', 'Charlottesville');
addModDatabase('37', '38.034231 -78.498662', 'female', 'Charlottesville');
addModDatabase('37', '38.034241 -78.499010', 'female', 'Charlottesville');
	
def fillTestBoardData():
	addToCollegeBoards("Test text 1", "Springfield", "00001")
	addToCollegeBoards("Test tefowi", "Charlottesville", "00002")
	addToCollegeBoards("Test t123", "Springfield", "00003")
	addToCollegeBoards("Test teawfeoi", "Charlottesville", "00004")

	
	



# getCityData('Louisville')
# updateLocation('28.033983 -78.4993632', '000000004')

	