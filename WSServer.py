###############################################################################
##
##  Copyright (C) 2011-2014 Tavendo GmbH
##
##  Licensed under the Apache License, Version 2.0 (the "License");
##  you may not use this file except in compliance with the License.
##  You may obtain a copy of the License at
##
##      http://www.apache.org/licenses/LICENSE-2.0
##
##  Unless required by applicable law or agreed to in writing, software
##  distributed under the License is distributed on an "AS IS" BASIS,
##  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.aFWEQWEFFFS
##  See the License for the specific language governing permissions and
##  limitations under the License.
##
###############################################################################
import DataManage
from autobahn.twisted.websocket import WebSocketServerProtocol, \
                                       WebSocketServerFactory


class MyServerProtocol(WebSocketServerProtocol):

	def onConnect(self, request):
		print("Client connecting: {0}".format(request.peer))

	def onOpen(self):
		print("WebSocket connection open.")
		
	def onMessage(self, payload, isBinary):
		decodelist = payload.split("/%/")
		requestType = decodelist[0]
		if isBinary:
			print("Binary message received: {0} bytes".format(len(payload)))
		else:
			print("Text message received: {0}".format(payload.decode('utf8')) + " from " + str(self.transport.getPeer()))
			
			if requestType=="collegeBoardRequest":
				city = decodelist[1]
				message = DataManage.getPostsByRegion(city)
				self.sendMessage("collegeBoardData>:>" + str(message), isBinary)

			if requestType=="login":
				#id = decodelist[1]
				gender = decodelist[2]
				#latitude = decodelist[3]
				#longitude = decodelist[4]
				region_id = decodelist[5]
				user_id = DataManage.addUser(region_id, gender)
				self.sendMessage("yourNewID>:>" + str(user_id))

			# if requestType=="locationis":
			# 	latitude = decodelist[1]
			# 	longitude = decodelist[2]
			# 	id = decodelist[3]
			# 	DataManage.updateLocation(latitude + " " + longitude, id)
				
			# if requestType=="sendCollegePost":
			# 	content = decodelist[1]
			# 	city = decodelist[2]
			# 	id = decodelist[3]
			# 	DataManage.addToGeneral(content, city, id)
			# 	message = DataManage.getCollegeBoard(city)
			# 	self.sendMessage("collegeBoardData>:>" + str(message), isBinary)

			if requestType=="postToHopSpot":
				content = decodelist[1]
				city = decodelist[2]
				id = decodelist[3]
				hopspot = decodelist[4]
				DataManage.postToHopSpot(content, hopspot, city, id)
				message = DataManage.getHopSpotBoard(city,hopspot)
				self.sendMessage("hopSpotData>:>" + city + ">:>" + hopspot + ">:>" + str(message), isBinary)
				
			if requestType=="getSpotBoard":
				city = decodelist[1];
				hopspot = decodelist[2];
				message = DataManage.getHopSpotBoard(city,hopspot)
				self.sendMessage("hopSpotData>:>" + city + ">:>" + hopspot + ">:>" + str(message), isBinary)
			
		#self.sendMessage(payload, isBinary)

	def onClose(self, wasClean, code, reason):
		print("WebSocket connection closed: {0}".format(reason))

if __name__ == '__main__':

   import sys

   from twisted.python import log
   from twisted.internet import reactor

   log.startLogging(sys.stdout)

   factory = WebSocketServerFactory("ws://localhost:160", debug = False)
   factory.protocol = MyServerProtocol

   reactor.listenTCP(160, factory)
   reactor.run()