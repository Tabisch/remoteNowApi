from RemoteNowApiWrapper import RemoteNowApi
import asyncio

# async main program (potentially fastapi)
async def main():
    sourceid = 2

    api = RemoteNowApi(hostname="192.168.200.60", identifer="devtest")
    api.register_handle_on_connected(printConnected)
    api.register_handle_on_capability(printPayload)

    api.connect()

    connected = await api.async_get_Connected()

    while not connected:
        await asyncio.sleep(1)
        connected = await api.async_get_Connected()

    print("connected")

def printConnected():
    print("connected callback")

def printPayload(payload):
    print(payload)

asyncio.run(main())