from RemoteNowApiWrapper import RemoteNowApi
import asyncio

# async main program (potentially fastapi)
async def main():
    sourceid = 2

    api = RemoteNowApi(hostname="192.168.200.60", identifer="devtest")

    api.register_handle_on_capability(printPayload)

    api.connect()

    await asyncio.sleep(5)

    api.getCapability()

    while True:
        await asyncio.sleep(5)

def printPayload(payload):
    print(payload)

asyncio.run(main())