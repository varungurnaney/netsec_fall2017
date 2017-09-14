
from protocol import *
import asyncio
import playground

class ServerProtocol(asyncio.Protocol):

	def connection_made(self, transport):
		print("Server Connected to Client ")
		self._deserializer = PacketType.Deserializer()		
		self.transport = transport
		pkt = Connect_Credentials()
		pkt.username = "Please provide username" 
		pkt.password = "Please provide password"
		self.send_packet(pkt)		
	

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

	loop = asyncio.get_event_loop()
	# Each client connection will create a new protocol instance
	coro = playground.getConnector().create_playground_server(ServerProtocol, '20174.1.1.1', 8000)
	server = loop.run_until_complete(coro)

	# Serve requests until Ctrl+C is pressed
	print('Serving on {}'.format(server.sockets[0].getsockname()))
	try:
		loop.run_forever()
	except KeyboardInterrupt:
		    pass

	# Close the server
	server.close()
	loop.run_until_complete(server.wait_closed())
	loop.close()

server_run()
