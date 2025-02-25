from RemoteNowApiWrapper import RemoteNowApi
import asyncio

# async main program (potentially fastapi)

async def main():
    sourceid = 2

    global api
    api = RemoteNowApi(hostname="192.168.200.60", identifer="devtest")

    api.register_handle_on_channelList(printPayload)
    api.register_handle_on_channelListInfo(printPayload)
    api.register_handle_on_capability(printPayload)
    api.register_handle_on_SourceList(printPayload)
    api.register_handle_on_state(printPayload)
    api.register_handle_on_tvInfo(printPayload)
    api.register_handle_on_sourceinsert(printPayload)
    api.register_handle_on_volumeChange(printPayload)
    api.register_handle_on_connected(printConnected)
    api.register_handle_on_disconnected(printDisconnected)

    api.connect()

    while True:
        await asyncio.sleep(5)

def printPayload(payload):
    print(payload)

def printConnected():
    print("Connected")

def printDisconnected():
    print("Disconnected")

asyncio.run(main())