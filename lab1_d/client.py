
from playground.network.packet import PacketType
from protocol import *
import asyncio 
import playground

class ClientProtocol(asyncio.Protocol):


	def __init__(self, callback=None):
		self.buffer = ""
		if callback:
			self.callback = callback
		else:
			self.callback = print
		self.transport = None
		self.deserializer = PacketType.Deserializer()
		#print("Init success")

	def connection_made(self, transport):
		self._deserializer = PacketType.Deserializer()	
		self.transport = transport
		print("Client Connected to Server")
		#print(transport)
		#print(typeof(self.transport))	
		


	def data_received(self, data):
		self._deserializer.update(data)
		for pkt in self._deserializer.nextPackets():
			if(pkt.DEFINITION_IDENTIFIER=="connect_credentials"):
				pkt = Response_Credentials()
				pkt.DEFINITION_IDENTIFIER = "response_credentials"
				pkt.username = "root" 
				pkt.password = "toor"
				self.sendpacket(pkt)	

			elif(pkt.DEFINITION_IDENTIFIER=="connection_response" and pkt.status==True):
				print("Success")	

	def sendpacket(self,packet):
		print("Client Sending data-->",packet.DEFINITION_IDENTIFIER)
		#self.transport = transport		
		self.transport.write(packet.__serialize__())

	def setTransport(self, transport):
		self.transport = transport

	def buildProtocol(self):
		#print("bp success")
		return ClientProtocol(self.callback)			

	def connection_lost(self, exc):
		print('The server closed the connection')
		print('Stop the event loop')
		#self.transport=None
		self.loop.stop()




def client_run():

	loopC = asyncio.get_event_loop()
	control = ClientProtocol()
	coroC = playground.getConnector().create_playground_connection(control.buildProtocol,'20174.1.1.1',101)
	transport,protocol = loopC.run_until_complete(coroC)
	print("Client Connected. Starting UI t:{}. p:{}".format(transport, protocol))
	#control.connection_made(transport)
	control.setTransport(transport)
	pkt1 = DB_connect()
	control.sendpacket(pkt1)
	loopC.run_forever()
	loopC.close()

client_run()
