import asyncio
import websockets

WEBSOCKET_SERVER_URL ="ws://localhost:3000"

async def hello():
    async with websockets.connect(WEBSOCKET_SERVER_URL) as websocket:
        while True:
            message = await websocket.recv()
            print(message)

asyncio.get_event_loop().run_until_complete(hello())
