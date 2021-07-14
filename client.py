import asyncio
import websockets

WEBSOCKET_SERVER_URL ="wss://kedsouza-python-websockets.azurewebsites.net"

async def hello():
    async with websockets.connect(WEBSOCKET_SERVER_URL) as websocket:
        while True:
            message = await websocket.recv()
            print(message)

asyncio.get_event_loop().run_until_complete(hello())
