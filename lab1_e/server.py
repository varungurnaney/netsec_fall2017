from playground.network.packet import PacketType
from playground.network.common import StackingProtocol,StackingTransport,StackingProtocolFactory
from protocol import *
import asyncio
import playground
from playground.network.common import StackingProtocol
from passthrough import PassThrough1, PassThrough2

class ServerProtocol(asyncio.Protocol):

	def __init__(self):
		self.deserializer = PacketType.Deserializer()

			

	def connection_made(self, transport):
		print("Server Connected to Client ")
		self._deserializer = PacketType.Deserializer()		
		self.transport = transport
		"""pkt = Connect_Credentials()
		pkt.username = "Please provide username" 
		pkt.password = "Please provide password"
		self.send_packet(pkt)	"""
	

	def data_received(self, data):
	
		self._deserializer.update(data)
		for pkt in self._deserializer.nextPackets():

			if(pkt.DEFINITION_IDENTIFIER=="client_db_connect"):
				
				pkt = Connect_Credentials()
				pkt.username = "Please provide username" 
				pkt.password = "Please provide password"
				self.send_packet(pkt)
			
			if(pkt.DEFINITION_IDENTIFIER=="response_credentials"):	
				
				if(pkt.username=="root" and pkt.password=="toor"):
					pkt = Connection_Response()
					pkt.status = True
					pkt.sessionID = "ABC123"
					self.send_packet(pkt)
		
	def send_packet(self, packet):

		print("Server to Client-->",packet.DEFINITION_IDENTIFIER )
		self.transport.write(packet.__serialize__())
	
	def connection_lost(self, exc):
		print("Echo Server Connection Lost because {}".format(exc))



def server_run(): 

		f = StackingProtocolFactory(lambda: PassThrough1(), lambda: PassThrough2())
		ptConnector = playground.Connector(protocolStack=f)
		playground.setConnector("passthrough", ptConnector)	

		loop = asyncio.get_event_loop()
		coro = playground.getConnector('passthrough').create_playground_server(lambda: ServerProtocol(), 101)
		server = loop.run_until_complete(coro)
		print("Echo Server Started at {}".format(server.sockets[0].gethostname()))
		loop.run_forever()
		loop.close()

	


server_run()
