
from protocol import *
import asyncio 
import playground

class ClientProtocol(asyncio.Protocol):

	def send_packet(self, packet):
		print("Client Sending data-->",packet.DEFINITION_IDENTIFIER)		
		self.transport.write(packet.__serialize__())
	
	def __init__(self,loop):
		self.loop = loop
		self.transport = None

	def connection_made(self, transport):
		self._deserializer = PacketType.Deserializer()	
		self.transport = transport
		print("Client Connected to Server ")
		pkt1 = DB_connect()
		send_packet(pkt1)
		print("Sent")

	
	def data_received(self, data):
		self._deserializer.update(data)
		for pkt in self._deserializer.nextPackets():
			if(pkt.DEFINITION_IDENTIFIER=="connect_credentials"):
				pkt = Response_Credentials()
				pkt.DEFINITION_IDENTIFIER = "response_credentials"
				pkt.username = "root" 
				pkt.password = "toor"
				self.send_packet(pkt)	

			if(pkt.DEFINITION_IDENTIFIER=="connection_response" and pkt.status==True):
				print("Success")	
			

	def connection_lost(self, exc):
		print('The server closed the connection')
		print('Stop the event loop')
		#self.transport=None
		self.loop.stop()




def client_run():

	loopC = asyncio.get_event_loop()
	coroC = playground.getConnector().create_playground_connection(lambda: ClientProtocol(loopC), '20174.1.1.1', 8000)
	loopC.run_until_complete(coroC)

	loopC.run_forever()
	loopC.close()

client_run()
