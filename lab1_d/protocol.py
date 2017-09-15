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
	

