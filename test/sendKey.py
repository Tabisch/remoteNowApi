from RemoteNowApiWrapper import RemoteNowApi, keys
import asyncio

# async main program (potentially fastapi)

async def main():

    global api
    api = RemoteNowApi(hostname="192.168.200.60", identifer="devtest")

    api.connect()

    while(True):
        await asyncio.sleep(1)
        api.sendKey(keys.keyVolumeDown)

asyncio.run(main())