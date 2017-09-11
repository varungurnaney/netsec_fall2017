"""
Author: Varun R Gurnaney
Email: varungurnaney@jhu.edu
"""

from playground.network.packet import PacketType
from playground.network.packet.fieldtypes import UINT32, STRING, BUFFER, BOOL
from playground.asyncio_lib.testing import TestLoopEx
from playground.network.testing import MockTransportToStorageStream
from playground.network.testing import MockTransportToProtocol

import asyncio

#Creating Class for Packet1 
class DB_connect(PacketType):
	DEFINITION_IDENTIFIER = "client_db_connect"
	DEFINITION_VERSION = "1.0"
	
#Creating Class for Packet2	
class Connect_Credentials(PacketType):
	DEFINITION_IDENTIFIER = "connect_credentials"
	DEFINITION_VERSION = "1.0"
	FIELDS = [
	("username", STRING),
	("password", STRING),
	]
#Creating Class for Packet3
class Response_Credentials(PacketType):
	DEFINITION_IDENTIFIER = "response_credentials"
	DEFINITION_VERSION = "1.0"
	FIELDS = [
	("username", STRING),
	("password", STRING),
	]
#Creating Class for Packet4
class Connection_Response(PacketType):
	DEFINITION_IDENTIFIER = "connection_response"
	DEFINITION_VERSION = "1.0"
	FIELDS = [
	("status", BOOL),
	("sessionID", STRING),
	]
	

class ClientProtocol(asyncio.Protocol):

	def __init__(self,loop):
		self.loop = loop

	def connection_made(self, transport):
		self.transport = transport
		print("Client Connected to Server ")
		"""self.message = "db_connect()"
		transport.write(self.message.encode())
		print('Data sent')"""

	def send_packet(self, packet):
		print("Sending data")		
		self.transport.write(packet.__serialize__())
		print('Data sent')
	
	def data_received(self, data):
		print('Data received')

	def connection_lost(self, exc):
		print('The server closed the connection')
		print('Stop the event loop')
		#self.transport=None
		self.loop.stop()




class ServerProtocol(asyncio.Protocol):

	def connection_made(self, transport):
		print("Server Connected to Client ")
		self._deserializer = PacketType.Deserializer()		
		self.transport = transport
			

	def data_received(self, data):
		self._deserializer.update(data)
		for pkt in self._deserializer.nextPackets():
		#self.transport.write(data)
			if(pkt.DEFINITION_IDENTIFIER=="client_db_connect()")
			{
				
			}
			if(pkt.DEFINITION_IDENTIFIER=="client_db_connect()")
			{
				
			}

			if(pkt.DEFINITION_IDENTIFIER=="client_db_connect()")
			{
				
			}


	def send_packet(self, packet)
		print("Send Response to Client..")
		
		
	def connection_lost(self, exc):
		print("Echo Server Connection Lost because {}".format(exc))



def basicUnitTest():
	
	loop = 	TestLoopEx()
	asyncio.set_event_loop(TestLoopEx())
	
	client = ClientProtocol(loop)	
	server = ServerProtocol()
	
	transportToServer = MockTransportToProtocol(server)
	transportToClient = MockTransportToProtocol(client)
	
	server.connection_made(transportToClient)	
	client.connection_made(transportToServer)		

	pkt1 = DB_connect()	
	client.send_packet(pkt1)
	

if __name__=="__main__":
    basicUnitTest()
print("\n---Basic Unit Test Successful---\n")
















