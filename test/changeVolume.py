from RemoteNowApiWrapper import RemoteNowApi
import asyncio

# async main program (potentially fastapi)
async def main():
    volume = 0

    api = RemoteNowApi(hostname="192.168.200.60", identifer="devtest")

    api.register_handle_on_capability(printPayload)

    api.connect()

    await asyncio.sleep(5)

    api.getCapability()

    while True:
        await asyncio.sleep(5)
        api.changeVolume(volume)
        volume = volume + 1

def printPayload(payload):
    print(payload)

asyncio.run(main())