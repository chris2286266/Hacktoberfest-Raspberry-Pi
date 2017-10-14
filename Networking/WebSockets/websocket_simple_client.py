#
# Very simple WebSocket client
#	14.10.2017
# chris2286266
#

from websocket import create_connection

ws = create_connection("ws://echo.websocket.org/")
print("Sending 'Hello, World'...")
ws.send("Hello, World")
print("Sent")

print("Receiving...")
result =  ws.recv()
print("Received '%s'" % result)

ws.close()