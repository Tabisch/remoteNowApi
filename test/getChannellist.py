from RemoteNowApiWrapper import RemoteNowApi
import asyncio

# async main program (potentially fastapi)

async def main():
    sourceid = 2

    global api
    api = RemoteNowApi(hostname="192.168.200.60", identifer="devtest")

    api.register_handle_on_channelList(printPayload)
    api.register_handle_on_channelListInfo(requestChannelList)

    api.connect()

    await asyncio.sleep(5)

    api.getChannelListInfo()

    while True:
        await asyncio.sleep(5)

def printPayload(payload):
    print(payload)

def requestChannelList(payload):
    print("requestChannelList")
    api.getChannelList(list_name=payload[0]["list_name"], list_para=payload[0]["list_para"])

asyncio.run(main())