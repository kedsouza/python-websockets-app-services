import asyncio
import websockets
import os
import logging


port = os.environ['PORT']
logger = logging.getLogger('websockets')
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())

print('Here')
print(port)


async def hello(websockets, path):
    name = await websockets.recv()
    print(f"< {name}")

    greeting = f"Hello {name}!"

    await websockets.send(greeting)
    print(f"> {greeting}")

start_server = websockets.serve(hello, "0.0.0.0", port )

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
    