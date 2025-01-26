from RemoteNowApiWrapper import RemoteNowApi
import asyncio

# async main program (potentially fastapi)

async def main():

    global api
    api = RemoteNowApi(hostname="192.168.200.60", identifer="devtest")

    api.register_handle_on_state(printPayload)

    api.connect()

    while(not api.get_Connected()):
        await asyncio.sleep(5)

def printPayload(payload):
    print(api._stateTopic)
    print(payload)

asyncio.run(main())