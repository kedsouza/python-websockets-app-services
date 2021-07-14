import asyncio
import websockets
import os
import logging
import time

connected = set()

port = os.environ['PORT']

async def producer():
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    return current_time + " Number or connected clients: " + str(len(connected))

async def hello(websocket, path):
    try:
        while True:
            connected.add(websocket)
            message = await producer()
            await websocket.send(message)
            await asyncio.sleep(1)
    finally:
        connected.remove(websocket)

start_server = websockets.serve(hello, "0.0.0.0", port)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()