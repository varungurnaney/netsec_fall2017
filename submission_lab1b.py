"""
Author: Varun R Gurnaney
Email: varungurnaney@jhu.edu

Reference: 
1.Client sends a DB connection request to the server; 
db_connect();
2. Server requests the client   
connect_credentials(username, password)
3. Client responds with the correct/incorrect credentials  
response_credentials('root','toor')
4. Server sends the status (true is credentials are correct with session ID; false is the credentials are incorrect)
connection_response(status, sessionID)
"""

from playground.network.packet import PacketType
from playground.network.packet.fieldtypes import UINT32, STRING, BUFFER, BOOL

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
	
#Instantiating packet1 
pkt1 = DB_connect()

#Instantiating packet2 and populating fields
pkt2 = Connect_Credentials()
pkt2.username = "Please provide username"
pkt2.password = "Please provide password"

#Instantiating packet3 and populating fields
pkt3 = Response_Credentials()
pkt3.username = "root"
pkt3.password = "toor"

#Instantiating packet4 and populating fields
pkt4 = Connection_Response()
pkt4.status = True
pkt4.sessionID = "ABC1234"


#Serializing and De-serializing packet1
pkt1Serialized = pkt1.__serialize__()
print(pkt1Serialized)
pkt1DeSerialized = DB_connect.Deserialize(pkt1Serialized)
print(pkt1DeSerialized)
assert pkt1 == pkt1DeSerialized

#Serializing and De-serializing packet2
pkt2Serialized = pkt2.__serialize__()
print(pkt2Serialized)
pkt2DeSerialized = Connect_Credentials.Deserialize(pkt2Serialized)
print(pkt2DeSerialized)
assert pkt2 == pkt2DeSerialized

#Serializing and De-serializing packet3
pkt3Serialized = pkt3.__serialize__()
print(pkt3Serialized)
pkt3DeSerialized = Response_Credentials.Deserialize(pkt3Serialized)
print(pkt3DeSerialized)
assert pkt3 == pkt3DeSerialized

#Serializing and De-serializing packet4
pkt4Serialized = pkt4.__serialize__()
print(pkt4Serialized)
pkt4DeSerialized = Connection_Response.Deserialize(pkt4Serialized)
print(pkt4DeSerialized)
assert pkt4 == pkt4DeSerialized

print("End")














